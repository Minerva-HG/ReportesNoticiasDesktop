import json
import os

ARCHIVO_ESTADO = "output/cache/estado.json"

def guardar_estado(datos):
    os.makedirs("output/cache", exist_ok=True)
    with open(ARCHIVO_ESTADO, "w", encoding="utf-8") as f:
        json.dump(datos, f)

def cargar_estado():
    if not os.path.exists(ARCHIVO_ESTADO):
        return None
    with open(ARCHIVO_ESTADO, "r", encoding="utf-8") as f:
        return json.load(f)

def limpiar_estado():
    if os.path.exists(ARCHIVO_ESTADO):
        os.remove(ARCHIVO_ESTADO)