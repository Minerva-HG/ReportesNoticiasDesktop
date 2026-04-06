from docx import Document
from openpyxl import Workbook
from docx import Document
from openpyxl import Workbook
from datetime import datetime
from config import EMPRESA, AUTOR

def crear_documentos(noticias):
    fecha = datetime.now().strftime("%Y-%m-%d")

    doc = Document()
    wb = Workbook()
    ws = wb.active

    # ENCABEZADO
    doc.add_heading(EMPRESA, level=1)
    doc.add_paragraph(f"Fecha: {fecha}")
    doc.add_paragraph(f"Autor: {AUTOR}")

    doc.add_heading("Resumen Ejecutivo", level=2)
    doc.add_paragraph(
        "El presente documento contiene un análisis general de información relevante obtenida de fuentes públicas, con el objetivo de mantener visibilidad sobre el entorno informativo actual."
    )

    ws.append(["Título", "Resumen"])

    doc.add_heading("Noticias y Análisis Relevante", level=2)

    for i, noticia in enumerate(noticias, 1):
        doc.add_heading(f"{i}. {noticia['titulo']}", level=3)
        doc.add_paragraph(noticia["resumen"])

        ws.append([noticia["titulo"], noticia["resumen"]])

    doc.add_heading("Conclusión", level=2)
    doc.add_paragraph(
        "No se identifican incidencias críticas al cierre del análisis. Se recomienda continuar con el monitoreo periódico."
    )

    doc.save(f"output/reportes/reporte_{fecha}.docx")
    wb.save(f"output/reportes/reporte_{fecha}.xlsx")