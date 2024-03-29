#from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton,QHBoxLayout,QLineEdit,QSplitter,QGridLayout,QSizePolicy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt, pyqtSignal

class Cmd_widget(QWidget):
    
    btn_signal = pyqtSignal(str,int)
    
    def __init__(self,name):
        super().__init__()
        
        # Create layout
        self.layout = QVBoxLayout()
        self.cmdlayout = QHBoxLayout()
        self.infolayout = QHBoxLayout()
        
        self.layout.setContentsMargins(0, 0, 0, 10)
        self.cmdlayout.setContentsMargins(0, 0, 0, 0)
        self.infolayout.setContentsMargins(0, 0, 0, 0)
        
        self.Label = QLabel(name)
        self.Value = QLineEdit('')
        self.Value.setMaxLength(6) 
        self.Value.setFixedWidth(40)
        self.Value.setFixedHeight(20)
        self.Value.setReadOnly(True)
        self.infolayout.addStretch(1)
        self.infolayout.addWidget(self.Label)
        self.infolayout.addWidget(self.Value)
        self.infolayout.addStretch(3)
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
        
        self.leftbtn1.clicked.connect(lambda: self.cmd_event('l', 1))
        self.leftbtn2.clicked.connect(lambda: self.cmd_event('l', 10))
        self.leftbtn3.clicked.connect(lambda: self.cmd_event('l', 100))
        self.rightbtn1.clicked.connect(lambda: self.cmd_event('r', 1))
        self.rightbtn2.clicked.connect(lambda: self.cmd_event('r', 10))
        self.rightbtn3.clicked.connect(lambda: self.cmd_event('r', 100))
        
        self.cmd_state(False)
    
    def cmd_event(self,dir,step):
        self.btn_signal.emit(dir,step)
        
    def cmd_state(self,value):
        self.leftbtn1.setEnabled(value)
        self.leftbtn2.setEnabled(value)
        self.leftbtn3.setEnabled(value)
        self.rightbtn1.setEnabled(value)
        self.rightbtn2.setEnabled(value)
        self.rightbtn3. setEnabled(value)
        
        

class Cmd_widgetlight(QWidget):
    def __init__(self,name):
        super().__init__()
        
        # Create layout
        self.layout = QVBoxLayout()
        self.cmdlayout = QHBoxLayout()
        self.infolayout = QHBoxLayout()
        
        self.layout.setContentsMargins(0, 0, 0, 10)
        self.cmdlayout.setContentsMargins(0, 0, 0, 0)
        self.infolayout.setContentsMargins(0, 0, 0, 0)
        
        
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
        
class CmdGcode_widget(QWidget):
    def __init__(self,name):
        super().__init__()
        
        # Create layout
        self.layout = QVBoxLayout()
        self.Hlayout = QHBoxLayout()
        
        self.layout.setContentsMargins(0, 0, 0, 10)
        self.Hlayout.setContentsMargins(0, 0, 0, 0)
        
        self.Label = QLabel(name)
        self.Value = QTextEdit('') 
        self.Value.setFixedHeight(50)
        
        self.sendbtn = QPushButton('Send')
        self.sendbtn.setFixedHeight(20)
        self.sendbtn.setFixedWidth(50)
        
        self.Hlayout.addWidget(self.Label)
        self.Hlayout.addStretch(1)
        self.Hlayout.addWidget(self.sendbtn)
        
        self.layout.addLayout(self.Hlayout)
        self.layout.addWidget(self.Value)
        # Widtget for labels and text edit + configuration
        
        
        self.setLayout(self.layout)
        
        #properties
        self.sendbtn.setEnabled(False)
        
if __name__ == "__main__":
    app = QApplication([])
    gui = CmdGcode_widget('test')
    gui.show()
    app.exec_()
