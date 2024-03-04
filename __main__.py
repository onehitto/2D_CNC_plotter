#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from GUI.cmd_widget import *
from GUI.config_widget import *

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
        
        
        self.motorInfoLayoutMain.addWidget(self.tabWidget)
        self.motorInfoLayoutMain.addWidget(self.GcodeGroup)
        self.motorInfoLayoutMain.addStretch(1)
        
        
        self.usbInfoWidget = QGroupBox("USB Communication:")
        self.usbInfoLayout = QVBoxLayout(self.usbInfoWidget)
        #clear / connect btn 
        self.usbInfoHLayout = QHBoxLayout()
        self.clearbtn = QPushButton('Clear')
        self.connectbtn = QPushButton('Connect')
        self.usbInfoHLayout.addWidget(self.clearbtn)
        self.usbInfoHLayout.addStretch(1)
        self.usbInfoHLayout.addWidget(self.connectbtn)
        # Communication widget for displaying incoming and outgoing messages
        self.commValue = QTextEdit()
        self.commValue.setReadOnly(True)
        self.usbInfoLayout.addWidget(self.commValue)
        self.usbInfoLayout.addLayout(self.usbInfoHLayout) 
           
        splitter.addWidget(self.motorInfoWidget)
        splitter.addWidget(self.usbInfoWidget)
        splitter.setCollapsible(0,False)
        splitter.setSizes([200, 400])
        # Set the layout on the application's window
        mainlayout.addWidget(splitter)
        self.setLayout(mainlayout)

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
        
        return self.motorInfoGroup
    
    def tab_2(self):
        self.configWidget = configmotor_widget()
        self.configWidget.loadSettings()
        return self.configWidget

if __name__ == "__main__":
    app = QApplication([])
    gui = Gui_2D()
    gui.show()
    app.exec_()
