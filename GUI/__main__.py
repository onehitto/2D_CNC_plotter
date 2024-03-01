#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from cmd_widget import *

class Gui_2D(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(700, 600)
        # splitter fix
        splitter =  QSplitter(Qt.Horizontal)
        # Create layout
        mainlayout = QHBoxLayout()
        # Widtget for labels and text edit + configuration
        self.motorInfoWidget = QWidget()
        self.motorInfoWidget.setMinimumWidth(300)
        self.motorInfoWidget.setMaximumWidth(300)
        self.motorInfoLayoutMain = QVBoxLayout(self.motorInfoWidget)
        
        self.motorInfoGroup = QGroupBox("Motor Information")

        self.motorInfoGroupLayout = QVBoxLayout(self.motorInfoGroup)
        # Step motor X label and text edit
        self.stepMotor1 = Cmd_widget("Steps Motor 1 :")

        # Step motor Y label and text edit
        self.stepMotor2 = Cmd_widget("Steps Motor 1 :")

        # Servo motor label and text edit
        self.servoMotor = Cmd_widget("Servo Motor   :")
        
        # XY  :
        self.XYlayout = QHBoxLayout()
        self.XWidget = Cmd_widgetlight("X :")
        self.YWidget = Cmd_widgetlight("Y:")       
   
        # layout
        self.XYlayout.addWidget(self.XWidget)
        self.XYlayout.addWidget(self.YWidget)
        
        self.motorInfoGroupLayout.addWidget(self.stepMotor1)
        self.motorInfoGroupLayout.addWidget(self.stepMotor2)
        self.motorInfoGroupLayout.addWidget(self.servoMotor)
        self.motorInfoGroupLayout.addLayout(self.XYlayout)
        self.motorInfoGroupLayout.addStretch(1)
        
        
        #Motor Control
        self.motorInfoGroup2 = QGroupBox("Motor Control")
        self.motorInfoGroup2.setMinimumWidth(200)
        self.motorInfoGroup2.setMaximumWidth(200)
        self.motorInfoGroup2Layout = QGridLayout(self.motorInfoGroup2)
        
        
        #layout config
        #self.motorInfoGroupLayout.setRowStretch(self.motorInfoGroupLayout.rowCount(), 1)
        #self.motorInfoGroupLayout.setColumnStretch(self.motorInfoGroupLayout.columnCount(), 1)
        
        
        self.motorInfoLayoutMain.addWidget(self.motorInfoGroup)
        self.motorInfoLayoutMain.addWidget(self.motorInfoGroup2)
        
        
        usbInfoWidget = QGroupBox("USB Communication:")
        usbInfoLayout = QVBoxLayout(usbInfoWidget)
        # Communication widget for displaying incoming and outgoing messages
        self.commValue = QTextEdit()
        self.commValue.setReadOnly(True)
        usbInfoLayout.addWidget(self.commValue)

        splitter.addWidget(self.motorInfoWidget)
        splitter.addWidget(usbInfoWidget)
        splitter.setCollapsible(0,False)
        splitter.setSizes([200, 400])
        # Set the layout on the application's window
        mainlayout.addWidget(splitter)
        self.setLayout(mainlayout)

if __name__ == "__main__":
    app = QApplication([])
    gui = Gui_2D()
    gui.show()
    app.exec_()
