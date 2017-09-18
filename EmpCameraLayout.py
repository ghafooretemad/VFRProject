from PyQt5.QtWidgets import QMainWindow, QFormLayout
from PyQt5.QtGui import QIcon
from StartCamera import *

class EmpCameraLayout(QMainWindow):
    def __init__(self,  selectedMode,  ID, parent=None):
        super(EmpCameraLayout,  self).__init__(parent)
        self.top = 30
        self.left = 50
        self.width = 400
        self.height = 400
        self.layout = QFormLayout()
        self.ID = ID
        self.selectedMode = selectedMode
        
        self.setUpUi()
    def setUpUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        camera = StartCamera(self.selectedMode,  self.ID,  self)
        camera.start()
        self.setCentralWidget(camera)
        self.setWindowIcon(QIcon("Icon.jpg"))
        self.setWindowTitle("Cupture Face")
