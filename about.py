# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'about.ui'
#
# Created: Wed Sep  6 04:09:13 2017
#      by: PyQt5 UI code generator 5.3.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class About(QtWidgets.QWidget):
    def __init__(self,  parent=None):
        super(About,  self).__init__(parent)
        self.setupUi(self)
    def getData(self):
        self.app_title = "Video face Recognition"
        self.app_description = "this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test "
        self.app_image = "camera-icon.png"
        self.developer_title = "Developer"
        self.developer_details =  "this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for test this is a text for "
        self.developer_image = "camera-icon.png"
    def setupUi(self, Form):
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.aboutTextView = QtWidgets.QTextBrowser(Form)
        self.aboutTextView.setObjectName("aboutTextView")
        self.verticalLayout.addWidget(self.aboutTextView)

        self.retranslateUi(Form)
    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.getData()
        self.aboutTextView.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Roboto\'; font-size:14pt; font-weight:200; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">"+self.app_title+"</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">"+self.app_description+"</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Images/about/"+self.app_image+"\" width=\"250\" height = \"200\"/></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600; font-style:italic; text-decoration: underline;\">"+self.developer_title+"</span><span style=\" font-size:16pt; font-weight:400;\">:</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">"+self.developer_details+"</span></p>\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"Images/about/"+self.developer_image+"\" width=\"250\"/ /></p></body></html>"))

