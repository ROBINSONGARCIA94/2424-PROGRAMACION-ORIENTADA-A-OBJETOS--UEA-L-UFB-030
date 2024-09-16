import tkinter as tk
from tkinter import messagebox, Listbox, Scrollbar

# Función para agregar información a la lista
def agregar_info():  
    info = entrada_texto.get()
    if info:
        lista_datos.insert(tk.END, info)
        entrada_texto.delete(0, tk.END)  # Limpiar el campo de texto
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingrese información.")

# Función para limpiar la lista
def limpiar_lista():
    lista_datos.delete(0, tk.END)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Aplicación GUI Básica")

# Crear un marco para la entrada de datos
marco_entrada = tk.Frame(ventana)
marco_entrada.pack(pady=10)

# Etiqueta para el campo de texto
etiqueta = tk.Label(marco_entrada, text="Ingrese información:")
etiqueta.pack(side=tk.LEFT)

# Campo de texto
entrada_texto = tk.Entry(marco_entrada, width=30)
entrada_texto.pack(side=tk.LEFT)

# Botón "Agregar"
boton_agregar = tk.Button(marco_entrada, text="Agregar", command=agregar_info)
boton_agregar.pack(side=tk.LEFT)

# Botón "Limpiar"
boton_limpiar = tk.Button(marco_entrada, text="Limpiar", command=limpiar_lista)
boton_limpiar.pack(side=tk.LEFT)

# Lista para mostrar datos
lista_datos = Listbox(ventana, width=50, height=10)
lista_datos.pack(pady=10)

# Barra de desplazamiento para la lista
scrollbar = Scrollbar(ventana)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configurar la lista para usar la barra de desplazamiento
lista_datos.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=lista_datos.yview)

# Ejecutar la aplicación
ventana.mainloop()