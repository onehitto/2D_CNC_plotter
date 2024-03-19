from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QColor,QTextCursor
import re
import serial
import serial.tools.list_ports


class usb_widget(QGroupBox):
    emitinfo = pyqtSignal(dict)
    emitconnected = pyqtSignal(int) 
    def __init__(self):
        super().__init__("USB Communication:")
        
        #step window
        self.usbInfoLayout = QVBoxLayout()
        #clear / connect btn 
        self.usbInfoHLayout = QHBoxLayout()
        self.clearbtn = QPushButton('Clear')
        self.connectbtn = QPushButton('Connect')
        ports = serial.tools.list_ports.comports()
        self.dropbox = QComboBox()
        for port, desc, hwid in sorted(ports):
                self.dropbox.addItem(f"{port}: {desc} [{hwid}]")
        
        
        self.usbInfoHLayout.addWidget(self.clearbtn)
        self.usbInfoHLayout.addStretch(1)
        self.usbInfoHLayout.addWidget(self.dropbox)
        self.usbInfoHLayout.addWidget(self.connectbtn)
        

        # Communication widget for displaying incoming and outgoing messages
        self.commValue = QTextEdit()
        self.commValue.setReadOnly(True)
        self.usbInfoLayout.addWidget(self.commValue)
        self.usbInfoLayout.addLayout(self.usbInfoHLayout) 
        
        self.setLayout(self.usbInfoLayout)
        
        #variable
        
        self.serial_thread = None
        self.on_combobox_activated(self.dropbox.currentText())
        
        #connect events 
        self.dropbox.activated[str].connect(self.on_combobox_activated)
        self.clearbtn.clicked.connect(self.clear_event)
        self.connectbtn.clicked.connect(self.connect_com)
        
        
        #timers
        self.timer = QTimer()
        self.timer.timeout.connect(self.getinfo) # Connect timeout signal to timerFunction
        
        
        
        
     
    def connect_com(self):
        if self.connectbtn.text() == 'Connect':
            self.emitconnected.emit(True)
            self.connectbtn.setText('Disconnect')
            self.dropbox.setEnabled(False)
            self.serial_thread.open()
            self.serial_thread.start()
            self.timer.start(50)
        elif self.connectbtn.text() == 'Disconnect':
            self.emitconnected.emit(False)
            self.dropbox.setEnabled(True)
            self.connectbtn.setText('Connect')
            self.timer.stop() 
            self.serial_thread.stop()
               
        
    def update_display(self, data):  
        if "<InfoS" in data:
            self.emitinfo.emit(self.parse_servo_info(data))
        elif "<InfoM" in data:
            self.emitinfo.emit(self.parse_motor_info(data))
        else:  
            self.append_colored_text(data, QColor('blue'))

        
    def closeEvent(self, event):
        self.serial_thread.stop()
        super().closeEvent(event)
    
    def clear_event(self):
        self.commValue.clear()
    
    def send_data(self,data):
        self.append_colored_text(data,QColor('red'))
        self.serial_thread.write_data(data)
        
    def getinfo(self):
         self.serial_thread.write_data('info')
    
    def on_combobox_activated(self,text):
        match = re.search(r'(COM\d+)', text)
        if match:
            com_port = match.group(1)
            self.serial_thread = Serial_Thread(com_port,115200)
            self.serial_thread.received_signal.connect(self.update_display)
        else:
            self.Qdiag = SimpleDialog("COM Port not found.")
            self.Qdiag.setFixedSize(170, 80)
            self.Qdiag.show()
            
        
    def append_colored_text(self, text, color):
        cursor = self.commValue.textCursor()
        cursor.movePosition(QTextCursor.End)
        
        char_format = cursor.charFormat()
        char_format.setForeground(color)
        cursor.setCharFormat(char_format)
        
        cursor.insertText(text + '\n')
        
        self.commValue.moveCursor(QTextCursor.End)      
        
    def parse_motor_info(self,message):
        pattern = r"<Info(M[12])>(\d+),(\d+),(\d+),(-?\d+),(\d+),(\d+),(\d+),(\d+)"
        # Search for the pattern in the message
        match = re.search(pattern, message)
        if match:
            # Extract the data from the matched groups
            motor_id, status, steps_count, tar_steps, num_steps, dir_conf, ms1, ms2, ms3 = match.groups()
            
            # Convert the extracted strings to their appropriate data types
            data = {
                "MotorID": motor_id,
                "Status": int(status),
                "StepsCount": int(steps_count),
                "TargetSteps": int(tar_steps),
                "NumSteps": int(num_steps),
                "DIR": int(dir_conf),
                "MS1": int(ms1),
                "MS2": int(ms2),
                "MS3": int(ms3),
            }
            return data
        else:
            return None
        
    def parse_servo_info(self,message):
        """
        Parses a servo information message and returns a dictionary with the parsed data.

        Args:
        - message (str): The message to be parsed.

        Returns:
        - dict: A dictionary containing the parsed information with fields:
            - Status: The current status of the servo.
            - CurrentPosition: The current position of the servo.
            - CCR1: The Capture/Compare Register value.
            - Prescaler: The prescaler value for the timer.
            - Period: The period value for the timer.
        """
        pattern = r"<InfoServo>(\d+),(\d+),(\d+),(\d+),(\d+)"
        
        # Search for the pattern in the message
        match = re.search(pattern, message)
        if match:
            # Extract the data from the matched groups
            status, curr_pos, ccr1, prescaler, period = match.groups()
            
            # Convert the extracted strings to their appropriate data types
            data = {
                "Status": int(status),
                "CurrentPosition": int(curr_pos),
                "CCR1": int(ccr1),
                "Prescaler": int(prescaler),
                "Period": int(period),
            }
            return data
        else:
            return None




class Serial_Thread(QThread):
    """
    This thread is responsible for handling serial communication
    asynchronously to prevent freezing the GUI.
    """
    received_signal = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.port = port
        self.baudrate = baudrate
        self.running = False
        self.serial = serial.Serial(self.port, baudrate=self.baudrate, timeout=0.1)
        self.serial.close()
        
    def run(self):
        while self.running:
            if self.serial.inWaiting() > 0:
                data = self.serial.readline().decode('utf-8').strip()
                self.received_signal.emit(data)
        if (self.running == False and self.serial != None):
            self.serial.close()



    def write_data(self, data):
        self.serial.write(data.encode())

    def stop(self):
        self.running = False

        
    def open(self):
        self.serial.open()  
        self.running = True
        
        


if __name__ == "__main__":
    app = QApplication([])
    gui = usb_widget()
    gui.show()
    app.exec_()


class SimpleDialog(QDialog):
    def __init__(self,msg):
        super().__init__()
        
        # Set the dialog title
        self.setWindowTitle('Warrning')
        
        # Create and set the layout
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        # Add a label
        self.label = QLabel(msg)
        layout.addWidget(self.label)
        
        # Add a button to close the dialog
        self.button = QPushButton('Close')
        self.button.clicked.connect(self.close)
        layout.addWidget(self.button)