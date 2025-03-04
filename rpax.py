"""
     CODIGO PARA USO EN CASOS/FORMS DE TRANACT
| ..PRUEBA RPA EN PYTHON. USO DE VISION Y TABLE.. |
:: Realiza una lectura de la página
:: Realiza una lectura de archivos csv
:: Realiza un print con la información buscada
Hecho por Felipe.
"""
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#....STACK....
import rpa as r #el unico e inigualable
import os #..en caso de abrir archivos y ocupar funcs os /(quizas podria guardar una lista con los resultados de los links)
import csv #..pa leer csv
import requests
import pandas as pd
import logging
from fpdf import FPDF
import webbrowser #para abrir el pdf despues

# ....init RPA....
r.init(visual_automation = True)

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

# ..clase para formatear pdf
class PDF(FPDF):
    def header(self):
        # ..encabezado->
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Detalle de Lecturas de Transparencia', 0, 1, 'C')
        self.ln(10)

    def footer(self):
        # ..pie de pagina->
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def title_seccion(self, title):
        # ..titulo de seccion->
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, 0, 1)
        self.ln(5)

    def title_contenido(self, content):
        # ..contenido gen->
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, content)
        self.ln(8)
        
        
# ..crear una instancia de FPDF
pdf = FPDF()
pdf.set_auto_page_break(auto=True, margin=15)
pdf.add_page()

# ..función para agregar texto al PDF
def agregar_a_pdf(texto):
    pdf.set_font("Arial", size=10)
    pdf.multi_cell(0, 10, texto)
    
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.| 
# ..metodo de lectura de csv | analisis de 'http':

# ..se lee el archivo CSV
def lectura():
    print('Se procede a leer archivo un archivo CSV/Carpeta')
    agregar_a_pdf('Se procede a leer archivo un archivo CSV/Carpeta:')
    try:
        df = pd.read_csv("TransparenciaActiva.csv", encoding='latin1', sep=';')
        print('Leyendo campos que contienen "http"...')
        agregar_a_pdf('Leyendo campos que contienen "http"...')
        
        for index, row in df.iterrows():
            for col in df.columns:
                enlace = row[col]
                # ..caso 1: Verificar si el enlace contiene "..pdf"
                if isinstance(enlace, str) and '..pdf' in enlace:
                    mensaje = f"Error en fila {index + 1}, columna '{col}': Enlace contiene '..pdf' - {enlace}"
                    print(mensaje)
                    agregar_a_pdf(mensaje)
                
                # ..caso 2: Verificar si el enlace está incompleto
                if isinstance(enlace, str) and enlace.rstrip('/').endswith('TransparenciaRengo/clientes/1/nuevos/2025'):
                    mensaje = f"Error en fila {index + 1}, columna '{col}': Enlace incompleto - {enlace}"
                    print(mensaje)
                    agregar_a_pdf(mensaje)
        
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        agregar_a_pdf(f"Error al leer el archivo CSV: {e}")
    print('Se termina esta lectura. \n')
    agregar_a_pdf('Se termina esta lectura. \n')
    agregar_a_pdf(' ')      

# ..función para guardar el PDF al final de todas las lecturas
def guardar_pdf():
    pdf.output("detalle_lecturas.pdf")
    print('PDF generado con todos los detalles de las lecturas.')

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 4

# ..movimiento a la pag de honorarios municipal
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
r.wait()

agregar_a_pdf('CARPETA 4 - HONORARIOS | MUNICIPAL')      
print('Se empieza a leer el archivo de honorarios del sector de MUNICIPAL:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

# ..movimiento a la pag de educacion
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
r.click('A6428:formInfo:j_idt76:1:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 4 - HONORARIOS | EDUCACION')   
print('Se empieza a leer el archivo de honorarios del sector de EDUCACION:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

# ..movimiento a la pag de educacion
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
r.click('A6428:formInfo:j_idt76:2:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 4 - HONORARIOS | SALUD')   
print('Se empieza a leer el archivo de honorarios del sector de SALUD:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 5

# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:4:j_idt43:2:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:1:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:0:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 5 - CONTRATACIONES DE BIENES | MENORES A 3UTM | MUNICIPAL')   
print('Se empieza a leer la carpeta 5:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|


#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 5

# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:4:j_idt43:2:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:1:j_idt78')
r.click('A6428:formInfo:j_idt94:1:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:0:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 5 - CONTRATACIONES DE BIENES | MENORES A 3UTM | EDUCACION')   
print('Se empieza a leer la carpeta 5:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#baja inmueble
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:0:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | BAJA INMUEBLE')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:1:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | COMETIDOS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:2:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | COMPRAS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:3:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | CONCEJO MUNICIPAL')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:4:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | CONTRATOS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:5:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | COSOC')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:6:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | DEVOLUCION')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:7:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | ESTADO DE PAGO')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:8:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | LICITACION')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:9:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | MODIFICACION PRESUPUESTARIA')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:10:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | OTORGA APORTE')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:11:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | PATENTE')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:12:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | PISCINA')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:13:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | PLAN DE COMPRAS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:14:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | PROGRAMAS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:15:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | PROYECTOS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:16:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | REINTEGRA')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:17:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | TRATOS DIRECTOS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 7
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:0:datalist:6:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt126:18:j_idt127')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 7 - ACTOS Y RESOLUCIONES | DECRETOS ALCALDICIOS | VEHICULOS')   
print('Se empieza a leer la carpeta 7:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Propios | Alimentos') 
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:1:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Propios | Asistencialidad')   
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:1:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Propios | Ayudas Medicas')   
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:2:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Propios | Cajas Chicas')   
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:2:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Propios | Incendios')   
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:0:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:3:j_idt111')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Propios | Servicios Funerarios')   
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 9
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:1:j_idt43:1:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 9 - Subsidios y Beneficios Intermediarios | Enero')   
print('Se empieza a leer la carpeta 9:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 10
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:2:j_idt43:2:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:0:j_idt78')
r.click('A6428:formInfo:j_idt200')
r.wait()

agregar_a_pdf('CARPETA 10 - Consejo consultivo | COSOC')   
print('Se empieza a leer la carpeta 10:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#-.-.-.-.-.-.-.-.-.-.-.-.-.-.-. CARPETA 10
#cometidos
# ..movimiento a la pag de acta de evaluacion
r.url('https://www.portaltransparencia.cl/PortalPdT/directorio-de-organismos-regulados/?org=MU266')
r.click(900, 300)
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
r.keyboard('[down][down][down][down][down]')
#r.click('Actas de evaluación de comisiones evaluadoras de licitaciones y compras públicas')  # <button class="citation-flag" data-index="8">
r.click('A6428:formInfo:j_idt39:1:datalist:2:j_idt43:2:j_idt47')
#r.click(510,500)
r.click('A6428:formInfo:j_idt76:2:j_idt78')
r.click('A6428:formInfo:j_idt94:0:j_idt95')
r.click('A6428:formInfo:j_idt110:0:j_idt111')
r.wait()

agregar_a_pdf('CARPETA 10 - Consejo consultivo | Escolar')   
print('Se empieza a leer la carpeta 10:')
print('* Si no se encuentra nada (ningun error), así lo indicara.')
lectura()
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|

#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|


#|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|.|
# ..metodo de lectura de csv | analisis de columna especifica:

"""
print('Se procede a leer archivo un nuevo csv de honorarios.')
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

print('proceso finalizado.')
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

# ....se cierra RPA....
guardar_pdf()
print('Se finaliza todo el proceso.')
r.close()
print('Se abre el archivo detallado:')
webbrowser.open_new(r'detalle_lecturas.pdf')