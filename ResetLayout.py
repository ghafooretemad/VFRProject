from PyQt5.QtWidgets import QMainWindow, QFormLayout
from PyQt5.QtGui import QIcon
from forgotPassword import *

class ResetLayout(QMainWindow):
    def __init__(self, parent=None):
        super(ResetLayout,  self).__init__(parent)
        self.top = 130
        self.left = 150
        self.width = 500
        self.height = 250
        self.layout = QFormLayout()        
        self.setUpUi()
    def setUpUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        resetForm = ResetForm(self)
        self.setCentralWidget(resetForm)
        self.setWindowIcon(QIcon("Icon.jpg"))
        self.setWindowTitle("Reset Password")

