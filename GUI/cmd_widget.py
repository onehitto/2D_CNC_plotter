#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Cmd_widget(QWidget):
    def __init__(self,name):
        super().__init__()
        
        # Create layout
        self.layout = QVBoxLayout()
        self.cmdlayout = QHBoxLayout()
        self.infolayout = QHBoxLayout()
        self.Label = QLabel(name)
        self.Value = QLineEdit('')
        self.Value.setMaxLength(6) 
        self.Value.setFixedWidth(40)
        self.Value.setFixedHeight(20)
        self.Value.setReadOnly(True)
        self.infolayout.addStretch(1)
        self.infolayout.addWidget(self.Label)
        self.infolayout.addWidget(self.Value)
        self.infolayout.addStretch(2)
        # Widtget for labels and text edit + configuration
        self.rightbtn1 = QPushButton('>')
        self.rightbtn2 = QPushButton('>>')
        self.rightbtn3 = QPushButton('>>>')
        self.leftbtn1 = QPushButton('<')
        self.leftbtn2 = QPushButton('<<')
        self.leftbtn3 = QPushButton('<<<')
        self.cmdlayout.addWidget(self.leftbtn3)
        self.cmdlayout.addWidget(self.leftbtn2)
        self.cmdlayout.addWidget(self.leftbtn1)
        self.cmdlayout.addWidget(self.rightbtn1)
        self.cmdlayout.addWidget(self.rightbtn2)
        self.cmdlayout.addWidget(self.rightbtn3)
        
        self.layout.addLayout(self.infolayout)
        self.layout.addLayout(self.cmdlayout)
        
        self.setLayout(self.layout)
        

class Cmd_widgetlight(QWidget):
    def __init__(self,name):
        super().__init__()
        
        # Create layout
        self.layout = QVBoxLayout()
        self.cmdlayout = QHBoxLayout()
        self.infolayout = QHBoxLayout()
        self.Label = QLabel(name)
        self.Value = QLineEdit('')
        self.Value.setMaxLength(6) 
        self.Value.setFixedWidth(40)
        self.Value.setFixedHeight(20)
        self.Value.setReadOnly(True)
        self.infolayout.addStretch(1)
        self.infolayout.addWidget(self.Label)
        self.infolayout.addWidget(self.Value)
        self.infolayout.addStretch(1)
        # Widtget for labels and text edit + configuration
        self.rightbtn1 = QPushButton('>')
        self.rightbtn2 = QPushButton('>>')
        self.leftbtn1 = QPushButton('<')
        self.leftbtn2 = QPushButton('<<')
        self.cmdlayout.addWidget(self.leftbtn2)
        self.cmdlayout.addWidget(self.leftbtn1)
        self.cmdlayout.addWidget(self.rightbtn1)
        self.cmdlayout.addWidget(self.rightbtn2)
        
        self.layout.addLayout(self.infolayout)
        self.layout.addLayout(self.cmdlayout)
        
        self.setLayout(self.layout)
if __name__ == "__main__":
    app = QApplication([])
    gui = Cmd_widgetlight('test')
    gui.show()
    app.exec_()
