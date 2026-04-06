from docx import Document
from openpyxl import Workbook
from datetime import datetime
from config import EMPRESA, AUTOR

def crear_documentos(noticias):
    fecha = datetime.now().strftime("%Y-%m-%d")

    doc = Document()
    wb = Workbook()
    ws = wb.active

    doc.add_heading(EMPRESA, level=1)
    doc.add_paragraph(f"Fecha: {fecha}")
    doc.add_paragraph(f"Autor: {AUTOR}")

    ws.append(["Título", "Resumen"])

    for i, noticia in enumerate(noticias, 1):
        doc.add_heading(f"{i}. {noticia['titulo']}", level=2)
        doc.add_paragraph(noticia["resumen"])

        ws.append([noticia["titulo"], noticia["resumen"]])

    ruta_word = f"output/reportes/reporte_{fecha}.docx"
    ruta_excel = f"output/reportes/reporte_{fecha}.xlsx"

    doc.save(ruta_word)
    wb.save(ruta_excel)