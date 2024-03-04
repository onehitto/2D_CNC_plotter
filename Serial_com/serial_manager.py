from PyQt5.QtCore import QThread, pyqtSignal
import serial

class SerialThread(QThread):
    """
    This thread is responsible for handling serial communication
    asynchronously to prevent freezing the GUI.
    """
    received_signal = pyqtSignal(str)

    def __init__(self, port, baudrate):
        super().__init__()
        self.serial = serial.Serial(port, baudrate=baudrate, timeout=0.1)
        self.running = True

    def run(self):
        while self.running:
            if self.serial.inWaiting() > 0:
                data = self.serial.readline().decode('utf-8').strip()
                self.received_signal.emit(data)

    def write_data(self, data):
        self.serial.write(data.encode())

    def stop(self):
        self.running = False
        self.serial.close()
        
    def open(self):
        self.running = True
        self.serial.open()
        