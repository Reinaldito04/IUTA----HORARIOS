
#Test
import sys
import typing
from PyQt5 import QtCore,QtGui,QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDate , QBuffer, QByteArray , QTime
from PyQt5.QtGui import QImage,QPixmap 
from PyQt5.QtWidgets import QSizePolicy,QHeaderView
from PyQt5.QtCore import QIODevice
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
import os
from PyQt5.QtWidgets import QDialog, QApplication, QPushButton, QVBoxLayout, QLabel, QLineEdit, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QCheckBox, QDialog, QLabel, QLineEdit
import sqlite3
import fitz





class FormularioDialog(QDialog):
    def __init__(self , titulo , hora, dia ,fila,columna ,horario,carrera,sesion):
        super().__init__()
        loadUi("./ui/busqueda.ui",self)
        self.titulo = titulo
        self.hora = next(iter(hora)) if isinstance(hora, set) else hora  # Obtiene el primer elemento del conjunto
        self.dia = next(iter(dia)) if isinstance(dia, set) else dia  # Obtiene el primer elemento del conjunto
        self.fila = fila
        self.columna = columna
        self.horario = horario
        self.carrera = carrera
        self.sesion = sesion
        
        
        
        if self.dia == 1:
            self.dia = "Lunes"
        if self.dia == 2:
            self.dia = "Martes"
        if self.dia == 3:
            self.dia = "Miercoles"
        if self.dia == 4:
            self.dia = "Jueves"
        if self.dia == 5:
            self.dia = "Viernes"
        if self.dia == 6:
            self.dia = "Sabado"
        self.initUI()

    def cancelar(self):
        celda = self.horario.tableWidget.item(self.fila, self.columna)
        if celda:
            celda.setText("")  # O puedes establecer el texto como desees
        self.hide()

    
    def initUI(self,):
       
        self.bt_codigoMat.clicked.connect(self.codigoMateria)
        self.bt_codigoSalon.clicked.connect(self.codigoSalon)
        self.bt_CedulaProf.clicked.connect(self.codigoProfesor)
        
        self.input_dia.setText(str(self.dia))
        self.input_dia.setReadOnly(True)
        self.rejected.connect(self.cancelar)

      
        self.input_hora.setText(str(self.hora))
        self.input_hora.setReadOnly(True)
        self.input_materia.setReadOnly(True)
        self.input_salon.setReadOnly(True)
        self.input_profesor.setReadOnly(True)
        self.boton_guardar.clicked.connect(self.guardar)
        self.boton_cancelar.clicked.connect(self.cancelar)
        

       
        self.setWindowTitle(self.titulo)

    def codigoMateria(self):
        consulta_like = "SELECT Codigo, Nombre FROM Materia WHERE Codigo LIKE ?"
        consulta_sql_materia = "SELECT Codigo, Nombre FROM Materia;"
        dialogo = DialogoConsulta("Consulta de Materia", "Seleccione una materia:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.input_materia.setText(codigo_materia) 
            
    def codigoSalon(self):
        consulta_like = "SELECT Descripcion, CodigoAula FROM Aulas WHERE Descripcion LIKE ?"
        
        consulta_sql_salon = "SELECT  Descripcion,CodigoAula FROM Aulas;"

        dialogo = DialogoConsulta("Consulta de Salon", "Seleccione un salon:", consulta_sql_salon,consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigoSalon = dialogo.item_seleccionado()
            self.input_salon.setText(codigoSalon)
            
    def codigoProfesor(self):
        consulta_like = "SELECT Nombres || ' ' || Apellidos AS Nombre_Y_Apellido, Cedula FROM Profesores WHERE Nombre_Y_Apellido LIKE ?"
        
        consulta_sql_profesor = "SELECT Nombres || ' ' || Apellidos AS Nombre_Y_Apellido ,Cedula FROM Profesores;"

        dialogo = DialogoConsulta("Consulta de Profesor", "Seleccione el nombre y apellido del profesor:" ,consulta_sql_profesor,consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo = dialogo.item_seleccionado()
            self.input_profesor.setText(codigo)

    def guardar(self):
        codigoMateria = self.input_materia.text()
        codigoSalon = self.input_salon.text()
        cedulaProfesor = self.input_profesor.text()

        if not (codigoMateria and codigoSalon and cedulaProfesor):
            QMessageBox.information(self, "Error", "Todos los campos son obligatorios")
            return None  # Devuelve None si hay campos faltantes

        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()

        verificarHorario = cursor.execute("SELECT * FROM HorarioTest WHERE Dia=? AND Hora=? AND CodigoAula=?",
                                          (self.dia, self.hora, codigoSalon))

        if verificarHorario.fetchone():
            QMessageBox.warning(self, "Error", "El salón ya está siendo utilizado en la misma hora")
            self.input_salon.clear()
            self.input_salon.setPlaceholderText("Ingrese un salón distinto...")
            return None  # Devuelve None si el salón ya está siendo utilizado

        else:
            cursor.execute("INSERT INTO HorarioTest (Dia,Hora,CodigoMat,CodigoAula,CedulaProf,Carrera,Sesion) VALUES (?,?,?,?,?,?,?)",
                           (self.dia,self.hora,codigoMateria,codigoSalon,cedulaProfesor,self.carrera,self.sesion))
            QMessageBox.information(self,"Exito","Se ha almacenado los datos correctamente")
            conexion.commit()
            conexion.close()
           

            print(f"El código de materia es {codigoMateria}, salón {codigoSalon}, cédula profesor {cedulaProfesor}")
            text_for_checkbox = (f"{codigoMateria}\n{codigoSalon}\n{cedulaProfesor}")
            self.establecer_texto_en_celda(text_for_checkbox)
            self.hide()
            return  codigoMateria,codigoSalon,cedulaProfesor

    def establecer_texto_en_celda(self, texto):
        # Obtener la instancia de QTableWidget desde la instancia de Horario
        table_widget = self.horario.tableWidget

        # Establecer el texto en la celda específica
        table_widget.setItem(self.fila, self.columna, QTableWidgetItem(texto))
        
class QuestionHorario(QDialog):
    def __init__(self,horario_instance,datos_carga_horas,dias):
        super(QuestionHorario,self).__init__()
        loadUi("ui/eliminarhorarioquestion.ui",self)
        self.setWindowTitle("Ya existe un horario")
        self.bt_eliminar.clicked.connect(self.eliminar)
        self.bt_view.clicked.connect(self.ver)
        self.horario_instance = horario_instance
        self.dias = dias
        print (self.dias)
        self.datos_carga_horas = datos_carga_horas
       
    def eliminar(self):
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute(
            "DELETE FROM HorarioTest WHERE Carrera=? AND Sesion=?",
            (self.horario_instance.ln_carrera.text(), self.horario_instance.ln_sesion.text())
        )
        QMessageBox.information(self,"Eliminar","se ha eliminado correctamente")
        conexion.commit()
        conexion.close()
        
        self.accept()

    def ver(self):
        QMessageBox.information(self, "Ver", "Se ha añadido a la tabla actual")
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Dia, Hora, CodigoMat, CodigoAula, CedulaProf FROM HorarioTest WHERE Carrera=? AND Sesion=?",
            (self.horario_instance.ln_carrera.text(), self.horario_instance.ln_sesion.text())
        )
        datos = cursor.fetchall()
        self.horario_instance.tableWidget.clearContents()

        # Recorrer datos_Carga_horas para agregar las horas en la primera columna
        for i, hora in enumerate(self.datos_carga_horas):
            item_hora = QTableWidgetItem(hora)
            item_hora.setFlags(item_hora.flags() & ~Qt.ItemIsEditable)  # Deshabilitar edición
            self.horario_instance.tableWidget.setItem(i, 0, item_hora)

        for result in datos:
            dia = result[0]
            hora = result[1]
            codigo_mat = result[2]
            codigo_aula = result[3]
            cedula_prof = result[4]

            # Buscar la hora en datos_carga_horas
            if hora in self.datos_carga_horas:
                # Obtener la fila correspondiente a la hora en datos_carga_horas
                fila = self.datos_carga_horas.index(hora)

                # Asignar el día a la columna correspondiente
                if dia == "Lunes":
                    columna = 1
                elif dia == "Martes":
                    columna = 2
                elif dia == "Miercoles":
                    columna = 3
                elif dia == "Jueves":
                    columna = 4
                elif dia == "Viernes":
                    columna = 5
                elif dia == "Sabado":
                    columna = 6
                else:
                    # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                    continue

                # Colocar los datos en la tabla
                item = QTableWidgetItem(f"{codigo_mat}\n{codigo_aula}\n{cedula_prof}")

                # Deshabilitar la edición de la primera columna (hora)
                if columna == 1:
                    item.setFlags(item.flags() & ~Qt.ItemIsEditable)  # Quitar la bandera de edición

                self.horario_instance.tableWidget.setItem(fila, columna, item)

        self.accept()

   
class PreviewPDF(QDialog):
    def __init__(self,pdf_path):
        super(PreviewPDF,self).__init__()
        loadUi("ui/preview.ui",self)
        self.pdf_path = pdf_path
        self.current_page = 0  # Página actual
        self.total_pages = 0  
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Vista Previa de PDF')
        self.btn_anterior.clicked.connect(self.showPreviousPage)
        self.btn_siguiente.clicked.connect(self.showNextPage)
        self.showPdfPreview()
        self.total_pages = self.getTotalPages(self.pdf_path)
        
    def showPdfPreview(self):
            # Cargar la imagen del PDF como vista previa en el QLabel
        pixmap = self.convertPdfPageToPixmap(self.pdf_path, self.current_page)

        # Mostrar la imagen en el QLabel
        self.foto.setPixmap(pixmap)
        self.foto.show()
    def showPreviousPage(self):
        # Mostrar la página anterior si no estamos en la primera página
        if self.current_page > 0:
            self.current_page -= 1
            self.showPdfPreview()
                
    def showNextPage(self):
        # Mostrar la página siguiente si no estamos en la última página
        if self.current_page < self.total_pages - 1:
            self.current_page += 1
            self.showPdfPreview()
    def getTotalPages(self, pdf_path):
        # Obtener el total de páginas en el PDF
        doc = fitz.open(pdf_path)
        total_pages = doc.page_count
        doc.close()
        return total_pages       
    def convertPdfPageToPixmap(self, pdf_path, page_number):
            # Utilizar PyMuPDF para convertir la página específica del PDF a una imagen
        doc = fitz.open(pdf_path)
        page = doc[page_number]
        pixmap = page.get_pixmap()

            # Convertir la imagen a un formato utilizable por QPixmap
        img = QImage(pixmap.samples, pixmap.width, pixmap.height, pixmap.stride, QImage.Format_RGB888)
        img = img.rgbSwapped()

            # Crear un QPixmap a partir de la imagen
        pixmap = QPixmap.fromImage(img)

        doc.close()

        return pixmap
    



# Clase del login
class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario, self).__init__()
        loadUi("./ui/login.ui",self)
        self.Loginboton.clicked.connect(self.ingreso)
        #self.bt_salir.clicked.connect(lambda : QApplication.quit())
        
    def menuPrincipal_access(self,admin):
        menuview = MenuPrincipal(admin)
        widget.addWidget(menuview)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.hide()
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

# Clase Menu Principal

class MenuPrincipal(QMainWindow):
    def __init__(self , admin):
        super(MenuPrincipal, self).__init__()
        loadUi("./ui/menu.ui",self)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_close.clicked.connect(self.backLogin)
        self.bt_users.clicked.connect(self.verifyAdmin)
        self.bt_teachers.clicked.connect(self.teacherView)
        self.bt_materias.clicked.connect(self.materiasView)
        self.setWindowTitle("MenuPrincipal")
        self.showMaximized()
        self.bt_carreras.clicked.connect(self.carrerasViews)
        self.admin = admin
        self.bt_horarios.clicked.connect(self.menuprincipalHorariosView)
        self.bt_sede.clicked.connect(self.menuSedes)
        if self.admin == "True":
            self.text.setText("Bienvenido Administrador")
        else:
            self.text.setText(f"Bienvenido, {self.user_name}")
    
    
    #def horariosView(self):
        #horarios = HorarioMenu(admin=self.admin)
        #widget.addWidget(horarios)
        #widget.setCurrentIndex(widget.currentIndex()+1)
    
    # desplegar ventana de gestionar carreras   
    def menuSedes(self):
        sedes = SedesMenu(admin=self.admin)
        widget.addWidget(sedes)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def carrerasViews(self):
        carreras = MenuCarreras(admin=self.admin)
        widget.addWidget(carreras)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # desplegar ventana de gestionar materias 
    def materiasView(self):
        materias = MenuMaterias(admin=self.admin)
        widget.addWidget(materias)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    # desplegar ventana de gestionar profesores 
    def teacherView(self):
        teacher = MenuTeachers(admin=self.admin)
        widget.addWidget(teacher)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    # Verificar permisos de administrador    
    def verifyAdmin(self):
        if self.admin =="True":
            self.userView()
        else:
            QMessageBox.information(self,"Permiso Denegado","No tienes permisos de administrador")
            return
        
    # Cerrar Sesion
    def backLogin(self):
        widget.addWidget(ingreso_usuario)
        widget.setCurrentIndex(widget.currentIndex()+1)
        ingreso_usuario.txt_name.clear()
        ingreso_usuario.txt_password.clear()
        self.hide()
    
    # Desplegar ventana de configuracion de ususarios(solo permisos admin)    
    def userView(self):
        Usuario = Users(admin=self.admin)
        widget.addWidget(Usuario)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
    # desplegar menu principal de horarios
    def menuprincipalHorariosView(self):
        modalidadDialogo = modalidadQuestion(admin=self.admin)
        modalidadDialogo.exec_()

class modalidadQuestion(QDialog):
    def __init__(self,admin):
        super(modalidadQuestion,self).__init__()
        loadUi("./ui/modalidadBusqueda.ui",self)
        self.bt_crear.clicked.connect(self.abrir_modalidad_registro)
        self.admin = admin
        self.cargarDatos()
        self.bt_busqueda.clicked.connect(self.busquedaRealizar)
    def cargarDatos(self):
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT modalidad FROM Modalidad")
          # Obtener los resultados
        modalidades = cursor.fetchall()

            # Cerrar la conexión a la base de datos
        conexion.close()

            # Insertar las modalidades en el ComboBox
        for modalidad in modalidades:
            self.combo_box.addItem(modalidad[0])
    def abrir_modalidad_registro(self):
        self.close()
        modalidad = modalidadRegistro(admin=self.admin)
        widget.addWidget(modalidad)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    def busquedaRealizar(self):
        
        valor_seleccionado = self.combo_box.currentText()
        print("Valor seleccionado:", valor_seleccionado)
        self.close()
        plantilla = menuHorarioPlantilla(admin=self.admin,modalidad=valor_seleccionado)
        widget.addWidget(plantilla)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class modalidadRegistro(QMainWindow):
    def __init__(self,admin):
        super(modalidadRegistro,self).__init__()
        loadUi("./ui/modalidad.ui",self)
        self.admin = admin
        self.bt_register.clicked.connect(self.addModalidad)
        self.bt_aggHora.setEnabled(False)
        self.bt_aggDias.setEnabled(False)
        self.bt_aggHora.clicked.connect(self.agregarHora)
        self.bt_aggDias.clicked.connect(self.aggDias)
        self.bt_deleteView.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_delete) )
        self.bt_database.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page) )
        self.bt_aggView.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_add) )
        self.cargardatosPrincipal()
        self.bt_search.clicked.connect(self.busquedaParaEliminar)
        self.bt_delete.clicked.connect(self.eliminarDatos)
        
    def busquedaParaEliminar(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.warning(self,"Advertencia","Es necesario el codigo")
            return
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT modalidad,descripcion FROM Modalidad WHERE codigo=?",(busqueda,))
        datos = cursor.fetchone()
        self.txt_name_3.setText(datos[0])
        self.txt_name_4.setText(datos[1])
        
    def eliminarDatos(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.warning(self,"Advertencia","Es necesario el codigo")
            return
        
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Modalidad WHERE codigo=?",(busqueda,))
        cursor.execute("DELETE FROM Modulo WHERE CodigoModulo=?",(busqueda,))
        conexion.commit()
        QMessageBox.information(self,"Exito","Se elimino correctamente")
        self.txt_name_3.clear()
        self.txt_name_4.clear()
        self.ln_busqueda.clear()
    def cargardatosPrincipal(self):
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT codigo,modalidad,descripcion FROM Modalidad")
        datos = cursor.fetchall()
        self.tableWidget.setRowCount(len(datos))  

        for row, row_data in enumerate(datos):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.tableWidget.setItem(row, col, item)
        conexion.close()
        
    def addModalidad(self):
        codigo =self.txt_Codigo.text()
        turno =self.txt_turno.text()
        descripcion = self.txt_descripcion.text()
        if  not (codigo or not turno or not descripcion):
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")
            return
        else:
            conexion =sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT COUNT(*) FROM Modalidad WHERE codigo=? ",(codigo,))
            existe = cursor.fetchone()[0]
            if existe:
                QMessageBox.warning(self,"Error","El código ya Existe")
                return
            cursor.execute("INSERT INTO Modalidad (modalidad,codigo,descripcion) VALUES (?,?,?)",(turno,codigo,descripcion))
            conexion.commit()
            QMessageBox.information(self,"Exito","Los datos han sido almacenados correctamente")
            self.bt_aggHora.setEnabled(True)
            self.bt_aggDias.setEnabled(True)

            conexion.close()
            
    def agregarHora(self):
        codigo =self.txt_Codigo.text()
        turno =self.txt_turno.text()
     
        if not (codigo and turno):
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")
            return
        else:
      # Obtener la hora del QDateTimeEdit
            horaInicio = self.dateTimeEdit.dateTime().toString("h:mm AP").replace(".", "").upper()
            HoraFinalizacion = self.dateTimeEdit_2.dateTime().toString("h:mm AP").replace(".", "").upper()
            # Combinar las dos horas con la unión de "A"
            horas_combinadas = f"{horaInicio} A {HoraFinalizacion}"
            print (horas_combinadas)
            conexion =sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Modulo (CodigoModulo,Turno,Descripcion) VALUES (?,?,?) ",(codigo,turno,horas_combinadas))
            conexion.commit()
            self.cargarTablaHoras()
    def aggDias(self):
        codigo=self.txt_Codigo.text()
        turno =self.txt_turno.text()
        
        if not (codigo and turno):
            QMessageBox.warning(self,"Error","Todos los campos son obligatorios")
            return
        else:
            
            dia= self.comboBox.currentText()
            
            conexion =sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("INSERT INTO Dias (Dia,modalidad,Codigo) VALUES (?,?,?) ",(dia,turno,codigo))
            conexion.commit()
            self.cargarTablaDias()
            
    def cargarTablaHoras(self):
        turno =self.txt_turno.text()
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT Descripcion FROM Modulo WHERE Turno=?",(turno,))
        datos = cursor.fetchall()
        self.tablaHoras.setRowCount(len(datos))  

        for row, row_data in enumerate(datos):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.tablaHoras.setItem(row, col, item)
        conexion.close()

    def cargarTablaDias(self):
        turno =self.txt_turno.text()
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT Dia FROM Dias WHERE modalidad=?",(turno,))
        datos = cursor.fetchall()
        self.tablaDias.setRowCount(len(datos))  

        for row, row_data in enumerate(datos):
            for col, value in enumerate(row_data):
                item = QTableWidgetItem(str(value))
                self.tablaDias.setItem(row, col, item)
        conexion.close()
        
class menuHorarioPlantilla(QMainWindow):
    def __init__(self,admin,modalidad):
        super(menuHorarioPlantilla,self).__init__()
        loadUi("./ui/plantilla_menu_de_horarios.ui",self)
        self.admin = admin
        self.modalidad =modalidad
        self.label.setText(self.modalidad)
        self.bt_crear.clicked.connect(self.crearHorario)
        
    def crearHorario(self):
        horario = crearHorarioPlantilla(admin=self.admin,modalidad=self.modalidad)
        widget.addWidget(horario)
        widget.setCurrentIndex(widget.currentIndex()+1)
    
class crearHorarioPlantilla(QMainWindow):
    def __init__(self,admin,modalidad):
        super(crearHorarioPlantilla,self).__init__()
        loadUi("./ui/plantilla_crear_hprarios.ui",self)
        self.admin = admin
        self.modalidad = modalidad
        self.datos_tabla = [] 
        self.label.setText(self.modalidad)
        # self.cargarHoras()
        self.tableWidget.cellClicked.connect(self.celda_clickeada)
        self.btn_buscarCarr.clicked.connect(self.buscarCarrera)
        self.btn_buscarSecc.clicked.connect(self.buscarSeccion)
        self.ln_carrera.textChanged.connect(self.buscarDisponibilidad)
        self.ln_sesion.textChanged.connect(self.buscarDisponibilidad)
        self.datos_almacenados =[]
        # self.cargarDias()
        self.cargarHorasYDias()
        self.obtener_dias()
    def buscarDisponibilidad(self):
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
        if carrera or sesion:
            self.searchHorario()
    def searchHorario(self):
        sesion =self.ln_sesion.text()
        carrera= self.ln_carrera.text()
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM HorarioTest WHERE Sesion = ? AND Carrera=? ",(sesion,carrera))
        existeHorario = cursor.fetchone()[0]
        if existeHorario:
            QMessageBox.information(self, "Advertencia", f"Ya existe un horario creado para {carrera} {sesion}")
            
            datos = []

            for row in range(self.tableWidget.rowCount()):
                fila = []
                for col in range(self.tableWidget.columnCount()):
                    item = self.tableWidget.item(row, col)
                    if item is not None:
                        fila.append(item.text())
                    else:
                        fila.append(None)
                datos.append(fila)

            # Asignar los datos al atributo de instancia
            self.datos_almacenados = datos
            horas = self.obtener_horas()
            dias = self.obtener_dias()
            dialogo = QuestionHorario(self, datos_carga_horas=horas, dias=dias)
            dialogo.exec_()
            return True
       
        return False

    def obtener_dias(self):
        try:
            # Obtener el número total de columnas en la tabla
            num_columnas = self.tableWidget.columnCount()

            # Obtener los días de las columnas restantes
            dias = [self.tableWidget.horizontalHeaderItem(col).text() for col in range(1, num_columnas)]

            print("Días:", dias)

            return dias, num_columnas

        except Exception as e:
            print(f"Error al obtener los días: {str(e)}")
            return None, None
    def obtener_horas(self):
        # Obtener solo la primera columna (la hora) de los datos almacenados
        horas = [fila[0] for fila in self.datos_almacenados if fila and fila[0] is not None]
        print(horas)
        return horas
    def buscarCarrera(self):
        consulta_like = "SELECT Descripcion, CodigoCarrera FROM Carreras WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT Descripcion, CodigoCarrera FROM Carreras;"
        dialogo = DialogoConsulta("Consulta de Carrera", "Seleccione una carrera:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_carrera.setText(codigo_materia) 
    # METODOD DE BUSCAR SECCION
    def buscarSeccion(self):
        consulta_like = "SELECT Numero FROM SesionCarrera WHERE Numero LIKE ?"
        consulta_sql_materia = "SELECT Numero FROM SesionCarrera;"
        dialogo = DialogoConsulta("Consulta de Seccion", "Seleccione una seccion:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_sesion.setText(codigo_materia)
            
    def cargarHorasYDias(self):
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()

        # Ejecutar la consulta para obtener los datos ordenados
        cursor.execute("SELECT Descripcion FROM Modulo WHERE Turno = ?", (self.modalidad,))
        horas = [fila[0] for fila in cursor.fetchall()]

        # Ejecutar la consulta para obtener los días ordenados
        cursor.execute("SELECT Dia FROM Dias WHERE modalidad = ?", (self.modalidad,))
        dias = [fila[0] for fila in cursor.fetchall()]

        # Configurar el número de filas y columnas en la tabla
        self.tableWidget.setRowCount(len(horas) + 1)  # +1 para la fila de horas
        self.tableWidget.setColumnCount(len(dias) + 1)  # +1 para la columna de días

        # Configurar los encabezados de la tabla
        self.tableWidget.setHorizontalHeaderLabels(["Hora"] + dias)

        # Limpiar la lista antes de cargar nuevos datos
        self.datos_tabla.clear()

        # Llenar la tabla con las horas y los días
        for row, row_data in enumerate(horas):
            item = QTableWidgetItem(str(row_data))
            self.tableWidget.setItem(row, 0, item)
            # Almacenar los datos en la lista
            self.datos_tabla.append((row, 0, str(row_data)))

       

        conexion.close()  # Cerrar la conexión a la base de datos al finalizar
#     def cargarHoras(self):
#         conexion = sqlite3.connect("./db/database.db")
#         cursor = conexion.cursor()
#         # Ejecutar la consulta para obtener los datos ordenados
#         cursor.execute("SELECT Descripcion FROM Modulo WHERE Turno = ?", (self.modalidad,))

#         datos = cursor.fetchall()

#         # Configurar el número de filas en la tabla
#         self.tableWidget.setRowCount(len(datos))

#         # Limpiar la lista antes de cargar nuevos datos
#         self.datos_tabla.clear()

#         # Llenar la tabla con los datos ordenados y almacenarlos en la lista
#         for row, row_data in enumerate(datos):
#             for col, value in enumerate(row_data):
#                 item = QTableWidgetItem(str(value))
#                 self.tableWidget.setItem(row, col, item)
#                 # Almacenar los datos en la lista
#                 self.datos_tabla.append((row, col, str(value)))

#     def cargarDias(self):
#         conexion = sqlite3.connect("./db/database.db")
#         cursor = conexion.cursor()

#         # Ejecutar la consulta para obtener los días ordenados
#         cursor.execute("SELECT Dia FROM Dias WHERE modalidad = ?", (self.modalidad,))
#         dias = [fila[0] for fila in cursor.fetchall()]

#         # Agregar "hora" como primer elemento en la lista de días
#         dias.insert(0, "hora")

#         self.tableWidget.setRowCount(1)
#         self.tableWidget.setColumnCount(len(dias))
#  # Configurar los encabezados de la tabla
#         self.tableWidget.setHorizontalHeaderLabels(dias)

       





        
    def celda_clickeada(self, fila, columna):
        try:
            # Obtener los datos de la celda clickeada desde la lista
            hora = self.tableWidget.item(fila, 0).text()

            # Obtener el día según la columna
            dia_item = self.tableWidget.horizontalHeaderItem(columna)
            dia = dia_item.text()

            print(f'Celda clickeada en el día {dia} en la hora {hora}')
            
            self.mostrar_dialogo(titulo=f"Formulario del dia {dia} a las horas {hora}",
                                    hora=hora,
                                    dia=dia,
                                    fila=fila,
                                    columna=columna
                                    )
        except:
            QMessageBox.warning(self,"Error","No hay datos ")
    def mostrar_dialogo(self, titulo, hora, dia,fila,columna ):
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
        if len(carrera) ==0 or len(sesion) ==0:
            QMessageBox.critical(self,"Error","Es necesario ingresar la carrera y su sesion")
            return
        else:
            dialog = FormularioDialog(titulo=titulo, hora=hora,
                                      dia=dia, fila=fila,columna=columna,horario=self,
                                      sesion=sesion,carrera=carrera)
            resultado = dialog.exec_()
            if resultado == QDialog.Accepted:
                texto_a_insertar = dialog.guardar()  # Obtener el texto desde la función guardar
                if texto_a_insertar is not None:
                    dialog.establecer_texto_en_celda(texto_a_insertar)

class SedesMenu(QMainWindow):
    def __init__(self,admin):
        super(SedesMenu,self).__init__()
        loadUi("./ui/sedes.ui",self)
        self.admin = admin
        
        self.bt_aggView_2.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_add) )
        self.bt_deleteView.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_delete) )
        self.bt_database.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page) )
        self.bt_aulas.clicked.connect(self.aulasmenu)
        self.bt_register.clicked.connect(self.agregarsede)
        self.bt_clear.clicked.connect(self.limpiarcampos)
        self.bt_act.clicked.connect(self.reloaddata)
        self.bt_delete.clicked.connect(self.eliminarsede)
        self.bt_search.clicked.connect(self.buscarparaeliminar)
        self.reloaddata()
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_salir_2.clicked.connect(self.regresaralmenu)
    def regresaralmenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def buscarparaeliminar(self):
        busqueda  = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Introduzca el codigo","Por favor introduzca el codigo de la sede")
            return
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT nombre,direccion FROM sedes WHERE codigo_sede =?",(busqueda,))
        resultado = cursor.fetchone()
        if not resultado:
            QMessageBox.information(self,"Error","No hay ninguna sede con ese codigo")
            return
        if resultado:
            self.txt_name_3.setText(resultado[0])
            self.txt_ubicacion_2.setText(resultado[1])
            
    def eliminarsede(self):
        busqueda  = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Introduzca el codigo","Por favor introduzca el codigo de la sede")
            return
        
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM sedes WHERE codigo_sede =?",(busqueda,))
        conexion.commit()
        self.txt_name_3.clear()
        self.txt_ubicacion_2.clear()
        QMessageBox.information(self,"Eliminado","Ha sido eliminado correctamente")
    def reloaddata(self):
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT codigo_sede,nombre,direccion FROM sedes")
            data = cursor.fetchall()
            self.tableWidget.setRowCount(len(data))  

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)

            conexion.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}")
    def limpiarcampos(self):
        self.txt_codigo.clear()
        self.txt_nombre.clear()
        self.txt_ubicacion.clear()
    def agregarsede(self):
        codigo = self.txt_codigo.text()
        nombre = self.txt_nombre.text()
        ubicacion = self.txt_ubicacion.text()
       
        if not codigo or not nombre or not ubicacion:
            QMessageBox.information(self,"Advertencia","Ingrese todos los campos por favor")
            return
        
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT codigo_sede FROM sedes WHERE codigo_sede=?", (codigo,)
                       )
        existing_teacher = cursor.fetchone()
        

        if existing_teacher:
            QMessageBox.warning(self, "Advertencia", "Ya existe una sede con el mismo codigo.")
            self.txt_codigo.clear()
            self.txt_nombre.clear()
            self.txt_ubicacion.clear()
            return
        else:
            cursor.execute("INSERT INTO sedes (codigo_sede, nombre,direccion)  VALUES (?, ?, ?)", (codigo, nombre, ubicacion))
            conexion.commit()
            
            QMessageBox.information(self, "Éxito", "Los datos se almacenaron correctamente")
            self.txt_codigo.clear()
            self.txt_nombre.clear()
            self.txt_ubicacion.clear()
       
       
        conexion.close()
    def aulasmenu(self):
        Aula = AulasMenu(admin=self.admin)
        widget.addWidget(Aula)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class AulasMenu(QMainWindow):
    def __init__(self,admin):
        super(AulasMenu,self).__init__()
        loadUi("./ui/aulas.ui",self)
        self.bt_sedes.clicked.connect(self.sedesmenu)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_salir_2.clicked.connect(self.regresaralmenu)
        self.admin = admin
        self.bt_buscarsede.clicked.connect(self.searchsede)
        self.bt_register.clicked.connect(self.aggaula)
        self.bt_clear.clicked.connect(self.limpiarcampos)
        self.bt_search.clicked.connect(self.buscarparaeliminar)
        self.bt_delete.clicked.connect(self.eliminarAula)
        self.bt_act.clicked.connect(self.reloaddata)
        self.bt_deleteView.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_delete) )
        self.bt_aggView_2.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page_add) )
        self.bt_database.clicked.connect( lambda:self.stackedWidget.setCurrentWidget(self.page) )
    
        self.reloaddata()        
        
        
    def regresaralmenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def reloaddata(self):
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT CodigoAula,Descripcion,codigo_sede FROM Aulas")
            data = cursor.fetchall()
            self.tableWidget.setRowCount(len(data))  

            for row, row_data in enumerate(data):
                for col, value in enumerate(row_data):
                    item = QTableWidgetItem(str(value))
                    self.tableWidget.setItem(row, col, item)

            conexion.close()
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Error al recuperar datos: {str(e)}")
    def buscarparaeliminar(self):
        busqueda  = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Introduzca el codigo","Por favor introduzca el codigo del aula")
            return
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT Descripcion,codigo_sede FROM Aulas WHERE CodigoAula =?",(busqueda,))
        resultado = cursor.fetchone()
        if not resultado:
            QMessageBox.information(self,"Error","No hay ninguna sede con ese codigo")
            return
        if resultado:
            self.txt_name_3.setText(resultado[0])
            self.txt_ubicacion.setText(resultado[1])
    def eliminarAula(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Advertencia","No ha ingresado nada para buscar")
            return
        conexion =sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("DELETE FROM Aulas WHERE CodigoAula =?",(busqueda,))
        conexion.commit()
        self.txt_name_3.clear()
        self.txt_ubicacion.clear()
        QMessageBox.information(self,"Eliminado","Ha sido eliminado correctamente")
    def aggaula(self):
        sede = self.txt_sedecodigo.text()
        nombre = self.txt_nombre.text()
        aula = self.txt_codigoaula.text()
       
        if not sede or not nombre or not aula:
            QMessageBox.information(self,"Advertencia","Ingrese todos los campos por favor")
            return
        
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT CodigoAula FROM Aulas WHERE CodigoAula=?", (aula,)
                       )
        existing_teacher = cursor.fetchone()
        

        if existing_teacher:
            QMessageBox.warning(self, "Advertencia", "Ya existe una aula con el mismo codigo.")
            self.txt_sedecodigo.clear()
            self.txt_nombre.clear()
            self.txt_codigoaula.clear()
            return
        else:
            cursor.execute("INSERT INTO Aulas (CodigoAula, Descripcion,codigo_sede)  VALUES (?, ?, ?)", (sede, nombre, aula))
            conexion.commit()
            
            QMessageBox.information(self, "Éxito", "Los datos se almacenaron correctamente")
            self.txt_sedecodigo.clear()
            self.txt_nombre.clear()
            self.txt_codigoaula.clear()
       
       
        conexion.close()    
    def limpiarcampos(self):
            self.txt_sedecodigo.clear()
            self.txt_nombre.clear()
            self.txt_codigoaula.clear()
    def searchsede(self):
        consulta_like = "SELECT codigo_sede, nombre,direccion FROM sedes WHERE nombre LIKE ?"
        consulta_sql_materia = "SELECT  codigo_sede,nombre,direccion FROM sedes;"
        dialogo = DialogoConsulta("Consulta de Sedes", "Seleccione una sede:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.txt_sedecodigo.setText(codigo_materia)
            
            
    def sedesmenu(self):
        Sede = SedesMenu(admin=self.admin)
        widget.addWidget(Sede)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
# MEnu principal de horarios
class horarios_menu(QMainWindow):
    def __init__(self, admin):
        super(horarios_menu, self).__init__()
        loadUi("./ui/menu-horarios_principal.ui",self)
        self.admin = admin
        self.bt_seccionView.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_seccion))
        self.bt_stckwdgt_individualProfe.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_profesor))
        self.bt_stckwdgt_individualAula.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_aula))
        self.bt_stckwdgt_ctrlAfacilit.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_controldeasistencia))
        self.btn_horaiossabatinos.clicked.connect(self.horariosSabatinosview)
        self.btn_horaiosdiurnos.clicked.connect(self.horariosdiurnosView)
        self.btn_volver_menu.clicked.connect(self.backMenu)
        
        #metodos para realizar la busqueda por cambio de texto
        self.ln_carrera.textChanged.connect(self.llamarBuscarseccion)
        self.ln_sesion.textChanged.connect(self.llamarBuscarseccion)
        self.ln_cedula_profesor.textChanged.connect(self.llamarbuscarProfesor)
        self.ln_codigo_aula.textChanged.connect(self.llamarbuscarAula)
        #Metodos para realizar busqueda con el dialog
        self.bt_carrera.clicked.connect(self.searchCarreraSeccion)
        self.bt_sesion.clicked.connect(self.buscarCarreraSeccion)
        self.btn_buscar_cedulaprof.clicked.connect(self.buscarprofesor)
        self.btn_buscar_codAula.clicked.connect(self.buscarAula)
       
    def buscarAula(self):
        consulta_like = "SELECT Descripcion,codigo_sede,CodigoAula FROM Aulas WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT  Descripcion,codigo_sede,CodigoAula FROM Aulas;"
        dialogo = DialogoConsulta("Consulta de Aula", "Seleccione una aula:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_codigo_aula.setText(codigo_materia)
          
    def buscarprofesor(self):
        consulta_like = "SELECT Nombres || ' ' || Apellidos AS Nombre_Y_Apellido, Cedula FROM Profesores WHERE Nombre_Y_Apellido LIKE ?"
        consulta_sql_profesor = "SELECT Nombres || ' ' || Apellidos AS Nombre_Y_Apellido ,Cedula FROM Profesores;"
        dialogo = DialogoConsulta("Consulta de Profesor", "Seleccione un profesor:", consulta_sql=consulta_sql_profesor,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_cedula_profesor.setText(codigo_materia)
            
    def llamarbuscarAula(self):
        descripcion = self.ln_codigo_aula.text()
        if descripcion :
            self.verDisponibilidadAula()
            
    def llamarbuscarProfesor(self):
        cedula = self.ln_cedula_profesor.text()
        if cedula:
            self.verDisponibilidadProfesor()
            
    def llamarBuscarseccion(self):
        carrera = self.ln_carrera.text()
        seccion = self.ln_sesion.text()
        if carrera and seccion:
            self.verDisponibilidadSeccion()
            
    def searchCarreraSeccion(self):
        consulta_like = "SELECT Descripcion, CodigoCarrera FROM Carreras WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT Descripcion, CodigoCarrera FROM Carreras;"
        dialogo = DialogoConsulta("Consulta de Carrera", "Seleccione una carrera:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_carrera.setText(codigo_materia)
     
    def buscarCarreraSeccion(self):
        consulta_like = "SELECT Numero FROM SesionCarrera WHERE Numero LIKE ?"
        consulta_sql_materia = "SELECT Numero FROM SesionCarrera;"
        dialogo = DialogoConsulta("Consulta de Seccion", "Seleccione una seccion:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_sesion.setText(codigo_materia)
       
    def verDisponibilidadAula(self):
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Dia, Hora, CodigoMat, CodigoAula, CedulaProf ,Sesion,Carrera FROM HorarioTest WHERE CodigoAula=? ",
            (self.ln_codigo_aula.text(),)
        )
        datos = cursor.fetchall()
        self.tableWidget_hor_IndAula.clearContents()

        

        for result in datos:
            dia = result[0]
            hora = result[1]
            codigo_mat = result[2]
            codigo_aula = result[3]
            cedula_prof = result[4]
            seccion = result[5]
            carrera = result[6]

            # Asignar la hora y el día a las posiciones correspondientes
            if hora == "07:30 A 08:10":
                fila = 0
            elif hora == "08:10 A 08:50":
                fila = 1
            elif hora == "08:50 A 09:30":
                fila = 2
            elif hora == "09:30 A 10:10":
                fila = 3
            elif hora == "10:10 A 10:50":
                fila = 4
            elif hora == "10:50 A 11:30":
                fila = 5
            elif hora == "11:30 A 12:10":
                fila = 6
            elif hora == "12:10 A 12:50":
                fila = 7
            elif hora == "12:50 A 1:30":
                fila = 8
            elif hora == "1:30 A 2:10":
                fila = 9
            elif hora == "2:10 A 2:50":
                fila = 10
            elif hora == "2:50 A 3:30":
                fila = 11
            elif hora == "3:30 A 4:10":
                fila = 12
            elif hora == "4:10 A 4:50":
                fila = 13
            elif hora == "4:50 A 5:30":
                fila = 14 
            else:
                # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                continue

            # Asignar el día a la columna correspondiente
            if dia == "Lunes":
                columna = 0
            elif dia == "Martes":
                columna = 1
            elif dia == "Miercoles":
                columna = 2
            elif dia == "Jueves":
                columna = 3
            elif dia == "Viernes":
                columna = 4
            elif dia == "Sabado":
                columna = 5
            else:
                # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                continue

            # Colocar los datos en la tabla
            item = QTableWidgetItem(f"{codigo_mat}\n{codigo_aula}\n{cedula_prof}\n{carrera}\n{seccion}")
            self.tableWidget_hor_IndAula.setItem(fila, columna, item) 
             
    def verDisponibilidadProfesor(self):
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Dia, Hora, CodigoMat, CodigoAula, CedulaProf ,Sesion,Carrera FROM HorarioTest WHERE CedulaProf=? ",
            (self.ln_cedula_profesor.text(),)
        )
        datos = cursor.fetchall()
        self.tableWidget_horIndprof.clearContents()

        

        for result in datos:
            dia = result[0]
            hora = result[1]
            codigo_mat = result[2]
            codigo_aula = result[3]
            cedula_prof = result[4]
            seccion = result[5]
            carrera = result[6]

            # Asignar la hora y el día a las posiciones correspondientes
            if hora == "07:30 A 08:10":
                fila = 0
            elif hora == "08:10 A 08:50":
                fila = 1
            elif hora == "08:50 A 09:30":
                fila = 2
            elif hora == "09:30 A 10:10":
                fila = 3
            elif hora == "10:10 A 10:50":
                fila = 4
            elif hora == "10:50 A 11:30":
                fila = 5
            elif hora == "11:30 A 12:10":
                fila = 6
            elif hora == "12:10 A 12:50":
                fila = 7
            elif hora == "12:50 A 1:30":
                fila = 8
            elif hora == "1:30 A 2:10":
                fila = 9
            elif hora == "2:10 A 2:50":
                fila = 10
            elif hora == "2:50 A 3:30":
                fila = 11
            elif hora == "3:30 A 4:10":
                fila = 12
            elif hora == "4:10 A 4:50":
                fila = 13
            elif hora == "4:50 A 5:30":
                fila = 14
            else:
                # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                continue

            # Asignar el día a la columna correspondiente
            if dia == "Lunes":
                columna = 0
            elif dia == "Martes":
                columna = 1
            elif dia == "Miercoles":
                columna = 2
            elif dia == "Jueves":
                columna = 3
            elif dia == "Viernes":
                columna = 4
            elif dia == "Sabado":
                columna = 5
            else:
                # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                continue

            # Colocar los datos en la tabla
            item = QTableWidgetItem(f"{codigo_mat}\n{codigo_aula}\n{cedula_prof}\n{carrera}\n{seccion}")
            self.tableWidget_horIndprof.setItem(fila, columna, item) 
          
            
    def verDisponibilidadSeccion(self):
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute(
            "SELECT Dia, Hora, CodigoMat, CodigoAula, CedulaProf FROM HorarioTest WHERE Carrera=? AND Sesion=?",
            (self.ln_carrera.text(), self.ln_sesion.text())
        )
        datos = cursor.fetchall()
        self.tableWidget_2.clearContents()

        

        for result in datos:
            dia = result[0]
            hora = result[1]
            codigo_mat = result[2]
            codigo_aula = result[3]
            cedula_prof = result[4]

            # Asignar la hora y el día a las posiciones correspondientes
            if hora == "07:30 A 08:10":
                fila = 0
            elif hora == "08:10 A 08:50":
                fila = 1
            elif hora == "08:50 A 09:30":
                fila = 2
            elif hora == "09:30 A 10:10":
                fila = 3
            elif hora == "10:10 A 10:50":
                fila = 4
            elif hora == "10:50 A 11:30":
                fila = 5
            elif hora == "11:30 A 12:10":
                fila = 6
            elif hora == "12:10 A 12:50":
                fila = 7
            elif hora == "12:50 A 1:30":
                fila = 8
            elif hora == "1:30 A 2:10":
                fila = 9
            elif hora == "2:10 A 2:50":
                fila = 10
            elif hora == "2:50 A 3:30":
                fila = 11
            elif hora == "3:30 A 4:10":
                fila = 12
            elif hora == "4:10 A 4:50":
                fila = 13
            elif hora == "4:50 A 5:30":
                fila = 14
            else:
                # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                continue

            # Asignar el día a la columna correspondiente
            if dia == "Lunes":
                columna = 0
            elif dia == "Martes":
                columna = 1
            elif dia == "Miercoles":
                columna = 2
            elif dia == "Jueves":
                columna = 3
            elif dia == "Viernes":
                columna = 4
            elif dia == "Sabado":
                columna = 5
            else:
                # En caso de que no haya coincidencia, puedes manejarlo según tu lógica
                continue

            # Colocar los datos en la tabla
            item = QTableWidgetItem(f"{codigo_mat}\n{codigo_aula}\n{cedula_prof}")
            self.tableWidget_2.setItem(fila, columna, item)

    def horariosdiurnosView(self):
        horarios = HorarioMenu(admin=self.admin)
        widget.addWidget(horarios)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def horariosSabatinosview(self):
        horarrios=Horario_SabatinoMenu(admin=self.admin)
        widget.addWidget(horarrios)
        widget.setCurrentIndex(widget.currentIndex()+1)
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

### Clase horariosdiurnosView ###
# MENU DE HORARIOS DIURNOS
class HorarioMenu(QMainWindow):
    def __init__(self , admin):
        super(HorarioMenu, self).__init__()
        loadUi("./ui/horarios.ui",self)
        self.admin = admin
        self.bt_back.clicked.connect(self.backMenu)
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_crear.clicked.connect(self.crearView)
        self.bt_buscar.clicked.connect(self.buscarAula)
        self.bt_profesor.clicked.connect(self.buscarprofesor)
        self.bt_profesor.clicked.connect(self.realizarbusquedaProfesor)
        self.bt_carrerabuscar.clicked.connect(self.buscarCarrera)
        self.bt_seccionbuscar.clicked.connect(self.buscarSeccion)
        
        # DEFINIR VALORES PARA LOS CHECKBOX DE CONSULTAR DISPONIBILIDAD AULAS
        self.diasLunesAulas = [{
            "07:30 A 08:10" : self.checkBox_0,
            "08:10 A 08:50" : self.checkBox_4,
            "08:50 A 09:30" : self.checkBox_11,
            "09:30 A 10:10": self.checkBox_5,
            "10:10 A 10:50" : self.checkBox_6,
            "10:50 A 11:30" : self.checkBox_7,
            "11:30 A 12:10" : self.checkBox_8,
            "12:10 A 12:50" : self.checkBox_9,
            "12:50 A 1:30" : self.checkBox_10
            
        }]
        self.diasMartesAulas = [{
            "07:30 A 08:10" : self.checkBox_12,
            "08:10 A 08:50" : self.checkBox_13,
            "08:50 A 09:30" : self.checkBox_14,
            "09:30 A 10:10" : self.checkBox_15,
            "10:10 A 10:50" : self.checkBox_16,
            "10:50 A 11:30" : self.checkBox_17,
            "11:30 A 12:10" : self.checkBox_18,
            "12:10 A 12:50" : self.checkBox_19,
            "12:50 A 1:30" : self.checkBox_20
        }]
        self.diasMiercolesAulas = [{
            "07:30 A 08:10" : self.checkBox_40,
            "08:10 A 08:50" : self.checkBox_66,
            "08:50 A 09:30" : self.checkBox_67,
            "09:30 A 10:10" : self.checkBox_68,
            "10:10 A 10:50" : self.checkBox_69,
            "10:50 A 11:30" : self.checkBox_70,
            "11:30 A 12:10" : self.checkBox_71,
            "12:10 A 12:50" : self.checkBox_72,
            "12:50 A 1:30" : self.checkBox_73
        }]
        self.diasJuevesAulas = [{
            "07:30 A 08:10" : self.checkBox_39,
            "08:10 A 08:50" : self.checkBox_49,
            "08:50 A 09:30" : self.checkBox_50,
            "09:30 A 10:10" : self.checkBox_51,
            "10:10 A 10:50" : self.checkBox_52,
            "10:50 A 11:30" : self.checkBox_53,
            "11:30 A 12:10" : self.checkBox_54,
            "12:10 A 12:50" : self.checkBox_55,
            "12:50 A 1:30" : self.checkBox_56
        }]
        self.diasViernesAulas = [{
            "07:30 A 08:10" : self.checkBox_57,
            "08:10 A 08:50" : self.checkBox_58,
            "08:50 A 09:30" : self.checkBox_59,
            "09:30 A 10:10" : self.checkBox_60,
            "10:10 A 10:50" : self.checkBox_61,
            "10:50 A 11:30" : self.checkBox_62,
            "11:30 A 12:10" : self.checkBox_63,
            "12:10 A 12:50" : self.checkBox_64,
            "12:50 A 1:30" : self.checkBox_65
        }]
        self.diasSabadoAulas = [{
            "07:30 A 08:10" : self.checkBox_21,
            "08:10 A 08:50" : self.checkBox_22,
            "08:50 A 09:30" : self.checkBox_23,
            "09:30 A 10:10" : self.checkBox_24,
            "10:10 A 10:50" : self.checkBox_25,
            "10:50 A 11:30" : self.checkBox_26,
            "11:30 A 12:10" : self.checkBox_27,
            "12:10 A 12:50" : self.checkBox_28,
            "12:50 A 1:30" : self.checkBox_29
        }]
        self.bt_buscar.clicked.connect(self.realizar_busquedaAula)
        
        # DEFINIR VALORES PARA LOS CHECKBOX DE CONSULTAR DISPONIBILIDAD SECCION

        self.diasLunesSeccion = [{
            "07:30 A 08:10" : self.checkBox_163,
            "08:10 A 08:50" : self.checkBox_164,
            "08:50 A 09:30" : self.checkBox_165,
            "09:30 A 10:10": self.checkBox_166,
            "10:10 A 10:50" : self.checkBox_167,
            "10:50 A 11:30" : self.checkBox_168,
            "11:30 A 12:10" : self.checkBox_169,
            "12:10 A 12:50" : self.checkBox_170,
            "12:50 A 1:30" : self.checkBox_171
            
        }]
        self.diasMartesSeccion = [{
            "07:30 A 08:10" : self.checkBox_172,
            "08:10 A 08:50" : self.checkBox_173,
            "08:50 A 09:30" : self.checkBox_174,
            "09:30 A 10:10" : self.checkBox_175,
            "10:10 A 10:50" : self.checkBox_176,
            "10:50 A 11:30" : self.checkBox_177,
            "11:30 A 12:10" : self.checkBox_178,
            "12:10 A 12:50" : self.checkBox_179,
            "12:50 A 1:30" : self.checkBox_180
        }]
        self.diasMiercolesSeccion = [{
            "07:30 A 08:10" : self.checkBox_181,
            "08:10 A 08:50" : self.checkBox_182,
            "08:50 A 09:30" : self.checkBox_183,
            "09:30 A 10:10" : self.checkBox_184,
            "10:10 A 10:50" : self.checkBox_185,
            "10:50 A 11:30" : self.checkBox_186,
            "11:30 A 12:10" : self.checkBox_187,
            "12:10 A 12:50" : self.checkBox_188,
            "12:50 A 1:30" : self.checkBox_189
        }]
        self.diasJuevesSeccion = [{
            "07:30 A 08:10" : self.checkBox_190,
            "08:10 A 08:50" : self.checkBox_191,
            "08:50 A 09:30" : self.checkBox_192,
            "09:30 A 10:10" : self.checkBox_193,
            "10:10 A 10:50" : self.checkBox_194,
            "10:50 A 11:30" : self.checkBox_195,
            "11:30 A 12:10" : self.checkBox_196,
            "12:10 A 12:50" : self.checkBox_197,
            "12:50 A 1:30" : self.checkBox_198
        }]
        self.diasViernesSeccion = [{
            "07:30 A 08:10" : self.checkBox_199,
            "08:10 A 08:50" : self.checkBox_200,
            "08:50 A 09:30" : self.checkBox_201,
            "09:30 A 10:10" : self.checkBox_202,
            "10:10 A 10:50" : self.checkBox_203,
            "10:50 A 11:30" : self.checkBox_204,
            "11:30 A 12:10" : self.checkBox_205,
            "12:10 A 12:50" : self.checkBox_206,
            "12:50 A 1:30" : self.checkBox_207
        }]
        self.diasSabadoSeccion = [{
            "07:30 A 08:10" : self.checkBox_208,
            "08:10 A 08:50" : self.checkBox_209,
            "08:50 A 09:30" : self.checkBox_210,
            "09:30 A 10:10" : self.checkBox_211,
            "10:10 A 10:50" : self.checkBox_212,
            "10:50 A 11:30" : self.checkBox_213,
            "11:30 A 12:10" : self.checkBox_214,
            "12:10 A 12:50" : self.checkBox_215,
            "12:50 A 1:30" : self.checkBox_216
        }]

        # DEFINIR VALORES PARA LOS CHECKBOX DE CONSULTAR DISPONIBILIDAD PROFESOR

        self.diasLunesProfesor =[{
            "07:30 A 08:10":self.checkBox_3,
            "08:10 A 08:50" : self.checkBox_110,
            "08:50 A 09:30" : self.checkBox_111,
            "09:30 A 10:10" : self.checkBox_112,
            "10:10 A 10:50" : self.checkBox_113,
            "10:50 A 11:30" : self.checkBox_114,
            "11:30 A 12:10" : self.checkBox_115,
            "12:10 A 12:50" : self.checkBox_116,
            "12:50 A 1:30" : self.checkBox_117
        }]
        self.diasMartesProfesor =[{
            "07:30 A 08:10":self.checkBox_118,
            "08:10 A 08:50" : self.checkBox_119,
            "08:50 A 09:30" : self.checkBox_120,
            "09:30 A 10:10" : self.checkBox_121,
            "10:10 A 10:50" : self.checkBox_122,
            "10:50 A 11:30" : self.checkBox_123,
            "11:30 A 12:10" : self.checkBox_124,
            "12:10 A 12:50" : self.checkBox_125,
            "12:50 A 1:30" : self.checkBox_126
        }]
        self.diasMiercolesProfesor =[{
            "07:30 A 08:10":self.checkBox_127,
            "08:10 A 08:50" : self.checkBox_128,
            "08:50 A 09:30" : self.checkBox_129,
            "09:30 A 10:10" : self.checkBox_130,
            "10:10 A 10:50" : self.checkBox_131,
            "10:50 A 11:30" : self.checkBox_132,
            "11:30 A 12:10" : self.checkBox_133,
            "12:10 A 12:50" : self.checkBox_134,
            "12:50 A 1:30" : self.checkBox_135
        }]
        self.diasJuevesProfesor =[{
            "07:30 A 08:10":self.checkBox_136,
            "08:10 A 08:50" : self.checkBox_137,
            "08:50 A 09:30" : self.checkBox_138,
            "09:30 A 10:10" : self.checkBox_139,
            "10:10 A 10:50" : self.checkBox_140,
            "10:50 A 11:30" : self.checkBox_141,
            "11:30 A 12:10" : self.checkBox_142,
            "12:10 A 12:50" : self.checkBox_143,
            "12:50 A 1:30" : self.checkBox_144
        }]
        self.diasViernesProfesor =[{
            "07:30 A 08:10":self.checkBox_145,
            "08:10 A 08:50" : self.checkBox_146,
            "08:50 A 09:30" : self.checkBox_147,
            "09:30 A 10:10" : self.checkBox_148,
            "10:10 A 10:50" : self.checkBox_149,
            "10:50 A 11:30" : self.checkBox_150,
            "11:30 A 12:10" : self.checkBox_151,
            "12:10 A 12:50" : self.checkBox_152,
            "12:50 A 1:30" : self.checkBox_153
        }]
        self.diasSabadoProfesor =[{
            "07:30 A 08:10":self.checkBox_154,
            "08:10 A 08:50" : self.checkBox_155,
            "08:50 A 09:30" : self.checkBox_156,
            "09:30 A 10:10" : self.checkBox_157,
            "10:10 A 10:50" : self.checkBox_158,
            "10:50 A 11:30" : self.checkBox_159,
            "11:30 A 12:10" : self.checkBox_160,
            "12:10 A 12:50" : self.checkBox_161,
            "12:50 A 1:30" : self.checkBox_162
        }]
        self.ln_disponibilidad_carrera.textChanged.connect(self.r3alizarbusqueda_Seccion)
        self.ln_disponibilidad_seccion.textChanged.connect(self.r3alizarbusqueda_Seccion)
        
    # METODO DE BUSCAR AULA
    def buscarAula(self):
        consulta_like = "SELECT Descripcion, CodigoAula,codigo_sede FROM Aulas WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT Descripcion, CodigoAula,codigo_sede FROM Aulas;"
        dialogo = DialogoConsulta("Consulta de Aula", "Seleccione una aula:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_disponibilidad_aula.setText(codigo_materia) 
    # METODO DE BUSCAR PROFESOR
    def buscarprofesor(self):
        consulta_like = "SELECT Nombres || ' ' || Apellidos AS Nombre_Y_Apellido, Cedula FROM Profesores WHERE Nombre_Y_Apellido LIKE ?"
        consulta_sql_profesor = "SELECT Nombres || ' ' || Apellidos AS Nombre_Y_Apellido ,Cedula FROM Profesores;"
        dialogo = DialogoConsulta("Consulta de Profesor", "Seleccione un profesor:", consulta_sql=consulta_sql_profesor,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_disponibilidad_profesores.setText(codigo_materia)
    # METODO DE BUSCAR CARRERA 
    def buscarCarrera(self):
        consulta_like = "SELECT Descripcion, CodigoCarrera FROM Carreras WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT Descripcion, CodigoCarrera FROM Carreras;"
        dialogo = DialogoConsulta("Consulta de Carrera", "Seleccione una carrera:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_disponibilidad_carrera.setText(codigo_materia) 
    # METODOD DE BUSCAR SECCION
    def buscarSeccion(self):
        consulta_like = "SELECT Numero FROM SesionCarrera WHERE Numero LIKE ?"
        consulta_sql_materia = "SELECT Numero FROM SesionCarrera;"
        dialogo = DialogoConsulta("Consulta de Seccion", "Seleccione una seccion:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_materia = dialogo.item_seleccionado()
            self.ln_disponibilidad_seccion.setText(codigo_materia)
    # METODO DE BUSCAR PROFESores
    def realizarbusquedaProfesor(self):
        #obtnern el valor de la seccion a buscar
        profesor = self.ln_disponibilidad_profesores.text()
        
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        
        for dia, checkboxes in zip(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
                                   [self.diasLunesProfesor, self.diasMartesProfesor, self.diasMiercolesProfesor, self.diasJuevesProfesor, self.diasViernesProfesor, self.diasSabadoProfesor]):
            for hora_inicio, checkbox in checkboxes[0].items():
                checkbox.setChecked(False)

                # Construir y ejecutar la consulta SQL para verificar la disponibilidad
                query = """
                    SELECT COUNT(*) FROM HorarioTest
                    WHERE Dia = ? AND Hora = ? AND CedulaProf = ?
                """
                cursor.execute(query, (dia, hora_inicio, profesor))
                resultado = cursor.fetchone()

                # Activar el checkbox si hay al menos un registro para esa hora
                if resultado[0] > 0:
                    checkbox.setChecked(True)

        # Cerrar la conexión a la base de datos
        conexion.close()
    def r3alizarbusqueda_Seccion(self):
        #obtnern el valor de la seccion a buscar
        carrera= self.ln_disponibilidad_carrera.text()
        seccion = self.ln_disponibilidad_seccion.text()
        
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
        
        for dia, checkboxes in zip(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
                                   [self.diasLunesSeccion, self.diasMartesSeccion, self.diasMiercolesSeccion, self.diasJuevesSeccion, self.diasViernesSeccion, self.diasSabadoSeccion]):
            for hora_inicio, checkbox in checkboxes[0].items():
                checkbox.setChecked(False)

                # Construir y ejecutar la consulta SQL para verificar la disponibilidad
                query = """
                    SELECT COUNT(*) FROM HorarioTest
                    WHERE Dia = ? AND Hora = ? AND Carrera = ? AND Sesion = ?
                """
                cursor.execute(query, (dia, hora_inicio,carrera, seccion))
                resultado = cursor.fetchone()

                # Activar el checkbox si hay al menos un registro para esa hora
                if resultado[0] > 0:
                    checkbox.setChecked(True)

        # Cerrar la conexión a la base de datos
        conexion.close()
        
    def realizar_busquedaAula(self):
        # Obtener el valor del QLineEdit
        aula = self.ln_disponibilidad_aula.text()

        # Conectar a la base de datos
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()

        # Iterar sobre las horas y días y desmarcar todos los checkboxes
        for dia, checkboxes in zip(["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado"],
                                   [self.diasLunesAulas, self.diasMartesAulas, self.diasMiercolesAulas, self.diasJuevesAulas, self.diasViernesAulas, self.diasSabadoAulas]):
            for hora_inicio, checkbox in checkboxes[0].items():
                checkbox.setChecked(False)

                # Construir y ejecutar la consulta SQL para verificar la disponibilidad
                query = """
                    SELECT COUNT(*) FROM HorarioTest
                    WHERE Dia = ? AND Hora = ? AND CodigoAula = ?
                """
                cursor.execute(query, (dia, hora_inicio, aula))
                resultado = cursor.fetchone()

                # Activar el checkbox si hay al menos un registro para esa hora
                if resultado[0] > 0:
                    checkbox.setChecked(True)

        # Cerrar la conexión a la base de datos
        conexion.close()
   
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        
        
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
       
    def crearView(self):
        menu = Horario(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

# CREAR HORARIOS DIURNOS   
class Horario(QMainWindow):
    def __init__(self,admin):
        super(Horario,self).__init__()
        loadUi("ui/horariosTabla.ui",self)
        self.tableWidget.cellClicked.connect(self.celda_clickeada)
        self.bt_carrera.clicked.connect(self.BuscarCarrera)
        self.bt_sesion.clicked.connect(self.buscarsesion)
        self.bt_preview.clicked.connect(self.previewpdf)
        self.admin = admin
        self.bt_volver.clicked.connect(self.backMenu)
        self.ln_carrera.textChanged.connect(self.buscarDisponibilidad)
        self.ln_sesion.textChanged.connect(self.buscarDisponibilidad)
        self.bt_guardar.clicked.connect(self.guardarPDF)
        
    def previewpdf(self):
        
        pdf = self.guardarPDF()
        if not pdf:
            QMessageBox.information(self,"PDF","Necesitas la ruta para poder visualizar el PDF")
            return
        else:
            dialogo=PreviewPDF(pdf_path=pdf)
            dialogo.exec_()
        
    def buscarDisponibilidad(self):
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
        if carrera or sesion:
            self.searchHorario()
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
                
    def guardarPDF(self):
        try:
            from   ui.pdfcrear import crear_pdf
            
            sesion = self.ln_sesion.text()
            carrera= self.ln_carrera.text()
          
            if not sesion or not carrera:
                QMessageBox.information(self,"Error","Es necesario ingresar la sesion y la carrera anteriormente")
                return
            ruta_salida, _ = QFileDialog.getSaveFileName(self, 'Guardar PDF', '', 'Archivos PDF (*.pdf)')

            # Verifica si el usuario canceló la selección
            if not ruta_salida:
                return
            else:
                crear_pdf(ruta_salida=ruta_salida,sesion=sesion,carrera=carrera )
                if crear_pdf:
                    return ruta_salida   
        except Exception as e:
            print(f"Error en vistaPrevia: {e}")
            
    def searchHorario(self):
        sesion =self.ln_sesion.text()
        carrera= self.ln_carrera.text()
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM HorarioTest WHERE Sesion = ? AND Carrera=? ",(sesion,carrera))
        existeHorario = cursor.fetchone()[0]
        if existeHorario:
            QMessageBox.information(self, "Advertencia", f"Ya existe un horario creado para {carrera} {sesion}")
            
            dialogo = QuestionHorario(self)
            dialogo.exec_()
            return True
       
        return False
    
    #ver horita
           
    def BuscarCarrera(self):
        consulta_like = "SELECT Descripcion, CodigoCarrera FROM Carreras WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT Descripcion, CodigoCarrera FROM Carreras;"
        dialogo = DialogoConsulta("Consulta de Carrera", "Seleccione una Carrera:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_carrera = dialogo.item_seleccionado()
            self.ln_carrera.setText(codigo_carrera) 
            
    def buscarsesion(self):
        consulta_like = "SELECT Numero FROM SesionCarrera WHERE Numero LIKE ?"
        consulta_sql_materia = "SELECT Numero FROM SesionCarrera;"
        dialogo = DialogoConsulta("Consulta de Sesion", "Seleccione una Sesion:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_sesion = dialogo.item_seleccionado()
            self.ln_sesion.setText(codigo_sesion) 
            
    def celda_clickeada(self, fila, columna):
        # obtener fila
        if fila == 0:
            hora= ("07:30 A 08:10")
            print(hora)
        if fila == 1:
            hora = ("08:10 A 08:50")
        if fila ==2:
            hora = ("08:50 A 09:30")
        if fila ==3:
            hora = ("09:30 A 10:10")
        if fila ==4 :
            hora= ("10:10 A 10:50")
        if fila == 5:
            hora = ( "10:50 A 11:30")
        if fila == 6:
            hora = ("11:30 A 12:10")
        if fila == 7:
            hora =("12:10 A 12:50")
        if fila == 8:
            hora =("12:50 A 1:30")
            
        if columna ==0:
            dia=("Lunes")
        if columna ==1:
            dia =("Martes")
        if columna ==2:
            dia =("Miercoles")
        if columna ==3:
            dia= ("Jueves")
        if columna ==4:
            dia =("Viernes")
        if columna ==5:
            dia =("Sabado")
            
        print(f'Celda clickeada en el dia {dia} en la hora {hora}')
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
       
        self.mostrar_dialogo(titulo=f"Formulario del dia {dia} a las horas {hora}",
                                hora=hora,
                                dia=dia,
                                fila=fila,
                                columna=columna
                                )
    def mostrar_dialogo(self, titulo, hora, dia,fila,columna ):
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
        if len(carrera) ==0 or len(sesion) ==0:
            QMessageBox.critical(self,"Error","Es necesario ingresar la carrera y su sesion")
            return
        else:
            dialog = FormularioDialog(titulo=titulo, hora=hora,
                                      dia=dia, fila=fila,columna=columna,horario=self,
                                      sesion=sesion,carrera=carrera)
            resultado = dialog.exec_()
            if resultado == QDialog.Accepted:
                texto_a_insertar = dialog.guardar()  # Obtener el texto desde la función guardar
                if texto_a_insertar is not None:
                    dialog.establecer_texto_en_celda(texto_a_insertar)


# Menu principal de horarios Sabatinos    
class Horario_SabatinoMenu(QMainWindow):
    def __init__(self , admin):
        super(Horario_SabatinoMenu, self).__init__()
        loadUi("./ui/menuprincipalsabantino.ui",self)
        self.admin = admin
        # self.bt_back.clicked.connect(self.backMenu)
        #self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_crear.clicked.connect(self.crearView)
        #self.bt_buscar.clicked.connect(self.buscarAula)
        #self.bt_profesor.clicked.connect(self.buscarprofesor)
        #self.bt_profesor.clicked.connect(self.realizarbusquedaProfesor)
        #self.bt_carrerabuscar.clicked.connect(self.buscarCarrera)
        #self.bt_seccionbuscar.clicked.connect(self.buscarSeccion)
    
    def crearView(self):
        menu = horario_sabatino(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)

class DialogoConsulta(QDialog):
    def __init__(self, titulo, mensaje, consulta_sql,consulta_like):
        super().__init__()
        
        self.setWindowTitle(titulo)
        layout = QVBoxLayout()
        layout.addWidget(QLabel(mensaje))


        self.campo_busqueda = QLineEdit(self)
        self.campo_busqueda.setPlaceholderText("Buscar...")
        
        self.campo_busqueda.textChanged.connect(lambda : self.cargar_datos(consulta_sql,consulta_like))
       
        layout.addWidget(self.campo_busqueda)
    
        # Crear la tabla de resultados
        self.tabla_resultados = QTableWidget(self)
        # Cargar datos desde la base de datos
        self.cargar_datos(consulta_sql,consulta_like)
       
       
        self.tabla_resultados.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.tabla_resultados.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        layout.addWidget(self.tabla_resultados)
       
        
        self.boton_aceptar = QPushButton("Aceptar")
        self.boton_aceptar.clicked.connect(self.aceptar)
       
        layout.addWidget(self.boton_aceptar)
        self.setLayout(layout)

        # Cerrar la conexión a la base de datos al finalizar
        

    def cargar_datos(self,  consulta_sql,consulta_like):
        conexion = sqlite3.connect("./db/database.db")
        cursor = conexion.cursor()
       
        termino_busqueda = self.campo_busqueda.text()
        if termino_busqueda:
            termino_busqueda = f"%{termino_busqueda}%"
            cursor.execute(consulta_like, (termino_busqueda,))
        else :
             cursor.execute(consulta_sql)
        
        datos = cursor.fetchall()
        if len(datos) <=0:
            QMessageBox.information(self,"Error ","No se encontraron registros.")
            self.campo_busqueda.clear()
            return

        # Configurar el número de filas y columnas de la tabla
        self.tabla_resultados.setRowCount(len(datos))
        self.tabla_resultados.setColumnCount(len(datos[0]))
        columnas = [desc[0] for desc in cursor.description]

        self.tabla_resultados.setHorizontalHeaderLabels(columnas)

        # Llenar la tabla con los datos de la consulta
        for fila_num, fila in enumerate(datos):
            for col_num, dato in enumerate(fila):
                item = QTableWidgetItem(str(dato))
                self.tabla_resultados.setItem(fila_num, col_num, item)
        conexion.close()
    
    def item_seleccionado(self):
       
        # Obtener el índice de la fila seleccionada
        fila_seleccionada = self.tabla_resultados.currentRow()

        # Obtener el texto de la primera columna de la fila seleccionada
        texto_seleccionado = self.tabla_resultados.item(fila_seleccionada, 0).text()

        return texto_seleccionado



    def aceptar(self):
        self.accept()


### CREAR HORARIO SABATINO
class horario_sabatino(QMainWindow):
    def __init__(self,admin):
        super(horario_sabatino,self).__init__()
        loadUi("./ui/horario_sabatinocrear.ui",self)
        self.tableWidget.cellClicked.connect(self.celda_clickeada)
        self.btn_buscarCarr.clicked.connect(self.BuscarCarrera)
        self.btn_buscarSecc.clicked.connect(self.buscarsesion)
        self.btn_vistaPrevia.clicked.connect(self.previewpdf)
        self.admin = admin
        self.bt_volver.clicked.connect(self.backMenu)
        self.ln_carrera.textChanged.connect(self.buscarDisponibilidad)
        self.ln_sesion.textChanged.connect(self.buscarDisponibilidad)
        self.btn_guardar.clicked.connect(self.guardarPDF)
        
    def previewpdf(self):
        
        pdf = self.guardarPDF()
        if not pdf:
            QMessageBox.information(self,"PDF","Necesitas la ruta para poder visualizar el PDF")
            return
        else:
            dialogo=PreviewPDF(pdf_path=pdf)
            dialogo.exec_()
        
    def buscarDisponibilidad(self):
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
        if carrera or sesion:
            self.searchHorario()
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
                
    def guardarPDF(self):
        try:
            from   ui.pdfcrear import crear_pdf
            
            sesion = self.ln_sesion.text()
            carrera= self.ln_carrera.text()
          
            if not sesion or not carrera:
                QMessageBox.information(self,"Error","Es necesario ingresar la sesion y la carrera anteriormente")
                return
            ruta_salida, _ = QFileDialog.getSaveFileName(self, 'Guardar PDF', '', 'Archivos PDF (*.pdf)')

            # Verifica si el usuario canceló la selección
            if not ruta_salida:
                return
            else:
                crear_pdf(ruta_salida=ruta_salida,sesion=sesion,carrera=carrera )
                if crear_pdf:
                    return ruta_salida   
        except Exception as e:
            print(f"Error en vistaPrevia: {e}")
            
    def searchHorario(self):
        sesion =self.ln_sesion.text()
        carrera= self.ln_carrera.text()
        conexion = sqlite3.connect("db/database.db")
        cursor = conexion.cursor()
        cursor.execute("SELECT COUNT(*) FROM HorarioTest WHERE Sesion = ? AND Carrera=? ",(sesion,carrera))
        existeHorario = cursor.fetchone()[0]
        if existeHorario:
            QMessageBox.information(self, "Advertencia", f"Ya existe un horario creado para {carrera} {sesion}")
            
            dialogo = QuestionHorario(self)
            dialogo.exec_()
            return True
       
        return False
           
    def BuscarCarrera(self):
        consulta_like = "SELECT Descripcion, CodigoCarrera FROM Carreras WHERE Descripcion LIKE ?"
        consulta_sql_materia = "SELECT Descripcion, CodigoCarrera FROM Carreras;"
        dialogo = DialogoConsulta("Consulta de Carrera", "Seleccione una Carrera:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_carrera = dialogo.item_seleccionado()
            self.ln_carrera.setText(codigo_carrera) 
            
    def buscarsesion(self):
        consulta_like = "SELECT Numero FROM SesionCarrera WHERE Numero LIKE ?"
        consulta_sql_materia = "SELECT Numero FROM SesionCarrera;"
        dialogo = DialogoConsulta("Consulta de Sesion", "Seleccione una Sesion:", consulta_sql=consulta_sql_materia,consulta_like=consulta_like)
        if dialogo.exec_() == QDialog.Accepted:
            codigo_sesion = dialogo.item_seleccionado()
            self.ln_sesion.setText(codigo_sesion) 
            
    def celda_clickeada(self, fila, columna):
        # obtener fila
        if fila == 0:
            hora= ("07:30 A 08:10")
            print(hora)
        if fila == 1:
            hora = ("08:10 A 08:50")
        if fila ==2:
            hora = ("08:50 A 09:30")
        if fila ==3:
            hora = ("09:30 A 10:10")
        if fila ==4 :
            hora= ("10:10 A 10:50")
        if fila == 5:
            hora = ( "10:50 A 11:30")
        if fila == 6:
            hora = ("11:30 A 12:10")
        if fila == 7:
            hora =("12:10 A 12:50")
        if fila == 8:
            hora =("12:50 A 1:30")
        if fila == 9:
            hora=("1:30 A 2:10")
        if fila == 10:
            hora=("2:10 A 2:50")
        if fila == 11:
            hora=("2:50 A 3:30")
        if fila == 12:
            hora=("3:30 A 4:10")
        if fila == 13:
            hora= ("4:10 A 4:50")
        if fila== 14:
            hora=("4:50 A 5:30")

        if columna ==0:
            dia =("Sabado")
            
        print(f'Celda clickeada en el dia {dia} en la hora {hora}')
  
        self.mostrar_dialogo(titulo=f"Formulario del dia {dia} a las horas {hora}",
                                hora=hora,
                                dia=dia,
                                fila=fila,
                                columna=columna
                                )
    def mostrar_dialogo(self, titulo, hora, dia,fila,columna ):
        carrera = self.ln_carrera.text()
        sesion = self.ln_sesion.text()
        if len(carrera) ==0 or len(sesion) ==0:
            QMessageBox.critical(self,"Error","Es necesario ingresar la carrera y su sesion")
            return
        else:
            dialog = FormularioDialog(titulo=titulo, hora=hora,
                                      dia=dia, fila=fila,columna=columna,horario=self,
                                      sesion=sesion,carrera=carrera)
            resultado = dialog.exec_()
            if resultado == QDialog.Accepted:
                texto_a_insertar = dialog.guardar()  # Obtener el texto desde la función guardar
                if texto_a_insertar is not None:
                    dialog.establecer_texto_en_celda(texto_a_insertar)
        

# CLASE DE VENTANA DE GESTIONAR USUARIOS
    
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
        #widget.setFixedHeight(1000)
        #widget.setFixedWidth(1000)   

# CLASE DE LA VENTANA DE GESTION DE CARRERAS       
class MenuCarreras(QMainWindow):
    def __init__(self, admin):
        super(MenuCarreras, self).__init__()
        loadUi("./ui/carreras.ui",self)
        self.admin = admin
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_view.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_view))
        self.bt_agg.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_agg))
        self.bt_edit.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_edit))
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
        #widget.setFixedHeight(1000)
        #widget.setFixedWidth(1000)  

# CLASES DE LA VENTANA DE GESTION DE MATERIAS
class MenuMaterias(QMainWindow):
    def __init__(self, admin):
        super(MenuMaterias, self).__init__()
        loadUi("./ui/materias.ui",self)
        self.admin = admin
        self.bt_salir.clicked.connect(lambda : QApplication.quit())
        self.bt_view.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_view))
        self.bt_agg.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_agg))
        self.bt_edit.clicked.connect(lambda :self.stackedWidget.setCurrentWidget(self.page_edit))
        self.bt_back.clicked.connect(self.backMenu)
        self.bt_agg_2.clicked.connect(self.addData)
        self.bt_act.clicked.connect(self.ViewData)
        self.bt_search.clicked.connect(self.searchData)
        self.bt_delete.clicked.connect(self.deleteData)
        self.bt_edit_2.clicked.connect(self.modifyData)
    def searchData(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Error","Se necesita el codigo para realizar la busqueda")
            return
        else:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT Codigo,Nombre FROM Materia WHERE Codigo=?",(busqueda,))
            resultado = cursor.fetchone()
            if not resultado:
                QMessageBox.information(self,"No existe","No existe una materia con ese codigo")
            if resultado:
                self.txt_name_2.setText(str(resultado[0]))
                self.txt_apell_2.setText(str(resultado[1]))
            conexion.close()
        
    def limpiaredit(self):
        self.txt_name_2.clear()
        self.ln_busqueda.clear()
        self.txt_apell_2.clear()
    def deleteData(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Error","Se necesita el codigo para realizar la busqueda")
            return
        else:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM Materia WHERE Codigo=?",(busqueda,))
            conexion.commit()
            QMessageBox.information(self,"Eliminado","Ha sido eliminado correctamente")
            self.limpiaredit()
    def modifyData(self):
        busqueda = self.ln_busqueda.text()
        if not busqueda:
            QMessageBox.information(self,"Error","Se necesita el codigo para realizar la busqueda")
            return
        else:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            codigo = self.txt_name_2.text()
            nombre = self.txt_apell_2.text()
            cursor.execute("UPDATE Materia SET Codigo=?, Nombre=? WHERE Codigo=?",(codigo,nombre,busqueda))
            conexion.commit()
            QMessageBox.information(self,"Modificado","La informacion ha sido actualizada correctamente")
            self.limpiaredit()
            
    def ViewData(self):
        print("click")
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Materia")
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
        Codigo = self.txt_code.text()
        Nombre = self.txt_name.text()
       
        if not Codigo or not Nombre :
            QMessageBox.information(self,"Añadir","Por favor introduzca todos los campos para agregarlos")
            return
        try:
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()

            # Comprobar si ya existe una con el mismo codigo
            cursor.execute("SELECT Codigo FROM Materia WHERE Codigo=?", (Codigo,))
            existing_materia = cursor.fetchone()

            if existing_materia:
                QMessageBox.warning(self, "Advertencia", "Ya existe una materia con el mismo codigo.")
                self.txt_name.clear()
                self.txt_code.clear()
               
            else:
                # Si no existe, agregar la nueva materia a la base de datos
                cursor.execute("INSERT INTO Materia (Codigo, Nombre) VALUES (?, ?)", (Codigo, Nombre))
                
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

# CLASES DE LA VENTAN DE GESTION DE PROFESORES
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
        self.txt_telefono_2.clear()
        self.txt_correo.clear()
        self.txt_titulos.clear()
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
                self.clearInputs()
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
            cursor.execute("SELECT Nombres, Apellidos,Cedula,Telefono,Mail,TituloProfesion FROM Profesores WHERE Cedula=?" ,(busqueda,))
            resultado = cursor.fetchone()
            if resultado:
                self.txt_name_2.setText(resultado[0])
                self.txt_apell_2.setText(resultado[1])
                self.txt_cedula_2.setText(resultado[2])
                self.txt_telefono_2.setText(resultado[3])
                self.txt_correo.setText(resultado[4])
                self.txt_titulos.setText(resultado[5])
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
            telefono = self.txt_telefono_2.text()
            correo =self.txt_correo.text()
            titulos = self.txt_titulos.text()
            conexion = sqlite3.connect("./db/database.db")
            cursor = conexion.cursor()
            cursor.execute("UPDATE Profesores SET Nombres=? ,Apellidos=? ,Telefono=?,Mail=?,TituloProfesion=? WHERE Cedula=?", (nombres, apellidos,telefono,correo,titulos, cedula))
            conexion.commit()
            QMessageBox.information(self, "Éxito", "Informacion actualizada correctamente.")
            conexion.close()
        except sqlite3.Error as error:
            QMessageBox.critical(self, "Error", f"Error al registrar el profesor: {str(error)}")
            
    def aggTeacher(self):
        nombres = self.txt_name.text()
        apellido = self.txt_apell.text()
        cedula = self.txt_cedula.text()
        telefono = self.txt_telefono.text()
        correo = self.txt_mail.text()
        titulos = self.txt_profesion.text()
        if not nombres or not apellido or not cedula or not telefono or not correo or not titulos:
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
                self.txt_telefono.clear()
                self.txt_mail.clear()
                self.txt_profesion.clear()
            else:
                # Si no existe, agregar el nuevo profesor a la base de datos
                cursor.execute("INSERT INTO Profesores (Nombres, Apellidos, Cedula,Telefono,Mail,TituloProfesion) VALUES (?, ?, ?, ?, ?,?)", (nombres, apellido, cedula, telefono, correo, titulos))
                
                conexion.commit()
                QMessageBox.information(self, "Éxito", "Los datos se almacenaron correctamente")
                self.txt_name.clear()
                self.txt_apell.clear()
                self.txt_cedula.clear()
                self.txt_telefono.clear()
                self.txt_mail.clear()
                self.txt_profesion.clear()
    
            conexion.close()
        except:
            QMessageBox.warning(self,"Error","Error con la base de datos")
            
    def backMenu(self):
        menu = MenuPrincipal(self.admin)
        widget.addWidget(menu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        #widget.setFixedHeight(1000)
        #widget.setFixedWidth(1000)   

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("IUTA")
    ingreso_usuario = IngresoUsuario()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(ingreso_usuario)
    widget.move(400, 80)
    widget.show()


    sys.exit(app.exec_())