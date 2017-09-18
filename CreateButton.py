from PyQt5.QtWidgets import QPushButton
from PyQt5 import QtGui
class CreateButton:
       
    def getButton(self,   title,  iconPath):
        button = QPushButton(title)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(iconPath), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        button.setIcon(icon)
        return button
