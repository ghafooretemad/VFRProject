from PyQt5.QtWidgets import QMainWindow, QFormLayout
from PyQt5.QtGui import QIcon
from AdminTabs import *

class AdministrationWindow(QMainWindow):
    def __init__(self,  parent=None):
        super(AdministrationWindow,  self).__init__(parent)
        self.top = 30
        self.left = 50
        self.width = 800
        self.height = 500
        self.layout = QFormLayout()
        
        self.setUpUi()
    def setUpUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        tabs = AdminTabs(self)
        self.setCentralWidget(tabs)
        self.setWindowIcon(QIcon("Icon.jpg"))
        self.setWindowTitle("Administration Window")

