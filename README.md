# 📊 Reporte Ejecutivo Diario Automatizado

Sistema de escritorio desarrollado en **Python** para **Windows**, que genera **reportes empresariales diarios** en **Word y Excel**, a partir de **datos reales (noticias públicas)**, mostrando **progreso visual** durante su ejecución.

El proceso está diseñado para **simular una redacción prolongada (~6 horas)** y se reinicia automáticamente cada día eliminando la información previa.

---

## ✅ Funcionalidades principales

- 📄 Genera **reporte en Word (.docx)**
- 📊 Genera **reporte en Excel (.xlsx)**
- 🌐 Obtiene **datos reales** desde fuentes públicas (RSS)
- 🕒 Simula un proceso largo por bloques
- 📈 Muestra **barra de progreso visual**
- 🗑️ Limpieza automática del reporte anterior
- 🇪🇸 Reportes en **español**
- 🖥️ Funciona en **Windows**
- 🚫 No requiere Google Scraping (legal y estable)

---

## 🧰 Requisitos del sistema

Antes de comenzar, necesitas:

- ✅ Windows 10 o superior  
- ✅ Python 3.9 o superior  
- ✅ Conexión a Internet (para obtener noticias)

---

## 🐍 Instalación de Python

1. Descarga Python desde:
   👉 https://www.python.org/downloads/windows/

2. Durante la instalación:
   - ✅ Marca la opción: **“Add Python to PATH”**

3. Verifica la instalación:
   ```bat
   python --version
---
en CMD
cd C:\Reportes_Automaticos
python -m venv venv
venv\Scripts\activate

pip install python-docx openpyxl feedparser schedule requests


---
4. 📁 Estructura del proyecto
La carpeta del proyecto debe verse así:
Reportes_Automaticos/
└── app/
    ├── main.py
    ├── ui.py
    ├── fuentes.py
    ├── redactor.py
    ├── generadores.py
    ├── limpieza.py
    ├── config.py
    └── output/
        ├── cache/
        └── reportes/

-- Todos los archivos .py deben estar dentro de la carpeta app

5. nstalación de dependencias
Abre una ventana de Símbolo del sistema (CMD) y ejecuta:
pip install python-docx openpyxl feedparser

6. cd C:\Reportes_Automaticos\app
  python main.py

🖥️ ¿Qué verás al ejecutarlo?

Se abre una ventana de progreso
Muestra:

Porcentaje de avance
Bloque actual


La barra avanza automáticamente
El proceso puede tardar varias horas (configurable)

✅ Puedes minimizar la ventana
✅ El proceso sigue ejecutándose en segundo plano

7.  Dónde se guardan los reportes
Al finalizar, los archivos se generan en:
app/output/reportes/

Ejemplo:

reporte_2026-04-06.docx
reporte_2026-04-06.xlsx

8. 🔄 Limpieza automática
Cada vez que se inicia el sistema:

Se eliminan reportes anteriores
Se limpian archivos temporales (cache)

Esto evita acumulación de archivos y errores.

9. ⏱️ Configuración del tiempo del proceso
En el archivo config.py puedes modificar:

PythonDURACION_HORAS = 6   # horas totales del procesoBLOQUES = 12        # número de pasos (progreso)Mostrar más líneas
Ejemplo:

6 horas / 12 bloques = 1 bloque cada 30 minutos 

10. 🔟 EJECUCIÓN AUTOMÁTICA DIARIA (WINDOWS)
✅ PASOS EN Task Scheduler

Abrir Programador de tareas
Crear tarea básica
Nombre:
Reporte Diario Automático
Frecuencia: Diaria
Acción → Iniciar programa
Programa:

C:\Reportes_Automaticos\venv\Scripts\python.exe


Argumentos:

C:\Reportes_Automaticos\app\main.py


Iniciar en:

C:\Reportes_Automaticos\app

✅ Se ejecuta solo
✅ No necesitas abrir nada
✅ Corre incluso sin sesión abierta