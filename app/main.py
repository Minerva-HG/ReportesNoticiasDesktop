from threading import Thread
from datetime import datetime
import time

from limpieza import limpiar
from fuentes import obtener_noticias
from generadores import crear_documentos
from redactor import redactar_por_bloques
from ui import VentanaProgreso
from email_sender import enviar_correo
from config import BLOQUES, INTERVALO_ENVIO_HORAS


def cargar_template_html():
    with open("email_template.html", "r", encoding="utf-8") as f:
        return f.read()


def proceso_largo(ui):
    limpiar()
    noticias = obtener_noticias()
    html = cargar_template_html()

    ultima_hora_envio = time.time()

    def tarea(bloque):
        nonlocal ultima_hora_envio

        ui.actualizar(bloque, "Procesando información...")

        ahora = time.time()
        if ahora - ultima_hora_envio >= INTERVALO_ENVIO_HORAS * 3600:
            fecha = datetime.now().strftime("%Y-%m-%d")
            archivos = [
                f"output/reportes/reporte_{fecha}.docx",
                f"output/reportes/reporte_{fecha}.xlsx"
            ]

            enviar_correo(
                asunto="Reporte Ejecutivo Diario (Avance)",
                html_body=html,
                archivos_adjuntos=archivos
            )

            ultima_hora_envio = ahora

    redactar_por_bloques(
        tarea_por_bloque=tarea,
        callback_ui=None
    )

    # ✅ Generar reporte final
    crear_documentos(noticias)

    fecha = datetime.now().strftime("%Y-%m-%d")
    enviar_correo(
        asunto="Reporte Ejecutivo Diario (Final)",
        html_body=html,
        archivos_adjuntos=[
            f"output/reportes/reporte_{fecha}.docx",
            f"output/reportes/reporte_{fecha}.xlsx"
        ]
    )

    ui.finalizar()


if __name__ == "__main__":
    ui = VentanaProgreso(BLOQUES)

    hilo = Thread(
        target=proceso_largo,
        args=(ui,),
        daemon=True
    )

    hilo.start()
    ui.iniciar()