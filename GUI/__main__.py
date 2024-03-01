#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Gui_2D(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(550, 400)
        # splitter fix
        splitter =  QSplitter(Qt.Horizontal)
        # Create layout
        mainlayout = QHBoxLayout()
        # Widtget for labels and text edit + configuration 
        motorInfoWidget = QWidget()
        motorInfoWidget.setMinimumWidth(200)
        motorInfoWidget.setMaximumWidth(200)
        motorInfoLayoutMain = QGridLayout(motorInfoWidget)
        # Step motor X label and text edit
        self.stepMotorXLabel = QLabel("Steps Motor 1 :")
        self.stepMotorXValue = QLineEdit('')
        self.stepMotorXValue.setMaxLength(7) 
        self.stepMotorXValue.setFixedWidth(45)
        self.stepMotorXValue.setReadOnly(True)
        motorInfoLayoutMain.addWidget(self.stepMotorXLabel,0,0)
        motorInfoLayoutMain.addWidget(self.stepMotorXValue,0,1)

        # Step motor Y label and text edit
        self.stepMotorYLabel = QLabel("Steps Motor 2 :")
        self.stepMotorYValue = QLineEdit('')
        self.stepMotorYValue.setMaxLength(7) 
        self.stepMotorYValue.setFixedWidth(45)
        self.stepMotorYValue.setReadOnly(True)
        motorInfoLayoutMain.addWidget(self.stepMotorYLabel,1,0)
        motorInfoLayoutMain.addWidget(self.stepMotorYValue,1,1)

        # Servo motor label and text edit
        self.servoMotorLabel = QLabel("Servo Motor   :")
        self.servoMotorValue = QLineEdit('')
        self.servoMotorValue.setMaxLength(7) 
        self.servoMotorValue.setFixedWidth(45)
        self.servoMotorValue.setReadOnly(True)
        motorInfoLayoutMain.addWidget(self.servoMotorLabel,2,0)
        motorInfoLayoutMain.addWidget(self.servoMotorValue,2,1)
        
        # X  :
        self.Xlayout = QHBoxLayout()
        self.XLabel = QLabel("X :")
        self.XValue = QLineEdit('')
        self.XValue.setMaxLength(7) 
        self.XValue.setFixedWidth(45)
        self.Xlayout.setStretch(0,1)
        self.Xlayout.addWidget(self.XLabel,alignment= Qt.AlignRight)
        self.Xlayout.addWidget(self.XValue)
        
        # Y  :
        self.Ylayout = QHBoxLayout()
        self.YLabel = QLabel("Y:")
        self.YValue = QLineEdit('')
        self.YValue.setMaxLength(7) 
        self.YValue.setFixedWidth(45)
        self.Ylayout.addWidget(self.YLabel)
        self.Ylayout.addWidget(self.YValue)
        
        motorInfoLayoutMain.addLayout(self.Xlayout,3,0)
        motorInfoLayoutMain.addLayout(self.Ylayout,3,1)
        
        #layout config
        motorInfoLayoutMain.setRowStretch(motorInfoLayoutMain.rowCount(), 1)
        motorInfoLayoutMain.setColumnStretch(motorInfoLayoutMain.columnCount(), 1)
        
        
        
        
        
        usbInfoWidget = QWidget()
        usbInfoLayout = QVBoxLayout(usbInfoWidget)
        # Communication widget for displaying incoming and outgoing messages
        self.commLabel = QLabel("USB Communication:")
        self.commValue = QTextEdit()
        self.commValue.setReadOnly(True)
        
        usbInfoLayout.addWidget(self.commLabel)
        usbInfoLayout.addWidget(self.commValue)

        splitter.addWidget(motorInfoWidget)
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
