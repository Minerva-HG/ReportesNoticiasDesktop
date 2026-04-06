import shutil
import os

def limpiar():
    rutas = ["output/cache", "output/reportes"]

    for ruta in rutas:
        if os.path.exists(ruta):
            shutil.rmtree(ruta)
        os.makedirs(ruta)