# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginForm.ui'
#
# Created: Sun Aug 20 09:56:58 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!
from AdministrationWindow import AdministrationWindow
from PyQt5 import QtCore, QtWidgets
from DbConnection import *
from Encryptor import *
from ResetLayout import *
class LoginForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 206)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.userName = QtWidgets.QLineEdit(Form)
        self.userName.setObjectName("userName")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.userName)
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setObjectName("password")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.password)
        self.loginButton = QtWidgets.QPushButton(Form)
        self.loginButton.setObjectName("loginButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.loginButton)
        self.forgotPassword = QtWidgets.QPushButton(Form)
        self.forgotPassword.setObjectName("forgotPassword")
        self.forgotPassword.setStyleSheet("border:0px")
        self.forgotPassword.clicked.connect(self.ResetPassword)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.forgotPassword)
        self.setStyleSheet("""QtWidgets.QFormLayout#formLayout{border: 2px solid black;\n" "border-radius: 2px;\n" "background-color: rgb(255,234,255)}""")
        self.loginButton.clicked.connect(self.login)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def ResetPassword(self):
        resetLayout = ResetLayout(self)
        resetLayout.show()
    def login(self):
        uname = self.userName.text().lower()
        password = self.password.text()
        try:
            db, query = DbConnection().Connect()
            db.open()
            query.exec('select * from Administrators where email = "'+ uname +'" and active =' + str(True))
            if(query.size()>0):
                while(query.next()):
                    decryptedPassword = AESCipher("GhafoorEtemad").decrypt(eval(query.value("password")))
                    if password == decryptedPassword :
                        self.admin = AdministrationWindow(self)
                        self.admin.show()
                        self.clear()
                    else:
                       self.incorrectLogin()
            else:
                self.incorrectLogin()
            db.close()
        except:
         QtWidgets.QMessageBox.critical(self, "Login Status", "Database connection field!")

    def clear(self):
        self.userName.setText("")
        self.password.setText("")
    def incorrectLogin(self):
         QtWidgets.QMessageBox.warning(self, "Login Status", "your user name or password is incorrecr!")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.userName.setPlaceholderText(_translate("Form", "e.g: etemad@example.com"))
        self.password.setPlaceholderText(_translate("Form", "password"))
        self.loginButton.setText(_translate("Form", "Login"))
        self.forgotPassword.setText(_translate("Form", "Forgot password?"))
        self.userName.setStyleSheet("background-color:#cbd18e")
        self.password.setStyleSheet("background-color:#cbd18e")
        self.loginButton.setStyleSheet("background-color:#b4ba77")
