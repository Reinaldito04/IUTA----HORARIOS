from weasyprint import HTML
import os
import base64
import sqlite3
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



def recuperar_datos_bd(carrera,sesion):
    conexion = sqlite3.connect("db/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT Dia, Hora, CodigoMat, CodigoAula, CedulaProf FROM HorarioTest WHERE Carrera=? AND Sesion=?", (carrera, sesion))
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base
    
    
def crear_pdf( ruta_salida,carrera,sesion):
    imagen_url = 'https://www.eduopinions.com/wp-content/uploads/2018/02/Instituto-Universitario-de-Tecnolog%C3%ADa-de-Administraci%C3%B3n-Industrial-IUTA-logo-350x181.gif'
    
    imagen_base64 = image_url_to_base64(imagen_url)
    Especialidad = f'{carrera}'
    Semestre = f'{sesion}'
    Turno = 'Diurno'
    Seccion ='Unica'
    
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    print("Fecha actual:", fecha_formateada)
    if imagen_base64:
        # Definir los datos de la tabla
        datos_base = recuperar_datos_bd(carrera,sesion)        
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
    # Obtén tus datos desde la base de datos
   
    # Llamada a la función con tus datos y ruta de salida
    ruta_salida = '/home/reinaldo/Documentos/dev/IUTA----HORARIOS/ui/waos.pdf'
    crear_pdf( carrera="hola",sesion="icomo", ruta_salida=ruta_salida)
