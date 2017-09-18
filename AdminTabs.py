from PyQt5.QtWidgets import QTabWidget, QWidget, QHBoxLayout
from UsersList import *
from EmployeeRegistration import *
class AdminTabs(QWidget):
    def __init__(self, parent):
        super(AdminTabs, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.tabs = QTabWidget()

        self.InitUi()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    def InitUi(self):
        self.UserTab()
        self.EmployeeTab()

    def UserTab(self):
        userTab = QWidget()
        userTab.layout = QHBoxLayout()
        userList = UsersList(self)
        userTab.layout.addWidget(userList)
        userTab.setLayout(userTab.layout)
        self.tabs.addTab(userTab, "Users")
    def EmployeeTab(self):
        employeeTab = QWidget()
        employeeTab.layout = QHBoxLayout()
        employeeRegistration = EmployeeRegistration(self)
        employeeTab.layout.addWidget(employeeRegistration)
        employeeTab.setLayout(employeeTab.layout)
        self.tabs.addTab(employeeTab, "Employee")
   
