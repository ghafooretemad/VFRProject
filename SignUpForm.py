# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SignUpForm.ui'
#
# Created: Sun Aug 20 10:12:07 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DbConnection import *
from Encryptor import *
class SignUpForm(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 336)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.fname = QtWidgets.QLineEdit(Form)
        self.fname.setObjectName("fname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.fname)
        self.lname = QtWidgets.QLineEdit(Form)
        self.lname.setObjectName("lname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lname)
        self.uname = QtWidgets.QLineEdit(Form)
        self.uname.setObjectName("uname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.uname)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.password)
        self.confirm = QtWidgets.QLineEdit(Form)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setObjectName("confirm")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.confirm)
        self.forgotKey = QtWidgets.QLineEdit(Form)
        self.forgotKey.setObjectName("forgotKey")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.forgotKey)
        self.signUp = QtWidgets.QPushButton(Form)
        self.signUp.setObjectName("signUp")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.signUp)
        self.signUp.clicked.connect(self.InsertUser)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fname.setPlaceholderText(_translate("Form", "First Name"))
        self.lname.setPlaceholderText(_translate("Form", "Last Name"))
        self.uname.setPlaceholderText(_translate("Form", "Email or User name"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.confirm.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.forgotKey.setPlaceholderText(_translate("Form", "Forgot password key e.g: Afghanistan"))
        self.signUp.setText(_translate("Form", "Sign Up"))
        self.ApplyStyle()
    def InsertUser(self):
        flag = True
        self.ApplyStyle()
        fname, lname, uname = self.fname.text(),  self.lname.text(), self.uname.text().lower()
        password, conf_pass, forgotKey = self.password.text(), self.confirm.text(), self.forgotKey.text()
        if(fname.strip() == ""):
            self.fname.setStyleSheet("background-color:#FF9999")
            self.fname.setText("")
            flag = False
        if(lname.strip() == ""):
            self.lname.setStyleSheet("background-color:#FF9999")
            self.lname.setText("")
            flag = False
        if(uname.strip() == ""):
            self.uname.setStyleSheet("background-color:#FF9999")
            self.uname.setText("")
            flag = False
        if(forgotKey.strip() == ""):
            self.forgotKey.setStyleSheet("background-color:#FF9999")
            self.forgotKey.setText("")
            flag = False
        if(password == ""):
            self.password.setStyleSheet("background-color:#FF9999")
            flag = False
        if(password != conf_pass):
             self.password.setStyleSheet("background-color:#FF9999")
             self.confirm.setStyleSheet("background-color:#FF9999")
             self.password.setText("")
             self.confirm.setText("")
             flag = False
             return False
        if(flag == True):
            cypherPassword = str(AESCipher("GhafoorEtemad").encrypt(password))
            cypherForgotKey = str(AESCipher("GhafoorEtemad").encrypt(forgotKey))
            try:
                db, query = DbConnection().Connect()
                db.open()
                if db.isOpen():
                    query.exec("select * from Administrators where email = '"+uname+"'")
                    if(query.size() >0):
                        QtWidgets.QMessageBox.about(self, "Sign Up Status", "User Name is already exist!")
                        return False
                    result = query.exec('insert into Administrators(firstName, lastName, email, password, passwordKey) values("'+ fname +'", "'+ lname +'", "'+ uname +'", "'+ cypherPassword +'", "'+ cypherForgotKey +'")')
                    db.close()
                    if result == True:
                        QtWidgets.QMessageBox.warning(self, "Sign Up Status", "Successfully Inserted!, wait for Admin to Active your account")
                        self.Clean()
                        return True
                    else:
                        QtWidgets.QMessageBox.about(self, "Sign Up Status", "An error Occured please try again!" + str(db.lastError()))
                else:
                    QtWidgets.QMessageBox.about(self, "Sign Up Status", "Database Connection fialed")
                    return False
            except:
                QtWidgets.QMessageBox.critical(self, "Sign Up Status", "An error occured!,please try again")
    def ApplyStyle(self):
        self.signUp.setStyleSheet("background-color:#b1b77e")
        self.uname.setStyleSheet("background-color:#dde2aa")
        self.fname.setStyleSheet("background-color:#dde2aa")
        self.lname.setStyleSheet("background-color:#dde2aa")
        self.password.setStyleSheet("background-color:#dde2aa")
        self.confirm.setStyleSheet("background-color:#dde2aa")
        self.forgotKey.setStyleSheet("background-color:#dde2aa")
    def Clean(self):
        self.uname.setText("")
        self.fname.setText("")
        self.lname.setText("")
        self.password.setText("")
        self.confirm.setText("")
        self.forgotKey.setText("")
