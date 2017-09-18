# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'UsersList.ui'
#
# Created: Tue Aug 22 16:19:18 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DbConnection import *
from EditLayout import EditLayout

class EmployeeList(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(EmployeeList, self).__init__(parent)
        self.setupUi(self)
        self.ShowUsers()
    def setupUi(self, Form):
        Form.setObjectName("Form")
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.employeeList = QtWidgets.QTableWidget(Form)
        self.employeeList.setLineWidth(1.5)
        self.employeeList.setObjectName("employeeList")
        self.setStyleSheet("background-image: url(background.ico); background-repeat: repeat")
        self.employeeList.setColumnCount(7)
        self.employeeList.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        self.employeeList.setHorizontalHeaderItem(6, item)
        self.horizontalLayout.addWidget(self.employeeList)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        item = self.employeeList.horizontalHeaderItem(0)
        item.setText(_translate("Form", "ID")) 
        item = self.employeeList.horizontalHeaderItem(1)
        item.setText(_translate("Form", "First Name"))
        item = self.employeeList.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Last Name"))
        item = self.employeeList.horizontalHeaderItem(3)
        item.setText(_translate("Form", "User Name"))
        item = self.employeeList.horizontalHeaderItem(4)
        item.setText(_translate("Form", "Edit"))
        item = self.employeeList.horizontalHeaderItem(5)
        item.setText(_translate("Form", "Delete"))
        item = self.employeeList.horizontalHeaderItem(6)
        item.setText(_translate("Form", "Active"))
    def ShowUsers(self):
        query = self.GetData()
        self.employeeList.setRowCount(query.size())
        row = 0
        editIcon = QtGui.QIcon("Images/edit.ico")
        deleteIcon = QtGui.QIcon("Images/delete.png")
        activeIcon = QtGui.QIcon("Images/active.ico")
        deActiveIcon = QtGui.QIcon("Images/deActive.ico")
        while query.next():
            self.employeeList.setItem(row, 0, QtWidgets.QTableWidgetItem(str(query.value("ID"))))
            self.employeeList.setItem(row, 1, QtWidgets.QTableWidgetItem(query.value("firstName")))
            self.employeeList.setItem(row, 2, QtWidgets.QTableWidgetItem(query.value("lastName")))
            self.employeeList.setItem(row, 3, QtWidgets.QTableWidgetItem(query.value("email")))
            self.editButton = QtWidgets.QPushButton("edit")
            self.editButton.setIcon(editIcon)
            self.editButton.clicked.connect(self.editData)
            self.employeeList.setCellWidget(row, 4, self.editButton)
            self.deleteButton = QtWidgets.QPushButton("delete")
            self.deleteButton.setIcon(deleteIcon)
            self.deleteButton.clicked.connect(self.deleteData)
            self.employeeList.setCellWidget(row, 5, self.deleteButton)
            if query.value("active") == 0:
                self.activeButton = QtWidgets.QPushButton("activate")
                self.activeButton.setIcon(activeIcon)
                self.activeButton.clicked.connect(self.activeUser)
                self.employeeList.setCellWidget(row, 6, self.activeButton)
            elif query.value("active") == 1:
                self.deActiveButton = QtWidgets.QPushButton("de-Active")
                self.deActiveButton.setIcon(deActiveIcon)
                self.deActiveButton.clicked.connect(self.deActiveUser)
                self.employeeList.setCellWidget(row, 6, self.deActiveButton)
            row +=1       
    def GetID(self):
        button = self.sender()
        index = self.employeeList.indexAt(button.pos())
        if index.isValid():
            try:
                row = int(index.row())
                ID= self.employeeList.item(row,0)
                return ID.text()
            except:
                QtWidgets.QMessageBox.critical(self, "Invalid ID","Invalid ID")
                return False
        else:
            QtWidgets.QMessageBox.critical("Invalid ID")
            return False
    def editData(self):
        try:
            ID = self.GetID()
            self.editForm = EditLayout( ID,  self)
            self.editForm.show()
        except:
            QtWidgets.QMessageBox.critical(self, "Update Status", "Errot occured!")
    def deleteData(self,  button):
        try:
            ID = self.GetID()
            result = QtWidgets.QMessageBox.question(self, "User deletion", "Are you sure to delete tihs user?",  QtWidgets.QMessageBox.Yes |  QtWidgets.QMessageBox.No)
            if(result == QtWidgets.QMessageBox.Yes):
                self.deleteUser(ID)
        except:
            QtWidgets.QMessageBox.critical(self, "Delete Status", "Invalid ID")
    def GetData(self):
        try:
            db, query = DbConnection().Connect()
            db.open()
            query.exec("SELECT * from Administrators ORDER BY ID DESC")
            db.close()
        except:
            if(db.open):
                db.close()
            QtWidgets.QMessageBox.critical(self,  "There is some problem with Database Connection")
        
        return query
    def deleteUser(self,  ID):
        try:
            db,  query = DbConnection().Connect()
            db.open()
            result = query.exec("DELETE FROM Administrators WHERE ID =" + ID)
            db.close()
            if(result == True):
                QtWidgets.QMessageBox.information(self,  "User Deletion",  "User Successfully deleted!")
            else:
                QtWidgets.QMessageBox.warning(self,  "User Deletion",  "Can not delete user, Pleas try again!")
        except:
            if(db.open):
                db.close()
            QtWidgets.QMessageBox.warning(self,  "User Deletion",  "Can not delete user, Pleas try again!")
    def activeUser(self):
        try:
            ID = self.GetID()
            db,  query = DbConnection().Connect()
            db.open()
            result = query.exec("UPDATE Administrators set active = 1 WHERE ID =" + ID)
            db.close()
            if(result == True):
                QtWidgets.QMessageBox.information(self,  "Activation",  "User Successfully Activated!")
            else:
                QtWidgets.QMessageBox.warning(self,  "Activation",  "Can not Activate user, Pleas try again!")
        except:
            if(db.open):
                db.close()
            QtWidgets.QMessageBox.critical(self,  "Activation",  "Error occured!, Pleas try again!")
    def deActiveUser(self):
        try:
            ID = self.GetID()
            db,  query = DbConnection().Connect()
            db.open()
            result = query.exec("UPDATE Administrators set active = 0 WHERE ID =" + ID)
            db.close()
            if(result == True):
                QtWidgets.QMessageBox.information(self,  "de-activateion",  "User Successfully de-activated!")
            else:
                QtWidgets.QMessageBox.warning(self,  "de-activateion",  "Can not de-active user, Pleas try again!")
        except:
            if(db.open):
                db.close()
            QtWidgets.QMessageBox.critical(self,  "de-activateion",  "error occured!, Pleas try again!")
