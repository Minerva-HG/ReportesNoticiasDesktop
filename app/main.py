from threading import Thread
from datetime import datetime
import time

from limpieza import limpiar
from fuentes import obtener_noticias
from generadores import crear_documentos
from ui import VentanaProgreso
from email_sender import enviar_correo
from estado import guardar_estado, cargar_estado, limpiar_estado
from config import (
    DOCUMENTOS_TOTALES,
    INTERVALO_DOCUMENTOS_MIN,
    INTERVALO_ENVIO_HORAS
)

def cargar_template_html():
    with open("email_template.html", "r", encoding="utf-8") as f:
        return f.read()

def proceso_largo(ui):
    estado = cargar_estado()
    html = cargar_template_html()
    noticias = obtener_noticias()

    if estado:
        inicio = estado["documento_actual"]
        ultima_hora_envio = estado["ultima_hora_envio"]
    else:
        limpiar()
        inicio = 1
        ultima_hora_envio = time.time()

    archivos_generados = []

    for i in range(inicio, DOCUMENTOS_TOTALES + 1):
        ui.actualizar(i, f"Generando documento {i} de {DOCUMENTOS_TOTALES}")

        word, excel = crear_documentos(noticias, f"doc{i}")
        archivos_generados.extend([word, excel])

        guardar_estado({
            "documento_actual": i + 1,
            "ultima_hora_envio": ultima_hora_envio
        })

        ahora = time.time()
        if ahora - ultima_hora_envio >= INTERVALO_ENVIO_HORAS * 3600:
            enviar_correo(
                asunto="Reporte Ejecutivo Diario (Avance)",
                html_body=html,
                archivos_adjuntos=archivos_generados
            )
            ultima_hora_envio = ahora

        time.sleep(INTERVALO_DOCUMENTOS_MIN * 60)

    enviar_correo(
        asunto="Reporte Ejecutivo Diario (Final)",
        html_body=html,
        archivos_adjuntos=archivos_generados
    )

    limpiar_estado()
    ui.finalizar()

if __name__ == "__main__":
    ui = VentanaProgreso(DOCUMENTOS_TOTALES)

    hilo = Thread(
        target=proceso_largo,
        args=(ui,),
        daemon=True
    )

    hilo.start()
    ui.iniciar()