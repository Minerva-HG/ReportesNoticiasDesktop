import time
from config import DURACION_HORAS, BLOQUES

def redactar_por_bloques(tarea_por_bloque, callback_ui=None):
    total_segundos = DURACION_HORAS * 60 * 60
    pausa = total_segundos / BLOQUES

    for bloque in range(1, BLOQUES + 1):
        tarea_por_bloque(bloque)

        if callback_ui:
            callback_ui(bloque, "Redactando reporte...")

        time.sleep(pausa)