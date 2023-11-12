import sqlite3
from PyQt5.QtGui import QIcon, QFont, QTextDocument
from PyQt5.QtCore import Qt, QFileInfo, QTextCodec, QByteArray, QTranslator, QLocale, QLibraryInfo
from PyQt5.QtWidgets import (QApplication, QTreeWidget, QTreeWidgetItem, QDialog, QPushButton, QFileDialog,
                             QMessageBox, QToolBar)
from PyQt5.QtPrintSupport import QPrintDialog, QPrinter, QPrintPreviewDialog
import sys
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QMessageBox,QLabel,QTableWidgetItem
from PyQt5.QtWidgets import QWidget ,QApplication ,QMainWindow,QStackedWidget,QGraphicsDropShadowEffect, QCalendarWidget , QBoxLayout



class IngresoUsuario(QMainWindow):
    def __init__(self):
        super(IngresoUsuario,self).__init__()
        loadUi("ui/pdfui.ui",self)
        self.bt_buscar.clicked.connect(self.cargarDatos)
        self.bt_preview.clicked.connect(self.previewpdf)
        self.documento = QTextDocument()
        
    def previewpdf(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)
            
            vista = QPrintPreviewDialog(impresion, self)
            vista.setWindowTitle("Vista previa")
            vista.setWindowFlags(Qt.Window)
            vista.resize(800, 600)

            exportarPDF = vista.findChildren(QToolBar)
            exportarPDF[0].addAction(QIcon("exportarPDF.png"), "Exportar a PDF", self.exportarPDF)
            
            vista.paintRequested.connect(self.vistaPreviaImpresion)
            vista.exec_()
        else:
            QMessageBox.critical(self, "Vista previa", "No hay datos para visualizar.   ",
                                 QMessageBox.Ok)


    def exportarPDF(self):
        if not self.documento.isEmpty():
            nombreArchivo, _ = QFileDialog.getSaveFileName(self, "Exportar a PDF", "Listado de usuarios",
                                                           "Archivos PDF (*.pdf);;All Files (*)",
                                                           options=QFileDialog.Options())

            if nombreArchivo:
                # if QFileInfo(nombreArchivo).suffix():
                #     nombreArchivo += ".pdf"

                impresion = QPrinter(QPrinter.HighResolution)
                impresion.setOutputFormat(QPrinter.PdfFormat)
                impresion.setOutputFileName(nombreArchivo)
                self.documento.print_(impresion)

                QMessageBox.information(self, "Exportar a PDF", "Datos exportados con éxito.   ",
                                        QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Exportar a PDF", "No hay datos para exportar.   ",
                                 QMessageBox.Ok)
    def vistaPreviaImpresion(self, impresion):
        self.documento.print_(impresion)

    def Imprimir(self):
        if not self.documento.isEmpty():
            impresion = QPrinter(QPrinter.HighResolution)
            
            dlg = QPrintDialog(impresion, self)
            dlg.setWindowTitle("Imprimir documento")

            if dlg.exec_() == QPrintDialog.Accepted:
                self.documento.print_(impresion)

            del dlg
        else:
            QMessageBox.critical(self, "Imprimir", "No hay datos para imprimir.   ",
                                 QMessageBox.Ok)

    def cargarDatos(self):
        conexionDB = sqlite3.connect("db/database.db")
        cursor = conexionDB.cursor()

        cursor.execute("SELECT Hora,Dia , CodigoMat, CodigoAula ,CedulaProf FROM HorarioTest")
        datosDB = cursor.fetchall()

        conexionDB.close()

        if datosDB:
            self.documento.clear()
            self.treeWidget.clear()

            datos = ""
            datosDB = sorted(datosDB, key=lambda x: x[0])

            
            item_widget = []
            for dato in datosDB:
                hora, dia, codigo_mat, codigo_aula, cedula_prof = dato
                datos += f"<tr><td>{hora}</td><td>"

                # Agregar etiquetas <p> para CodigoAula, CodigoMat y CedulaProf
                datos += f"<p>{codigo_aula}</p>"
                datos += f"<p>{codigo_mat}</p>"
                datos += f"<p>{cedula_prof}</p>"

                datos += "</td></tr>"
                item_widget.append(QTreeWidgetItem((str(hora), dia, codigo_mat, codigo_aula, cedula_prof)))

            reporteHtml = """
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<style>
  .horario-table {
        border-collapse: collapse;
        width: 100%;
    }

    .horario-table th, .horario-table td {
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }

    
    .container-tabla {
        margin-top: 70px;
        display: table;
        width: 100%;
        border-collapse: collapse;
    }

    .element-div {
        display: table-cell;
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }   

    .container-periodo{
        display: flex;
        margin-left: 80%;
        margin-top: 10px;
        font-weight: bolder;
    }
    .container-fecha{
        display: flex;
        margin-top: -15%;
        margin-left: 70%;
    }
    .date{
        text-decoration: underline;
    }
    .title{
        font-size: 25px;
        text-align: center;
        margin-bottom: 3%;
        text-decoration: underline;
        font-style: italic;
    }
    img{
        width: 200px;
        height: 100px;
        
    }
    .div-title{
       
        width: 30%;
        text-align: center;
        margin-left: 18%;
        margin-top: -8%;
        line-height: 1.0;
        font-weight: bold;
    }
</style>
</head>
<body>
 <div class="div-title">
        <p>
            Instituto Universitario De Tecnologia 
            
        </p>
        <p>
            De Administración Industrial 
        </p>
        <p>
            Extensión Puerto La Cruz

        </p>
    </div>  
    <p class="title">
        HORARIO
    </p>
    <div class="container-fecha">
        <p class="fecha">Fecha de Impresión 11/11/2023</p>
    </div>
    <div class="container-periodo">
        <p>PERIODO:  <p class="date"> 2023-III</p> </p>
    </div>

    <div class="container-tabla">
        <div class="especialidad  element-div primerelemento">
            <p>Especialidad</p>
            <p>INFORMÁTICA</p>
        </div>
        <div class="semestre element-div segundoelemento">
            <p>Semestre</p>
            <p>1</p>
        </div>
        <div class="turno element-div tercerelemento">
            <p>Turno</p>
            <p>DIURNO</p>
        </div>
        <div class="SECCION element-div cuartoelemento">
            <p>Sección</p>
            <p>PRIMERO INF 01</p>
        </div>
    </div>

<table align="left" width="100%" cellspacing="0">
  <tr class="horario-header">
            <th>HORA</th>
            <th>LUNES</th>
            <th>MARTES</th>
            <th>MIERCOLES</th>
            <th>JUEVES</th>
            <th>VIERNES</th>
            <th>SABADO</th>
        </tr>
  [DATOS]
</table>

</body>
</html>
""".replace("[DATOS]", datos)

            datos = QByteArray()
            datos.append(str(reporteHtml))
            codec = QTextCodec.codecForHtml(datos)
            unistr = codec.toUnicode(datos)

            if Qt.mightBeRichText(unistr):
                self.documento.setHtml(unistr)
            else:
                self.documento.setPlainText(unistr)

            self.treeWidget.addTopLevelItems(item_widget)
        else:
            QMessageBox.information(self, "Buscar usuarios", "No se encontraron resultados.      ",
                                    QMessageBox.Ok)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationName("Clinica")  # Establecer el nombre de la aplicación

    ingreso_usuario = IngresoUsuario()
    ingreso_usuario.showFullScreen()  # Muestra la ventana en pantalla completa

    widget = QStackedWidget()
    widget.addWidget(ingreso_usuario)
    widget.setGeometry(ingreso_usuario.geometry())
    widget.show()
    icon = QIcon("./interfaces/ELEMENTOS GRAFICOS/odontology-outline.png")
    ingreso_usuario.setWindowIcon(icon)
    sys.exit(app.exec_())