import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
import hashlib
import os
from PyQt5.QtCore import Qt
import sqlite3

class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario, self).__init__()
        loadUi("./ui/login.ui",self)
        self.Loginboton.clicked.connect(self.ingreso)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        
    def menuPrincipal_access(self,admin):
        menuview = MenuPrincipal(admin)
        widget.addWidget(menuview)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)   
    def ingreso(self):
        usuario = self.txt_name.text()
        password = self.txt_password.text()
        if not  usuario or not password:
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            return
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM Usuarios WHERE User = ?", (usuario,))
        usuario = cursor.fetchone()
        if usuario :
            passwordDb = usuario[1]
            if password == passwordDb:
                print("contraseña correcta")
                admin = usuario[2]
                self.menuPrincipal_access(admin=admin)
                    
            else:
                QMessageBox.warning(self,"Error","Contraseña erronea")
        else:
            QMessageBox.information(self,"Error","Usuario no encontrado en la base de datos")
        conexion.close()


class MenuPrincipal(QMainWindow):
    def __init__(self , admin):
        super(MenuPrincipal, self).__init__()
        loadUi("./ui/menu.ui",self)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_close.clicked.connect(self.backLogin)
        self.admin = admin
        if self.admin == "True":
           self.text.setText("Bienvenido Administrador")
        else : 
            self.text.setText("Bievenido ")
    def backLogin(self):
       self.hide()
       IngresoUsuario.show()
       IngresoUsuario.txt_name.clear()
       IngresoUsuario.txt_password.clear()
        

app = QApplication(sys.argv)
IngresoUsuario = IngresoUsuario()
widget = QtWidgets.QStackedWidget()
widget.addWidget(IngresoUsuario)
widget.move(400, 80)
widget.setFixedHeight(580)
widget.setFixedWidth(750)
widget.setWindowFlag(QtCore.Qt.FramelessWindowHint)
widget.setAttribute(QtCore.Qt.WA_TranslucentBackground)
widget.show()



try:
    sys.exit(app.exec_())
except:
    print("saliendo")
        