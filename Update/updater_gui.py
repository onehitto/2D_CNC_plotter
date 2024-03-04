from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget,QPushButton,QLabel
import sys
from PyQt5.QtWidgets import QAbstractItemView,QHeaderView,QTableWidgetItem
from PyQt5.QtCore import Qt
from update_req import *

class VersionInfoWindow(QWidget):
    def __init__(self, obj):
        super().__init__()
        self.title = 'Version Information'
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 400
        self.version_data = obj.versions
        self.current = obj.config['settings']['current_version']

        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create table
        self.createTable()
        self.label = QLabel(f"the current is :{self.current}")
        # Create a central widget
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout )
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.tableWidget) 
        self.adjustSizeToTable()
        # Show widget
        self.show()

    def createTable(self):
        # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(len(self.version_data))
        self.tableWidget.setColumnCount(4)  # Added an extra column for the download buttons
        self.tableWidget.setHorizontalHeaderLabels(['Version', 'Name', 'Description', ' '])
        
        for i, version_info in enumerate(self.version_data):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(version_info['tag_name']))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(version_info['name']))
            
            # Make the link clickable
            linkLabel = QLabel(f'<a href="{version_info["link"]}">{version_info["link"]}</a>')
            linkLabel.setOpenExternalLinks(True)  # Open links externally by default
            self.tableWidget.setCellWidget(i, 2, linkLabel)

            # Create a download button and set its 'clicked' signal
            downloadBtn = QPushButton('Download')
            downloadBtn.clicked.connect(lambda state, url=version_info.get('exe_url'): self.download_file(url))
            self.tableWidget.setCellWidget(i, 3, downloadBtn)
        
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setSelectionMode(QTableWidget.NoSelection)
        self.tableWidget.setEditTriggers(QTableWidget.NoEditTriggers)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        
        
    def adjustSizeToTable(self):
        width = self.tableWidget.verticalHeader().width() + 50  # margin
        height = self.tableWidget.horizontalHeader().height() + 60  # margin
        for column in range(self.tableWidget.columnCount()):
            width += self.tableWidget.columnWidth(column)
        for row in range(self.tableWidget.rowCount()):
            height += self.tableWidget.rowHeight(row)
        
        # Adjust the size of the window
        self.resize(width, height)
        self.setFixedSize(self.size())
        
    def download_file(self, url):
        print(url)
        
def main():
    # Your code here
    obj = app_def()
    obj.check_for_updates()
    app = QApplication(sys.argv)
    ex = VersionInfoWindow(obj)
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()