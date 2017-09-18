from PyQt5.QtWidgets import QApplication, QMainWindow
import sys
from PyQt5.QtGui import QIcon
from AllTabs import *
class VFRMainWindow(QMainWindow):
    def __init__(self):
        super(VFRMainWindow,  self).__init__()
    
        self.top = 60
        self.left = 80
        self.width = 800
        self.height = 500
        self.setUpUi()
    def setUpUi(self):
        self.setGeometry(self.left, self.top, self.width, self.height)
        tabs = AllTabs(self)
        self.setCentralWidget(tabs)
        self.setWindowIcon(QIcon("Icon.jpg"))
        self.setWindowTitle("Video Face Recognition")
def main():
    app = QApplication(sys.argv)
    myApp = VFRMainWindow()
    myApp.show()
    sys.exit(app.exec())

if __name__== '__main__':
    main()
