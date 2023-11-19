import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QPushButton, QFileDialog, QWidget
from PyQt5.QtGui import QPixmap,QImage
from weasyprint import HTML

import os
import base64
import sqlite3
import fitz
from datetime import datetime

def image_url_to_base64(image_url):
    try:
        import requests
        response = requests.get(image_url)
        response.raise_for_status()
        encoded_string = base64.b64encode(response.content).decode("utf-8")
        return f"data:{response.headers['Content-Type']};base64,{encoded_string}"
    except Exception as e:
        print(f"Error al obtener la imagen desde la URL: {e}")
        return None 

def recuperar_datos_bd():
    conexion = sqlite3.connect("db/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT Dia,Hora,CodigoMat,CodigoAula,CedulaProf FROM HorarioTest")
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base
    

def crear_pdf(ruta_salida):
    imagen_url = 'https://www.eduopinions.com/wp-content/uploads/2018/02/Instituto-Universitario-de-Tecnolog%C3%ADa-de-Administraci%C3%B3n-Industrial-IUTA-logo-350x181.gif'
    
    imagen_base64 = image_url_to_base64(imagen_url)
    Especialidad = 'Informatica'
    Semestre = '7'
    Turno = 'Diurno'
    Seccion ='Unica'
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    print("Fecha actual:", fecha_formateada)
    if imagen_base64:
        # Definir los datos de la tabla
        datos_base = recuperar_datos_bd()        
        filas_datos = []
        for dato in datos_base:
            dia = dato[0]
            hora = dato[1]

            # Buscar si ya existe una fila con esta hora
            fila_existente = next((fila for fila in filas_datos if fila["hora"] == hora), None)

            # Si no existe, crear una nueva fila
            if not fila_existente:
                nueva_fila = {"hora": hora, "lunes": "", "martes": "", "miercoles": "", "jueves": "", "viernes": "", "sabado": ""}
                filas_datos.append(nueva_fila)
                fila_existente = nueva_fila

            # Colocar los datos en la celda correspondiente al día
            fila_existente[dia.lower()] = f"{dato[2]} </br> {dato[3]} </br> {dato[4]}"
        filas_datos = sorted(filas_datos, key=lambda x: x['hora'])

        filas_html = ""
        for fila in filas_datos:
            fila_html = "<tr>"
            fila_html += f"<th>{fila.get('hora', '')}</th>"
            fila_html += f"<td>{fila.get('lunes', '')}</td>"
            fila_html += f"<td>{fila.get('martes', '')}</td>"
            fila_html += f"<td>{fila.get('miercoles', '')}</td>"
            fila_html += f"<td>{fila.get('jueves', '')}</td>"
            fila_html += f"<td>{fila.get('viernes', '')}</td>"
            fila_html += f"<td>{fila.get('sabado', '')}</td>"
            fila_html += "</tr>"
            filas_html += fila_html
    html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
        <style>
           .horario-table {{
                border-collapse: collapse;
            }}
             .horario-table th, .horario-table td {{
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }}
    
    .container-tabla {{
        margin-top: 50px;
        display: table;
        width: 109%;
        
        border-collapse: collapse;
    }}
     .element-div {{
        display: table-cell;
        border: 1px solid #ddd;
        padding: 8px;
        text-align: center;
    }}  
    
     .container-periodo{{
        display: flex;
        margin-left: 80%;
        margin-top: 10px;
        font-weight: bolder;
    }} 
    .container-fecha{{
        display: flex;
        margin-top: -35%;
        margin-left: 80%;
    }}
     .date{{text-decoration: underline;
     margin-top:5%;
     margin-left:-10%;
     }}
     .title{{
        font-size: 25px;
        text-align: center;
        margin-bottom: 3%;
        text-decoration: underline;
        font-style: italic;
    }}
    img{{
        width: 150px;
        height: 100px;
        margin-left:-10px;
        
    }}
     .div-title{{
       
        width: 30%;
        text-align: center;
        margin-left: 18%;
      
        margin:0 auto;
        margin-top: -25%;
        line-height: 1.0;
        font-weight: bold;
    }}
    .horario-table th, .horario-table td {{
    border: 1px solid #ddd;
    padding: 8px;
    text-align: center;
    max-width: 10%; /* Ajusta el ancho máximo según tus necesidades */
}}
.horario-table {{
    border-collapse: collapse;
   
}}
.table-container,.horario-table{{
   
    width:50%;
    font-size:14px;
    
}}
        
   
    

        </style>
    </head>
    <body>
       <div class="container-img">
        <img src="{imagen_base64}" width="150px" height="80px">

    </div>
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
        <p class="fecha">Fecha de Impresión {fecha_formateada}</p>
    </div>
    <div class="container-periodo">
        <p>PERIODO:  <p class="date"> 2023-III</p> </p>
    </div>
