import tkinter as tk
from tkinter import ttk

class VentanaProgreso:
    def __init__(self, total_bloques):
        self.total = total_bloques

        self.root = tk.Tk()
        self.root.title("Reporte Ejecutivo Diario")
        self.root.geometry("420x220")
        self.root.resizable(False, False)

        tk.Label(
            self.root,
            text="Generación de Reporte Empresarial",
            font=("Segoe UI", 12, "bold")
        ).pack(pady=10)

        self.progreso = tk.IntVar()

        self.barra = ttk.Progressbar(
            self.root,
            length=350,
            maximum=100,
            variable=self.progreso
        )
        self.barra.pack(pady=10)

        self.lbl_estado = tk.Label(
            self.root,
            text="Iniciando proceso...",
            font=("Segoe UI", 9)
        )
        self.lbl_estado.pack()

        self.lbl_bloque = tk.Label(
            self.root,
            text=f"Bloque 0 de {self.total}",
            font=("Segoe UI", 9)
        )
        self.lbl_bloque.pack(pady=5)

    def actualizar(self, bloque_actual, mensaje="Procesando datos..."):
        porcentaje = int((bloque_actual / self.total) * 100)
        self.progreso.set(porcentaje)
        self.lbl_bloque.config(
            text=f"Bloque {bloque_actual} de {self.total}"
        )
        self.lbl_estado.config(text=mensaje)
        self.root.update_idletasks()

    def finalizar(self):
        self.progreso.set(100)
        self.lbl_estado.config(text="Reporte finalizado correctamente")

    def iniciar(self):
        self.root.mainloop()