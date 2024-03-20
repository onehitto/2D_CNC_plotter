#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from GUI.cmd_widget import *
from GUI.config_widget import *
from GUI.usb_widget import *

class Gui_2D(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 600)
        # splitter fix
        splitter =  QSplitter(Qt.Horizontal)
        # Create layout
        mainlayout = QHBoxLayout()
        
        
        # motor info Widget
        self.motorInfoWidget = QWidget()
        self.motorInfoWidget.setMinimumWidth(300)
        self.motorInfoWidget.setMaximumWidth(300)
        self.motorInfoLayoutMain = QVBoxLayout(self.motorInfoWidget)
        self.motorInfoLayoutMain.setContentsMargins(0, 0, 0, 0)
        
        #tab motor info / config
        
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.tab_1(), "Control")
        self.tabWidget.addTab(self.tab_2(), "Config")
        
        #Motor Control
        self.GcodeGroup = QGroupBox("Gcode Commands")
        self.GcodeGroup.setMinimumWidth(300)
        self.GcodeGroup.setMaximumWidth(300)
        self.GcodeLayout = QVBoxLayout(self.GcodeGroup)
        self.Gcodewidget = CmdGcode_widget("Command :")
        self.GcodeLayout.addWidget(self.Gcodewidget)
        self.GcodeLayout.addStretch(1)
        
        #layout config
        #self.motorInfoGroupLayout.setRowStretch(self.motorInfoGroupLayout.rowCount(), 1)
        #self.motorInfoGroupLayout.setColumnStretch(self.motorInfoGroupLayout.columnCount(), 1)
        
        self.infolabel = QLabel()
        
        
        self.motorInfoLayoutMain.addWidget(self.tabWidget)
        self.motorInfoLayoutMain.addWidget(self.GcodeGroup)
        self.motorInfoLayoutMain.addWidget(self.infolabel)
        self.motorInfoLayoutMain.addStretch(1)
        
        
        self.usbInfoWidget = usb_widget()
           
        splitter.addWidget(self.motorInfoWidget)
        splitter.addWidget(self.usbInfoWidget)
        splitter.setCollapsible(0,False)
        splitter.setSizes([200, 400])
        # Set the layout on the application's window
        mainlayout.addWidget(splitter)
        self.setLayout(mainlayout)
        
        
        # Events
        self.usbInfoWidget.emitconnected.connect(self.onstatecmd)
        self.Gcodewidget.sendbtn.clicked.connect(self.onsend_cmd)
        self.usbInfoWidget.emitinfo.connect(self.onupdateui)
        self.configWidget.emitconf.connect(self.onsend_conf)
        self.tabWidget.currentChanged.connect(self.onchangetab)
        
        #Disable tab in init wait the connect event to enable it
        self.tabWidget.setTabEnabled(1, False)
        

    def tab_1(self):
        
        #self.motorInfoGroup = QGroupBox("Motor Information / Raw Control ")
        self.motorInfoGroup = QWidget()
        self.motorInfoGroupLayout = QVBoxLayout(self.motorInfoGroup)
        
        # Step motor X label and text edit
        self.stepMotor1_wd = Cmd_widget("Steps Motor 1 :")

        # Step motor Y label and text edit
        self.stepMotor2_wd = Cmd_widget("Steps Motor 2 :")

        # Servo motor label and text edit
        self.servoMotor_wd = Cmd_widget("  Servo Motor :")
        
        # XY  :
        self.XYlayout = QHBoxLayout()
        self.separatorLine = QFrame()
        self.separatorLine.setFrameShape( QFrame.VLine )
        self.separatorLine.setFrameShadow( QFrame.Raised )
        self.XYlayout.setContentsMargins(0, 0, 0, 0)
        self.XWidget = Cmd_widgetlight("X :")
        self.YWidget = Cmd_widgetlight("Y:")       
   
        # layout
        self.XYlayout.addWidget(self.XWidget)
        self.XYlayout.addWidget(self.separatorLine)
        self.XYlayout.addWidget(self.YWidget)
        
        self.motorInfoGroupLayout.addWidget(self.stepMotor1_wd)
        self.motorInfoGroupLayout.addWidget(self.stepMotor2_wd)
        self.motorInfoGroupLayout.addWidget(self.servoMotor_wd)
        self.motorInfoGroupLayout.addLayout(self.XYlayout)
        self.motorInfoGroupLayout.addStretch(1)
        
        self.stepMotor1_wd.btn_signal.connect(lambda dir,step: self.onstep_cmd(1,dir,step))
        self.stepMotor2_wd.btn_signal.connect(lambda dir,step: self.onstep_cmd(2,dir,step))
        
        return self.motorInfoGroup
    
    def tab_2(self):
        self.configWidget = configmotor_widget()
        self.configWidget.loadSettings()
        return self.configWidget

    def onsend_cmd(self):
        if self.Gcodewidget.Value.toPlainText() != '':
            self.usbInfoWidget.send_data(self.Gcodewidget.Value.toPlainText())
        
    def onsend_conf(self,conf):
        self.usbInfoWidget.send_data("conf:M1:" + conf +":M2:" + conf)
        
    def onstep_cmd(self,M,dir,step):
        if dir == 'r':
            self.usbInfoWidget.send_data('cmd:M'+ str(M) +':' + str(step) + ':1')
        else:
            self.usbInfoWidget.send_data('cmd:M'+ str(M) +':' + str(step) + ':0')
            
    def onstatecmd(self,value):
        self.stepMotor1_wd.cmd_state(value)
        self.stepMotor2_wd.cmd_state(value)
        self.servoMotor_wd.cmd_state(value)
        self.Gcodewidget.sendbtn.setEnabled(value)
        self.tabWidget.setTabEnabled(1, value)
        
    def onupdateui(self,data):
        if 'MotorID' in data:
            if data['MotorID'] == 'M1':
                self.stepMotor1_wd.Value.setText(str(data['NumSteps']))
            elif data['MotorID'] == 'M2':
                self.stepMotor2_wd.Value.setText(str(data['NumSteps']))
            if data['MS3'] == 0 and data['MS2'] == 0 and data['MS1'] == 0:
                self.conf = "Full Step 1/1"
            elif data['MS3'] == 0 and data['MS2'] == 0 and data['MS1'] == 1:
                self.conf = "Half Step 1/2"
            elif data['MS3'] == 0 and data['MS2'] == 1 and data['MS1'] == 0:
                self.conf = "Quarter Step 1/4"
            elif data['MS3'] == 1 and data['MS2'] == 1 and data['MS1'] == 0:
                self.conf = "Eighth Step 1/8"
            elif data['MS3'] == 1 and data['MS2'] == 1 and data['MS1'] == 1:
                self.conf = "Sixteenth Step 1/16"
            self.infolabel.setText('Current Configuration : '+ self.conf +' (' +str(data['MS3']) + str(data['MS2']) + str(data['MS1'])+ ')')

    def onchangetab(self,index):
        if index == 1:
            self.configWidget.smconfigcomboBox.setCurrentText(self.conf)
                

if __name__ == "__main__":
    app = QApplication([])
    gui = Gui_2D()
    gui.show()
    app.exec_()
