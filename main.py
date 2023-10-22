import sys
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
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
        self.bt_users.clicked.connect(self.verifyAdmin)
        self.bt_teachers.clicked.connect(self.teacherView)
        self.bt_carreras.clicked.connect(self.carrerasViews)
        self.admin = admin
        if self.admin == "True":
           self.text.setText("Bienvenido Administrador")
        else : 
            self.text.setText("Bievenido ")
    def carrerasViews(self):
        carreras = MenuCarreras(admin=self.admin)
        widget.addWidget(carreras)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000) 
    def teacherView(self):
        teacher = MenuTeachers(admin=self.admin)
        widget.addWidget(teacher)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)   
    def verifyAdmin(self):
        if self.admin =="True":
            self.userView()
        else:
            QMessageBox.information(self,"Permiso Denegado","No tienes permisos de administrador")
            return
    def backLogin(self):
       self.hide()
       IngresoUsuario.show()
       IngresoUsuario.txt_name.clear()
       IngresoUsuario.txt_password.clear()
    def userView(self):
        Usuario = Users(admin=self.admin)
        widget.addWidget(Usuario)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(620)
        widget.setFixedWidth(700)   
class Users(QMainWindow):
    def __init__(self , admin):
        super(Users , self).__init__()
        loadUi("./ui/register.ui",self)
        self.admin = admin
        self.bt_salir_2.clicked.connect(self.backMenu)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_clear.clicked.connect(self.clearInputs)
        self.bt_register.clicked.connect(self.AddUser)
        self.bt_aggView.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_add) )
        self.bt_deleteView.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_delete) )
        self.bt_database.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page) )
        self.bt_search.clicked.connect(self.searchUser)
        self.bt_delete.clicked.connect(self.deleteUser)
        self.bt_act.clicked.connect(self.reloaddata)
    def reloaddata(self):
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT User,Admin FROM Usuarios")
            data = cursor.fetchall()
            
            

            self.tableWidget.setRowCount(len(data))  

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)

            conexion.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}")
    def searchUser(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda :
            QMessageBox.information(self,"Falta el usuario","Introduzca el usuario para proceder a la busqueda")
            return
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT User , Admin FROM Usuarios WHERE User=?", (busqueda,))
            usuario = cursor.fetchone()
            if usuario:
                self.txt_name_3.setText(usuario[0])
                if usuario[1] =="True":
                    self.rd_si_3.setChecked(True)
                if usuario[1] =="False":
                    self.rd_no_3.setChecked(True)
            else:
                QMessageBox.information(self,"Error","El usuario no existe")
                self.ln_busqueda.clear()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}")
        
    def deleteUser(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda :
            QMessageBox.information(self,"Falta el usuario","Introduzca el usuario para proceder a la busqueda")
            return
        try:
            
            reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas eliminar los registros?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
            if reply ==QMessageBox.Yes:
                conexion = sqlite3.connect("./db/database.db")
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM Usuarios WHERE User =? ",(busqueda,))
                conexion.commit()
                conexion.close()
                QMessageBox.information(self,"Eliminar","Se ha eliminado los datos correctamente")
                self.txt_name_3.clear()
                self.ln_busqueda.clear()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}")
    def AddUser(self):
        usuario = self.txt_name.text()
        password = self.txt_password.text()
        adminPermisos = None
        if self.rd_si.isChecked() :
            adminPermisos ="True"
        if self.rd_no.isChecked():
            adminPermisos = "False"
        if not  usuario or not password or not adminPermisos:
            QMessageBox.warning(self, "Error", "Por favor ingrese usuario y contraseña.")
            return
        if len(password) <=4 :
            QMessageBox.information(self,"Error","Por favor introduzca más de 4 digitos en su contraseña")
            return
        if len(usuario) <=6:
            QMessageBox.information(self,"Error","Por favor introduzca más de 6 digitos en su usuario")
            return
        
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT User FROM Usuarios WHERE User=?", (usuario,))
        existing_teacher = cursor.fetchone()
        

        if existing_teacher:
            QMessageBox.warning(self, "Advertencia", "Ya existe un usuario registrado con el mismo usuario.")
            self.txt_name.clear()
            self.txt_password.clear()
            return
        else:
            cursor.execute("INSERT INTO Usuarios (User, Password,Admin)  VALUES (?, ?, ?)", (usuario, password, adminPermisos))
            conexion.commit()
            
            QMessageBox.information(self, "Éxito", "Los datos se almacenaron correctamente")
            self.txt_name.clear()
            self.txt_password.clear()
       
       
        conexion.close()
    def clearInputs(self):
        self.txt_name.clear()
        self.txt_password.clear()
        self.rd_no.setChecked(True)
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)   
        
