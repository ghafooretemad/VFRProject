from PyQt5 import QtCore, QtGui, QtWidgets
from DbConnection import *
from Encryptor import *
from UsersList import *

class EditForm(QtWidgets.QWidget):
    def __init__(self,  ID,  userList, parent=None):
        super(EditForm,  self).__init__(parent)
        self.ID = ID
        self.usersList = userList
        self.parent = parent
        self.setupUi(self)
        self.showData()
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
        self.currentPassword = QtWidgets.QLineEdit(Form)
        self.currentPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.currentPassword.setObjectName("currentPassword")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.currentPassword)
        self.label_4.setObjectName("label_4")
        self.password = QtWidgets.QLineEdit(Form)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setObjectName("password")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.password)
        self.confirm = QtWidgets.QLineEdit(Form)
        self.confirm.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm.setObjectName("confirm")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.confirm)
        self.forgotKey = QtWidgets.QLineEdit(Form)
        self.forgotKey.setObjectName("forgotKey")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.forgotKey)
        self.signUp = QtWidgets.QPushButton(Form)
        self.signUp.setObjectName("signUp")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.signUp)
        self.signUp.clicked.connect(self.updateUser)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
    def closeApp(self):
        self.parent.close()
        self.usersList.ShowUsers()
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.fname.setPlaceholderText(_translate("Form", "First Name"))
        self.lname.setPlaceholderText(_translate("Form", "Last Name"))
        self.uname.setPlaceholderText(_translate("Form", "Email or User name"))
        self.currentPassword.setPlaceholderText(_translate("Form", "Current Password"))
        self.password.setPlaceholderText(_translate("Form", "Password"))
        self.confirm.setPlaceholderText(_translate("Form", "Confirm Password"))
        self.forgotKey.setPlaceholderText(_translate("Form", "Forgot password key e.g: Afghanistan"))
        self.signUp.setText(_translate("Form", "Update"))
    def loadData(self):
        try:
            db, query = DbConnection().Connect()
            db.open()
            query.exec("SELECT * from Administrators WHERE ID =" + self.ID)
            db.close()
            return query
        except:
            if(db.open):
                db.close()
            QtWidgets.QMessageBox.warning(self,  "Status","There is some problem with Database Connection")
            return False
    def showData(self):
        self.ApplyStyle()
        query = self.loadData()
        while(query.next()):
            self.fname.setText(query.value("firstName"))
            self.lname.setText(query.value("lastName"))
            self.uname.setText(query.value("email"))
            self.password.setText("")
            self.confirm.setText("")
            self.forgotKey.setText("")
    def updateUser(self):
        flag = True
        fname, lname, uname = self.fname.text(), self.lname.text(), self.uname.text().lower()
        password, conf_pass, forgotKey,  cPassword = self.password.text(), self.confirm.text(), self.forgotKey.text(),  self.currentPassword.text()
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
        if(cPassword.strip() == ""):
            self.currentPassword.setStyleSheet("background-color:#FF9999")
            self.currentPassword.setText("")
            flag = False
        try:
            cdb,  cquery = DbConnection().Connect()
            cdb.open()
            cquery.exec("SELECT password FROM Administrators WHERE ID =" + self.ID)
            while(cquery.next()):
                dcPassword = AESCipher("GhafoorEtemad").decrypt(eval(cquery.value("password")))
                if(dcPassword != cPassword):
                    self.currentPassword.setStyleSheet("background-color:#FF9999")
                    self.currentPassword.setText("")
                    flag = False
        except:
            QtWidgets.QMessageBox.warning(self, "Update Status", "An error occured!")

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
        if(forgotKey.strip() == ""):
            self.forgotKey.setStyleSheet("background-color:#FF9999")
            self.forgotKey.setText("")
            flag = False
        try:
            if(flag == True):
                cypherPassword = str(AESCipher("GhafoorEtemad").encrypt(password))
                cypherForgotKey = str(AESCipher("GhafoorEtemad").encrypt(forgotKey))
                db, query = DbConnection().Connect()
                db.open()
                if db.isOpen():
                    result = query.exec('UPDATE Administrators set firstName = "'+ fname +'", lastName = "'+ lname +'", email = "'+ uname +'", password = "'+ cypherPassword +'", passwordKey ="'+ cypherForgotKey +'" WHERE ID = ' + self.ID)
                    db.close()
                    if result == True:
                        QtWidgets.QMessageBox.information(self, "Update Status", "Successfully Updated!")
                        self.closeApp()
                    else:
                        QtWidgets.QMessageBox.critical(self, "Update Status", "An error Occured please try again!" + str(db.lastError()))
                else:
                    QtWidgets.QMessageBox.critical(self, "Update Status", "Database Connection fialed")
                    return False
        except:
            QtWidgets.QMessageBox.critical(self, "Update Status", "An error occured!" )
    def ApplyStyle(self):
        self.signUp.setStyleSheet("background-color:#b1b77e")
        self.uname.setStyleSheet("background-color:#dde2aa")
        self.fname.setStyleSheet("background-color:#dde2aa")
        self.lname.setStyleSheet("background-color:#dde2aa")
        self.currentPassword.setStyleSheet("background-color:#dde2aa")
        self.password.setStyleSheet("background-color:#dde2aa")
        self.confirm.setStyleSheet("background-color:#dde2aa")
        self.forgotKey.setStyleSheet("background-color:#dde2aa")
