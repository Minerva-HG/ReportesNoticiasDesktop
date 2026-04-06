from threading import Thread
from limpieza import limpiar
from fuentes import obtener_noticias
from generadores import crear_documentos
from redactor import redactar_por_bloques
from ui import VentanaProgreso
from config import BLOQUES

def proceso_largo(ui):
    limpiar()
    noticias = obtener_noticias()

    def tarea(bloque):
        crear_documentos(noticias)

    redactar_por_bloques(
        tarea_por_bloque=tarea,
        callback_ui=ui.actualizar
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
