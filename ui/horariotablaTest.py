import sys
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

    def guardar(self, checkbox):
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
            cursor.execute("INSERT INTO HorarioTest (Dia, Hora, CodigoMat, CodigoAula, CedulaProf,Carrera,Sesion) VALUES (?,?,?,?,?,?,?)",
                           (self.dia, self.hora, codigoMateria, codigoSalon, cedulaProfesor,self.carrera,self.sesion))
            conexion.commit()
            conexion.close()
            QMessageBox.information(self, "Exito", "Los datos fueron almacenados correctamente")

            print(f"El código de materia es {codigoMateria}, salón {codigoSalon}, cédula profesor {cedulaProfesor}")
            text_for_checkbox = (f"{codigoMateria}\n{codigoSalon}\n{cedulaProfesor}")
            self.establecer_texto_en_celda(text_for_checkbox)
            self.hide()
            return text_for_checkbox

    def establecer_texto_en_celda(self, texto):
        # Obtener la instancia de QTableWidget desde la instancia de Horario
        table_widget = self.horario.tableWidget

        # Establecer el texto en la celda específica
        table_widget.setItem(self.fila, self.columna, QTableWidgetItem(texto))
class Horario(QMainWindow):
    def __init__(self):
        super(Horario,self).__init__()
        loadUi("ui/horariosTabla.ui",self)
        self.tableWidget.cellClicked.connect(self.celda_clickeada)
        self.bt_carrera.clicked.connect(self.BuscarCarrera)
        self.bt_sesion.clicked.connect(self.buscarsesion)
        
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
            hora= ("7:30 a 8:10")
            print(hora)
        if fila == 1:
            hora = ("08:10  A 08:50")
        if fila ==2:
            hora = ("08:50 A 09:30")
        if fila ==3:
            hora = ("09:30 A 10:10")
        if fila ==4 :
            hora= ("10:10 A 10:50")
        if fila == 5:
            hora = ( "10:50 A 11:30")
        if fila == 6:
            hora = ("11:30 A 12:50")
        if fila == 7:
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("IUTA")
    ingreso_usuario = Horario()
    ingreso_usuario.showFullScreen()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget(ingreso_usuario)
    widget.move(400, 80)
    widget.show()


    sys.exit(app.exec_())
        