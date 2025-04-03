"""
     CODIGO PARA USO EN EL CASO DE HONORARIOS
| ..PRUEBA RPA EN PYTHON. USO DE VISION Y TABLE.. |
:: Realiza una lectura de la página
:: Realiza una lectura de archivos csv
:: Realiza un print con la información buscada
Hecho por Felipe. (FECORO)
"""
#....STACK....
import rpa as r #el unico e inigualable
import os #..en caso de abrir archivos y ocupar funcs os /(quizas podria guardar una lista con los resultados de los links)
import csv #..pa leer csv
import requests
import pandas as pd

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
# ..init
r.init(visual_automation = True)

# ..movimiento a la pag
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.click('A6428:formInfo:j_idt39:0:datalist:3:j_idt43:4:j_idt47')
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt200')

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
# ..metodo de lectura de csv | analisis de 'http':

# ..se lee el archivo CSV
print('Se procede a leer archivo CSV de honorarios.')
try:
    df = pd.read_csv("TransparenciaActiva.csv", encoding='latin1', sep=';')
    print('Leyendo campos que contienen "http"...')

    # ..busca columnas que contengan algún valor con "http"
    http_columns = [col for col in df.columns if any(df[col].astype(str).str.contains('http', na=False))]

    if not http_columns:
        print('Error: No se encontraron columnas que contengan enlaces (http/https).')
    else:
        print(f"Columnas con enlaces encontradas: {http_columns}")

        # ..itera sobre cada columna que contiene enlaces
        for col in http_columns:
            print(f"Procesando columna: {col}")
            for index, row in df.iterrows():
                enlace = row[col]

                # ..caso 1: Verificar si el enlace contiene "..pdf"
                if isinstance(enlace, str) and '..pdf' in enlace:
                    print(f"Error en fila {index + 1}, columna '{col}': Enlace contiene '..pdf' - {enlace}")

                # ..caso 2: Verificar si el enlace está incompleto (solo contiene la carpeta base)
                if isinstance(enlace, str) and enlace.rstrip('/').endswith('TransparenciaRengo/clientes/1/nuevos/2025'):
                    print(f"Error en fila {index + 1}, columna '{col}': Enlace incompleto - {enlace}")

                # ..se verifica si el enlace es funcional
                if isinstance(enlace, str) and enlace.startswith(('http://', 'https://')):
                    try:
                        response = requests.get(enlace, timeout=10)
                        if response.status_code != 200:
                            print(f"Error en fila {index + 1}, columna '{col}': Enlace no funcional ({response.status_code}) - {enlace}")
                    except Exception as e:
                        print(f"Error en fila {index + 1}, columna '{col}': No se pudo acceder al enlace - {enlace} ({str(e)})")

except FileNotFoundError:
    print("Error: Archivo 'TransparenciaActiva.csv' no encontrado.")
except Exception as e:
    print(f"Error inesperado: {str(e)}")

print('Proceso finalizado.')

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
# ..metodo de lectura de csv | analisis de columna especifica:

"""
print('Se procede a leer archivo csv de honorarios.')
df = pd.read_csv("TransparenciaActiva.csv", encoding='latin1', sep=';')

# ..marcamos que se esta leyendo
print('leyendo columna "Enlace funciones desarrolladas"...')

# ..se verifica que la columna existe
if 'Enlace funciones desarrolladas' not in df.columns:
    print('Error: La columna "Enlace funciones desarrolladas" no existe en el archivo CSV.')
else:
    # ..iteramos sobre cada fila de la columna
    for index, row in df.iterrows():
        enlace = row['Enlace funciones desarrolladas']
        
        # ..caso 1: Verificar si el enlace contiene "..pdf"
        if isinstance(enlace, str) and '..pdf' in enlace:
            print(f"Error en fila {index + 1}: Enlace contiene '..pdf' - {enlace}")

        # ..caso 2: Verificar si el enlace está incompleto (solo contiene la carpeta base)
        if isinstance(enlace, str) and enlace.rstrip('/').endswith('TransparenciaRengo/clientes/1/nuevos/2025'):
            print(f"Error en fila {index + 1}: Enlace incompleto - {enlace}")

        # ..opcional: Verificar si el enlace es funcional
        if isinstance(enlace, str) and enlace.startswith(('http://', 'https://')):
            try:
                response = requests.get(enlace, timeout=10)
                if response.status_code != 200:
                    print(f"Error en fila {index + 1}: Enlace no funcional ({response.status_code}) - {enlace}")
            except Exception as e:
                print(f"Error en fila {index + 1}: No se pudo acceder al enlace - {enlace} ({str(e)})")

print('Proceso finalizado.')
"""

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#..metodo de lectura directa:

"""
# ..localizamos la tabla que contiene la palabra "Enlace"
r.table('Enlace', 'in')  # Busca la tabla que contiene la palabra "Enlace"

# ..extraer todos los hipervínculos de la columna "Enlace"
links = []
for row in r.table_row():
    enlace = r.read(f"{row}|Enlace")  # Lee el valor de la columna "Enlace" en cada fila
    if enlace and enlace.startswith(('http://', 'https://')):
        links.append(enlace)

# ..se verifica que los enlaces están funcionales
for link in links:
    try:
        response = requests.get(link, timeout=10)
        if response.status_code == 200:
            print(f"Enlace funcional: {link}")
        else:
            print(f"Enlace error ({response.status_code}): {link}")
    except Exception as e:
        print(f"Error al acceder al enlace {link}: {str(e)}")

# ..fotinha
r.snap('page', 'results.png')
"""

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#ejemplo:
#result_locator = "Enlace"
#search_results = browser.find_elements(result_locator)
#for element_index in range(1,len(search_results):
    # hacer algo
    

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
# ..se cierra RPA
r.close()