<div class="contenedor">
    <div class="container-tabla">
        <div class="especialidad  element-div primerelemento">
            <p>Especialidad</p>
            <p><strong>{Especialidad}</strong></p>
        </div>
        <div class="semestre element-div segundoelemento">
            <p>Semestre</p>
            <p><strong>{Semestre}</strong></p>
        </div>
        <div class="turno element-div tercerelemento">
            <p>Turno</p>
            <p><strong>{Turno}</strong></p>
        </div>
        <div class="SECCION element-div cuartoelemento">
            <p>Sección</p>
            <p><strong>{Seccion}</strong></p>
        </div>
    </div>
    <div class="table-container">
        <table class="horario-table">
            <tr class="horario-header">
                <th>HORA</th>
                <th>LUNES</th>
                <th>MARTES</th>
                <th>MIERCOLES</th>
                <th>JUEVES</th>
                <th>VIERNES</th>
                <th>SABADO</th>
            </tr>
            {filas_html}
        </table>
        </div>
        </div>
        <!-- ... (contenido HTML posterior) ... -->
    </body>
    </html>
    
    """

    HTML(string=html).write_pdf(ruta_salida)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    class ImagePreviewer(QMainWindow):
        def __init__(self, pdf_path):
            super().__init__()

            self.pdf_path = pdf_path
            self.current_page = 0  # Página actual
            self.total_pages = 0   # Total de páginas en el PDF
            self.initUI()

        def initUI(self):
            self.setWindowTitle('Vista Previa de PDF')

            # Crear un widget central y un layout vertical
            central_widget = QWidget(self)
            self.setCentralWidget(central_widget)
            layout = QVBoxLayout(central_widget)

            # Crear un QLabel para mostrar la vista previa de la imagen
            self.image_label = QLabel(self)
            layout.addWidget(self.image_label)

            # Crear botones para navegar por las páginas
            btn_prev = QPushButton('Página Anterior', self)
            btn_prev.clicked.connect(self.showPreviousPage)
            layout.addWidget(btn_prev)
            
            btn_next = QPushButton('Página Siguiente', self)
            btn_next.clicked.connect(self.showNextPage)
            layout.addWidget(btn_next)
            btn_save = QPushButton('Guardar PDF', self)
            btn_save.clicked.connect(self.savePdf)
            layout.addWidget(btn_save)
            # Obtener el total de páginas en el PDF
            self.total_pages = self.getTotalPages(self.pdf_path)

            # Mostrar la primera página al iniciar la aplicación
            self.showPdfPreview()

        def showPdfPreview(self):
            # Cargar la imagen del PDF como vista previa en el QLabel
            pixmap = self.convertPdfPageToPixmap(self.pdf_path, self.current_page)

            # Mostrar la imagen en el QLabel
            self.image_label.setPixmap(pixmap)
            self.image_label.show()
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

        def savePdf(self):
            # Obtener el directorio actual como directorio inicial
            current_dir = os.path.dirname(os.path.realpath(__file__))

            # Abrir el cuadro de diálogo para seleccionar la ubicación y el nombre del archivo
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_dialog = QFileDialog()
            file_dialog.setOptions(options)
            file_dialog.setDirectory(current_dir)  # Establecer el directorio inicial
            file_path, _ = file_dialog.getSaveFileName(self, "Guardar PDF", "", "Archivos PDF (*.pdf);;Todos los archivos (*)")

            # Si el usuario eligió un archivo, guardar el PDF en esa ubicación
            if file_path:
                # Agregar el prefijo file:// en sistemas Linux
                if sys.platform.startswith('linux'):
                    file_path = 'file://' + file_path
                crear_pdf(ruta_salida=file_path)

    ruta_salida = '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/waos.pdf'
    crear_pdf(ruta_salida=ruta_salida)

    ex = ImagePreviewer(pdf_path=ruta_salida)
    ex.setGeometry(100, 100, 800, 600)
    ex.show()

    sys.exit(app.exec_())
