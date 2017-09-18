from PyQt5.QtWidgets import QTabWidget, QWidget, QHBoxLayout
from LoginForm import *
from SignUpForm import *
from about import *
class AllTabs(QWidget):
    def __init__(self, parent):
        super(AllTabs, self).__init__(parent)
        self.layout = QHBoxLayout()
        self.tabs = QTabWidget()

        self.InitUi()
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    def InitUi(self):
        self.HomeTab()
        self.VideoProccesingTab()
        self.AdministrationTab()
        self.AboutTab()

    def HomeTab(self):
        homeTab = QWidget()
        homeTab.layout = QHBoxLayout()
        homeTab.setLayout(homeTab.layout)
        self.tabs.addTab(homeTab, "Home")
    def VideoProccesingTab(self):
        videoProccessing = QWidget()
        videoProccessing.layout = QHBoxLayout()
        videoProccessing.setLayout(videoProccessing.layout)
        self.tabs.addTab(videoProccessing, "Video Proccessing")
    def AdministrationTab(self):
        administration = QWidget()
        administration.setStyleSheet("background-image: url(me.jpg)")
        administration.layout = QHBoxLayout()
        loginForm = LoginForm()
        signUpForm = SignUpForm()
        administration.layout.addWidget(signUpForm)
        administration.layout.addWidget(loginForm)
        administration.setLayout(administration.layout)
        self.tabs.addTab(administration, "Administration")
    def AboutTab(self):
        aboutTab = QWidget()
        aboutTab.layout = QHBoxLayout()
        about = About()
        aboutTab.layout.addWidget(about)
        aboutTab.setLayout(aboutTab.layout)
        self.tabs.addTab(aboutTab, "About Us")
