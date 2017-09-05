from PyQt5.QtSql import *
from PyQt5 import QtWidgets
try:
    db = QSqlDatabase.addDatabase("QMYSQL")
    db.setDatabaseName("vfr_db")
    db.setUserName("root")
    db.setPassword("halimetemad")
except:
    QtWidgets.QMessageB0x.warning(QtWidgets.QWidget,  "Database Connection",  "Database Connection Field!")
class DbConnection():
    def Connect(self):
        return db, QSqlQuery()
