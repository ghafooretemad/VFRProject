# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeRegistration.ui'
#
# Created: Mon Sep  4 06:41:23 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from DbConnection import *
from StartCamera import *

class EmployeeRegistration(QtWidgets.QWidget):
    def __init__(self,  parent = None):
        super(EmployeeRegistration,  self).__init__(parent)
        self.setupUi(self)
    def setupUi(self, Form):
        self.formLayout = QtWidgets.QFormLayout(Form)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setObjectName("formLayout")
        self.label0 = QtWidgets.QLabel(Form)
        self.label0.setObjectName("label0")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label0)
        self.empID = QtWidgets.QLineEdit(Form)
        self.empID.setObjectName("empID")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.empID)
        
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.fname = QtWidgets.QLineEdit(Form)
        self.fname.setObjectName("fname")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.fname)
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.lname = QtWidgets.QLineEdit(Form)
        self.lname.setObjectName("lname")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lname)
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.possition = QtWidgets.QLineEdit(Form)
        self.possition.setObjectName("possition")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.possition)
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.photoButton = QtWidgets.QPushButton(Form)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../../Icons/camera-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.photoButton.setIcon(icon)
        self.photoButton.setObjectName("photoButton")
        self.photoButton.clicked.connect(self.dataSaver)
        self.formLayout.setWidget(12, QtWidgets.QFormLayout.FieldRole, self.photoButton)
        self.saveButton = QtWidgets.QPushButton(Form)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../../Icons/Save-icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.saveButton.setIcon(icon1)
        self.saveButton.setObjectName("saveButton")
        self.saveButton.setEnabled(False)
        self.formLayout.setWidget(14, QtWidgets.QFormLayout.FieldRole, self.saveButton)
        self.normal = QtWidgets.QCheckBox(Form)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../../Icons/face.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.normal.setIcon(icon2)
        self.normal.setObjectName("normal")
        self.formLayout.setWidget(8, QtWidgets.QFormLayout.FieldRole, self.normal)
        self.excited = QtWidgets.QCheckBox(Form)
        self.excited.setIcon(icon2)
        self.excited.setObjectName("excited")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.FieldRole, self.excited)
        self.glasses = QtWidgets.QCheckBox(Form)
        self.glasses.setIcon(icon2)
        self.glasses.setObjectName("glasses")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.glasses)
        self.laugh = QtWidgets.QCheckBox(Form)
        self.laugh.setIcon(icon2)
        self.laugh.setObjectName("laugh")
        self.formLayout.setWidget(11, QtWidgets.QFormLayout.FieldRole, self.laugh)
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(9, QtWidgets.QFormLayout.LabelRole, self.label_5)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        self.label0.setText(_translate("Form", "Emp ID: "))
        self.label.setText(_translate("Form", "Frist Name: "))
        self.label_2.setText(_translate("Form", "Last Name: "))
        self.label_3.setText(_translate("Form", "Possition: "))
        self.label_4.setText(_translate("Form", "Take Photo: "))
        self.photoButton.setText(_translate("Form", "Take"))
        self.saveButton.setText(_translate("Form", "Save"))
        self.normal.setText(_translate("Form", "Normal"))
        self.excited.setText(_translate("Form", "Excited"))
        self.glasses.setText(_translate("Form", "Glasses"))
        self.laugh.setText(_translate("Form", "Laugh"))
        self.label_5.setText(_translate("Form", "Face Mode:"))
    def dataSaver(self):
        flag = True
        self.ApplyStyle()

        self.fnameData = self.fname.text().strip()
        self.lnameData = self.lname.text().strip()
        self.possitionData = self.possition.text().strip()
        self.empIDData = self.empID.text().strip()
        if(self.fnameData == "" or self.lnameData == "" or self.possitionData== "" or self.empIDData == ""):
            if(self.empIDData == ""):
                self.empID.setStyleSheet("background-color:#FF9999")
                self.empID.setText("")
            if(self.fnameData == ""):
                self.fname.setStyleSheet("background-color:#FF9999")
                self.fname.setText("")
            if(self.lnameData == ""):
                self.lname.setStyleSheet("background-color:#FF9999")
                self.lname.setText("")
            else:
                self.possition.setStyleSheet("background-color:#FF9999")
                self.possition.setText("")
            flag = False
        else:
            try:
                db,  query = DbConnection().Connect()
                db.open()
                query.exec("select * from Employee where employeeID = '" + self.empIDData  + "'")
                if(query.size() > 0):
                    db.close()
                    QtWidgets.QMessageBox.warning(self,  "Employee Insertion",  "Employee is already exist with this ID")
                    return False
                else:
                    result = query.exec("INSERT INTO Employee (employeeID, firstName, lastName, possition) values('"+ self.empIDData +"', '"+ self.fnameData +"','"+ self.lnameData +"','"+ self.possitionData +"')")
                    db.close()
                    if(result == False):
                        QtWidgets.QMessageBox.warning(self,  "Employee Insertion",  "Employee Registration Field")
                        return False
            except:
                QtWidgets.QMessageBox.critical(self,  "Employee Insertion",  "Database connection field")
        selectedMode = {} 
        if (self.normal.isChecked()):
            selectedMode['normal'] = True
        if(self.excited.isChecked()):
            selectedMode['excited'] = True
        if(self.glasses.isChecked()):
            selectedMode['glasses'] = True
        if(self.laugh.isChecked()):
            selectedMode['laugh'] = True
        if(len(selectedMode) <= 0):
            flag = False
        if(flag == True):
            StartCamera(selectedMode,  self.empIDData)
    def ApplyStyle(self):
        self.empID.setStyleSheet("background-color:white")
        self.fname.setStyleSheet("background-color:white")
        self.lname.setStyleSheet("background-color:white")
        self.possition.setStyleSheet("background-color:white")
