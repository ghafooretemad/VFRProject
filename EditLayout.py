from PyQt5.QtWidgets import QMainWindow, QFormLayout
from PyQt5.QtGui import QIcon
from EditForm import *

class EditLayout(QMainWindow):
    def __init__(self,  ID, parent=None):
        super(EditLayout,  self).__init__(parent)
        self.parent = parent
        self.top = 30
        self.left = 50
        self.width = 500
        self.height = 400
        self.layout = QFormLayout()
        self.ID = ID
        
        self.setUpUi()
    def setUpUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        editForm = EditForm(self.ID, self.parent,  self)
        self.setCentralWidget(editForm)
        self.setWindowIcon(QIcon("Icon.jpg"))
        self.setWindowTitle("Edit User")

