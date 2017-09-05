# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forgotPass\.ui'
#
# Created: Mon Sep  4 11:26:23 2017
#      by: PyQt5 UI code generator 5.3.2`                                                                                       
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DbConnection import *
from Encryptor import *
class ResetForm(QtWidgets.QWidget):
    def __init__(self,  parent = None):
        super(ResetForm,  self).__init__(parent)
        self.parent = parent
        self.setupUi(self)
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(426, 235)
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.uname = QtWidgets.QLineEdit(Form)
        self.uname.setObjectName("uname")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.uname)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.forgotKey = QtWidgets.QLineEdit(Form)
        self.forgotKey.setObjectName("forgotKey")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.forgotKey)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.npassword = QtWidgets.QLineEdit(Form)
        self.npassword.setObjectName("npassword")
        self.npassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.npassword)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.cpassword = QtWidgets.QLineEdit(Form)
        self.cpassword.setObjectName("cpassword")
        self.cpassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.cpassword)
        self.change = QtWidgets.QPushButton(Form)
        self.change.setObjectName("change")
        self.change.clicked.connect(self.reset)
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.change)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def reset(self):
        flag = True
        self.ApplyStyle()
        uname = self.uname.text().lower()
        npassword, conf_pass, forgotKey = self.npassword.text(), self.cpassword.text(), self.forgotKey.text()
        if(uname.strip() == ""):
            self.uname.setStyleSheet("background-color:#FF9999")
            self.uname.setText("")
            flag = False
        if(forgotKey.strip() == ""):
            self.forgotKey.setStyleSheet("background-color:#FF9999")
            self.forgotKey.setText("")
            flag = False
        if(npassword == ""):
            self.npassword.setStyleSheet("background-color:#FF9999")
            flag = False
        if(npassword != conf_pass):
             self.npassword.setStyleSheet("background-color:#FF9999")
             self.cpassword.setStyleSheet("background-color:#FF9999")
             self.npassword.setText("")
             self.cpassword.setText("")
             flag = False
             return False
        if(flag == True):
            try:
                db,  query = DbConnection().Connect()
                db.open()
                query.exec('select * from Administrators where email = "'+ uname +'" and active =' + str(True))
                db.close()
                if(query.size()>0):
                    while(query.next()):
                        decryptedForgotKey= AESCipher("GhafoorEtemad").decrypt(eval(query.value("passwordKey")))
                        if forgotKey == decryptedForgotKey :
                            encPassword =  str(AESCipher("GhafoorEtemad").encrypt(npassword))
                            db.open()
                            result = query.exec('UPDATE Administrators SET password = "'+ encPassword+'"  WHERE email = "'+ uname +'"')
                            db.close()
                            if(result == True):
                                QtWidgets.QMessageBox.information(self,  "Reset Status",  "Your Password Successfully Changed!")
                                self.parent.close()
                            else:
                                QtWidgets.QMessageBox.warning(self,  "Reset Status",  "Can not reset password, please try again!")
                        else:
                            self.incorrectLogin()
                else:
                    self.incorrectLogin()
            except:
                QtWidgets.QMessageBox.critical(self,  "Reset Status",  "Data Insertion Field")
    def incorrectLogin(self):
        QtWidgets.QMessageBox.warning(self,  "Reset Status",  "there is no such account with this forgot key")
        return False
    def ApplyStyle(self):
        self.uname.setStyleSheet("background-color:#dde2aa")
        self.npassword.setStyleSheet("background-color:#dde2aa")
        self.cpassword.setStyleSheet("background-color:#dde2aa")
        self.forgotKey.setStyleSheet("background-color:#dde2aa")
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label.setText(_translate("Form", "User Name :"))
        self.label_2.setText(_translate("Form", "Forgot Key: "))
        self.label_3.setText(_translate("Form", "New Password:"))
        self.label_4.setText(_translate("Form", "Confirm:"))
        self.change.setText(_translate("Form", "Change"))
