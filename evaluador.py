# Importamos tkinter para crear ventanas
import tkinter as tk
from tkinter import messagebox

# Funcion que calcula el resultado de la calificacion
def evaluar_calificacion():
    try:
        nota = float(entrada.get())

        if nota >= 90:
            resultado = "Excelente"
        elif nota >= 80:
            resultado = "Muy bueno"
        elif nota >= 70:
            resultado = "Bueno"
        else:
            resultado = "Necesita mejorar"

        messagebox.showinfo("Resultado", f"La calificacion es: {resultado}")

    except ValueError:
        messagebox.showerror("Error", "Por favor ingrese un numero valido")


# Creamos la ventana principal
ventana = tk.Tk()
ventana.title("Evaluador de Calificaciones")
ventana.geometry("300x200")
ventana.resizable(False, False)

# Etiqueta
etiqueta = tk.Label(
    ventana,
    text="Ingrese la calificacion:",
    font=("Arial", 13)
)
etiqueta.pack(pady=15)

# Cuadro para escribir la calificacion
entrada = tk.Entry(
    ventana,
    font=("Arial", 14),
    justify="center"
)
entrada.pack(pady=5)

# Boton para calcular
boton = tk.Button(
    ventana,
    text="Evaluar",
    font=("Arial", 13),
    command=evaluar_calificacion,
    bg="#4CAF50",
    fg="white"
)
boton.pack(pady=20)

# Iniciamos la ventana
ventana.mainloop()