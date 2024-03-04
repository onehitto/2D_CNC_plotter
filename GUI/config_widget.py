#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import json
import sys

class configmotor_widget(QWidget):
    def __init__(self):
        super().__init__()
        
        # default location for saving files
        self.settingsFile ='.\\cache\\configwideget.json'
        # Create layout
        self.layout = QVBoxLayout()
        self.Vlayout = QVBoxLayout()
        
        
        self.layout.setContentsMargins(0, 0, 0, 10)
        self.Vlayout.setContentsMargins(0, 0, 0, 0)
        
        
        # Setp motors config
        self.smconfigLabel = QLabel("Step Motor configuration :")
        self.smconfigcomboBox = QComboBox()
        
        # options 
        self.smconfigcomboBox.addItem("Option 1")
        self.smconfigcomboBox.addItem("Option 2")
        # layout 
        self.Vlayout.addWidget(self.smconfigLabel)
        self.Vlayout.addWidget(self.smconfigcomboBox)

        # sensor end/stop config
        self.sensorconfigLabel = QLabel("Sensor End/Stop configuration :")
        self.sensorconfigcomboBox = QComboBox()
        
        # options 
        self.sensorconfigcomboBox.addItem("Option 1")
        self.sensorconfigcomboBox.addItem("Option 2")
        # layout 
        self.Vlayout.addWidget(self.sensorconfigLabel)
        self.Vlayout.addWidget(self.sensorconfigcomboBox)
       
       
        # Motor speed : 

        self.speedconfiglabel = QLabel("Motor speed :")
        self.speedconfigcomboBox = QComboBox()
        
        # options 
        self.speedconfigcomboBox.addItem("Option 1")
        self.speedconfigcomboBox.addItem("Option 2")
        # layout 
        self.Vlayout.addWidget(self.speedconfiglabel)
        self.Vlayout.addWidget(self.speedconfigcomboBox)
        
        #push button apply
        self.applybtn = QPushButton('Apply')
        self.applybtn.clicked.connect(self.saveSettings)
        
        self.layout.addLayout(self.Vlayout)
        
        self.layout.addStretch(1)
        self.layout.addWidget(self.applybtn)
        
        self.setLayout(self.layout)
        
        
    def saveSettings(self):
        settings = {
            "step_motor_config": self.smconfigcomboBox.currentIndex(),
            "sensor_config": self.sensorconfigcomboBox.currentIndex(),
            "motor_speed": self.speedconfigcomboBox.currentIndex(),
        }

        with open(self.settingsFile, 'w') as file:
            json.dump(settings, file)
            
    def loadSettings(self):
        try:
            with open(self.settingsFile, 'r') as file:
                settings = json.load(file)
                self.smconfigcomboBox.setCurrentIndex(settings["step_motor_config"])
                self.sensorconfigcomboBox.setCurrentIndex(settings["sensor_config"])
                self.speedconfigcomboBox.setCurrentIndex(settings["motor_speed"])
        except FileNotFoundError:
            print("Settings file not found. Loading defaults.")
       


if __name__ == "__main__":
    app = QApplication([])
    gui = configmotor_widget()
    gui.show()
    app.exec_()
