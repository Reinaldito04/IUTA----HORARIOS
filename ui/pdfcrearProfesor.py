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



def recuperar_datos_bd(profesor):
    conexion = sqlite3.connect("db/database.db")
    cursor = conexion.cursor()
    cursor.execute("SELECT Dia, Hora, CodigoMat, CodigoAula, CedulaProf FROM HorarioTest WHERE CedulaProf=?", (profesor,))
    datos_base = cursor.fetchall()
    cursor.close()
    return datos_base
    
def recuperarordenHorasDB(turno):
    conexion = sqlite3.connect("db/database.db")
    cursor=conexion.cursor()
    cursor.execute("SELECT Descripcion FROM Modulo WHERE Turno =?",(turno,))
    horasDb= cursor.fetchall()
    cursor.close()
    return  horasDb
    


def obtener_hora_y_pm(hora):
    partes = hora.split(" ")
    hora_sin_am_pm = partes[0]
    es_pm = "PM" in hora
    return hora_sin_am_pm, es_pm

# Función personalizada para la clave de ordenación
def clave_ordenacion(fila):
    es_pm = obtener_hora_y_pm(fila['hora'])[1]
    if es_pm:
        return (1, fila['hora'])
    else:
        return (0, fila['hora'])
    
def convertir_formato_hora(hora):
    try:
        # Separar la hora de la parte 'A' o 'P' (AM o PM)
        hora_parts = hora.split('A') if 'A' in hora else hora.split('P')
        if len(hora_parts) == 2:
            # Unir la hora y la parte 'A' o 'P' sin espacios adicionales
            hora_objeto = datetime.strptime(f"{hora_parts[0].strip()} {hora_parts[1].strip()}", "%I:%M %p").strftime("%I:%M %p")
            return hora_objeto
    except ValueError:
        pass
    # Si no se puede convertir, devolver la cadena original
    return hora


def crear_pdf( ruta_salida,profesor,periodo,Turno):
    imagen_url = 'https://www.eduopinions.com/wp-content/uploads/2018/02/Instituto-Universitario-de-Tecnolog%C3%ADa-de-Administraci%C3%B3n-Industrial-IUTA-logo-350x181.gif'
    
    imagen_base64 = image_url_to_base64(imagen_url)
  
    Turno = f'{Turno}'
    periodo =f'{periodo}'
    profesorTexto =f'{profesor}'
    fecha_actual = datetime.now()
    fecha_formateada = fecha_actual.strftime("%Y-%m-%d")

    print("Fecha actual:", fecha_formateada)
    if imagen_base64:
        # Definir los datos de la tabla
       

        datos_base = recuperar_datos_bd(profesor)        
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
        horas_db = [fila['hora'] for fila in filas_datos]
        filas_datos = sorted(filas_datos, key=lambda x: horas_db.index(x['hora']) if x['hora'] in horas_db else float('inf'))


        filas_html = ""
        for fila in filas_datos:
            fila_html = "<tr>"
            fila_html += f"<td>{fila.get('hora', '')}</td>"
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
            .div-img {{
        margin-left: 20px;
      }}
      .img {{
        width: 80px;
        height: 80px;
      }}
      .container-fecha {{
        margin-top: -10px;
        margin-left: 20px;
        font-weight: bolder;
      }}
      h2 {{
        text-align: center;
        text-decoration: underline;
      }}
      .container {{
        width: 90%;
        margin-left: 20px;
        display: flex;
        font-weight: bolder;
        justify-content: space-between;
      }}
      /* Estilos para la tabla */
      table {{
        max-width: 500px;
       
        border-collapse: collapse;
        font-size:16px;
        margin-top: 20px; /* Ajusta el margen superior según sea necesario */
    }}
    
    /* Estilos para las filas del encabezado */
    tr.horario-header th {{
        border: 1px solid #ddd; /* Borde para las celdas del encabezado */
        padding: 8px;
        text-align: center;
    }}
    
    /* Estilos para celdas normales */
    td {{
        border: 1px solid #ddd; /* Borde para las celdas normales */
        padding: 8px;
        text-align: center;
    }}
 
    

        </style>
    </head>
    <body>
    <div class="container-title">
    
   <h2>HORARIO INDIVIDUAL DE DOCENTE</h2>
    </div>
       <div class="div-img">
      <img
        class="img"
        src="{imagen_base64}" />
      <div class="container-fecha">
        <p>Fecha de Impresion : {fecha_formateada}</p>
      </div>
      <div class="container">
        <div class="container-docente">
          <p>DOCENTE: {profesorTexto} </p>
        </div>
        <div class="container-periodo">
          <p>PERIODO : {periodo}</p>
        </div>
      </div>
    </div>
 
   
    <div class="tabla">
    
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
   <br>
    <div class="container-fecha">
        <p>Total de Horas :</p>
    </div>
    <br>

    <div class="container-fecha">
        <P>Nota: ESTE HORARIO ESTA SUJETO A LA MATRICULA.</P>
    </div>
    <div class="container-fecha">
        <P>RECIBIDO Y CONFORME _________________________</P>
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