class MenuCarreras(QMainWindow):
    def __init__(self, admin):
        super(MenuCarreras, self).__init__()
        loadUi("./ui/carreras.ui",self)
        self.admin = admin
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_view.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_view))
        self.bt_agg.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_agg))
        self.bt_back.clicked.connect(self.backMenu)
        self.bt_agg_2.clicked.connect(self.addData)
        self.bt_act.clicked.connect(self.ViewData)
       
    def ViewData(self):
        print("click")
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Carreras")
            data = cursor.fetchall()
            self.tableWidget.setRowCount(len(data))  

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)

            conexion.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}") 
    def addData(self):
        codigo = self.txt_code.text()
        nombre = self.txt_name.text()
       
        if not codigo or not nombre :
            QMessageBox.information(self,"Añadir","Por favor introduzca los campos para agregarlos")
            return
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()

            # Comprobar si ya existe un profesor con la misma cédula
            cursor.execute("SELECT CodigoCarrera FROM Carreras WHERE CodigoCarrera=?", (codigo,))
            existing_teacher = cursor.fetchone()

            if existing_teacher:
                QMessageBox.warning(self, "Advertencia", "Ya existe una carrera con el mismo codigo.")
                self.txt_name.clear()
                self.txt_code.clear()
               
            else:
                # Si no existe, agregar el nuevo profesor a la base de datos
                cursor.execute("INSERT INTO Carreras (CodigoCarrera, Descripcion) VALUES (?, ?)", (codigo, nombre))
                
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Los datos se almacenaron correctamente")
                self.txt_name.clear()
                self.txt_code.clear()
                
    
            conexion.close()
        except:
            QMessageBox.warning(self,"Error","Error con la base de datos")
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)  
class MenuTeachers(QMainWindow):
    def __init__(self , admin):
        super(MenuTeachers , self).__init__()
        loadUi("./ui/teachers.ui",self)
        self.admin = admin
        self.bt_back.clicked.connect(self.backMenu)
        self.bt_agg.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_agg) )
        self.bt_edit.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_edit) )
        self.bt_view.clicked.connect(lambda : self.stackedWidget.setCurrentWidget(self.page_view) )
        self.bt_salir.clicked.connect(lambda :QApplication.quit())
        self.bt_agg_2.clicked.connect(self.aggTeacher)
        self.bt_search.clicked.connect(self.searchData)
        self.bt_delete.clicked.connect(self.DeleteData)
        self.bt_edit_2.clicked.connect(self.editData)
        self.bt_clear.clicked.connect(self.clearInputs)
        self.bt_act.clicked.connect(self.ViewData)
    def ViewData(self):
        print("click")
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Profesores")
            data = cursor.fetchall()
            self.tableWidget.setRowCount(len(data))  

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)

            conexion.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}")
    def clearInputs(self):
        self.txt_name_2.clear()
        self.txt_apell_2.clear()
        self.txt_cedula_2.clear()
        self.ln_busqueda.clear()
    def DeleteData(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.warning(self,"Error","Introduzca la cedula por favor")
            return
        try:
            reply = QMessageBox.question(
            self,
            'Confirmación',
            '¿Deseas eliminar los registros?',
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.Yes
        )
            if reply ==QMessageBox.Yes:
                conexion = sqlite3.connect("./db/database.db")
                cursor = conexion.cursor()
                cursor.execute("DELETE FROM Profesores WHERE Cedula =? ",(busqueda,))
                conexion.commit()
                conexion.close()
                QMessageBox.information(self,"Eliminar","Se ha eliminado los datos correctamente")
                self.txt_name_2.clear()
                self.txt_apell_2.clear()
                self.txt_cedula_2.clear()
                self.ln_busqueda.clear()
        except:
            QMessageBox.critical(self,"Error","Error con la base de datos")
    def searchData(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda :
            QMessageBox.warning(self,"Error","Ingrese la Cedula del profesor")
            return
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT Nombres, Apellidos,Cedula FROM Profesores WHERE Cedula=?" ,(busqueda,))
            resultado = cursor.fetchone()
            if resultado:
                self.txt_name_2.setText(resultado[0])
                self.txt_apell_2.setText(resultado[1])
                self.txt_cedula_2.setText(resultado[2])
            else:
                # Limpiar la tabla existente si no se encuentra ningún registro
                self.ln_busqueda.clear()
                QMessageBox.warning(self, "Advertencia", "No se ha encontrado ningún registro")
                self.txt_name_2.clear()
                self.txt_apell_2.clear()
                self.txt_cedula_2.clear()

            conexion.close()
        except:
            QMessageBox.warning(self,"Error","Error con la base de datos")
    def editData(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.warning(self,"Error","Introduzca la cedula por favor")
            return
        try:
            nombres = self.txt_name_2.text()
            apellidos = self.txt_apell_2.text()
            cedula = self.ln_busqueda.text()
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("UPDATE Profesores SET Nombres=? ,Apellidos=? WHERE Cedula=?", (nombres, apellidos, cedula))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Informacion actualizada correctamente.")
            conexion.close()
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar el profesor: {str(error)}")
            
    def aggTeacher(self):
        nombres = self.txt_name.text()
        apellido = self.txt_apell.text()
        cedula = self.txt_cedula.text()
        if not nombres or not apellido or not cedula:
            QMessageBox.information(self,"Añadir","Por favor introduzca los campos para agregarlos")
            return
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()

            # Comprobar si ya existe un profesor con la misma cédula
            cursor.execute("SELECT Cedula FROM Profesores WHERE Cedula=?", (cedula,))
            existing_teacher = cursor.fetchone()

            if existing_teacher:
                QMessageBox.warning(self, "Advertencia", "Ya existe un profesor con la misma cédula.")
                self.txt_name.clear()
                self.txt_apell.clear()
                self.txt_cedula.clear()
            else:
                # Si no existe, agregar el nuevo profesor a la base de datos
                cursor.execute("INSERT INTO Profesores (Nombres, Apellidos, Cedula) VALUES (?, ?, ?)", (nombres, apellido, cedula))
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Los datos se almacenaron correctamente")
                self.txt_name.clear()
                self.txt_apell.clear()
                self.txt_cedula.clear()
    
            conexion.close()
        except:
            QMessageBox.warning(self,"Error","Error con la base de datos")
            
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(1000)
        widget.setFixedWidth(1000)   


 
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
        