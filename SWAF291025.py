# Importamos las librerías necesarias
import tkinter as tk
from tkinter import messagebox

# Función que se ejecuta al presionar el botón
def registrar_usuario():
    nombre = entry_nombre.get()
    edad = entry_edad.get()
    correo = entry_correo.get()

    if nombre == "" or edad == "" or correo == "":
        messagebox.showinfo("Error", "Por favor completa todos los campos")
    else:
        messagebox.showinfo("Registro existoso",f"Bienvenido {nombre} tu registro a sido existoso.")
        ventana_registro.destroy()
        print("Abrir ventana del test...")


# ventana de registro
ventana_registro= tk.Tk ()
ventana_registro.title("Registro de Usuario")
ventana_registro.config(bg="#3F779D")
ventana_registro.geometry("600x400")

#titulo
titulo = tk.Label(
    ventana_registro,
    text= "REGISTRO DE USUARIO",
    font=("Arial", 18, "bold"),
    bg="#080708",
    fg="#FAF0FA",
    wraplength=500,
    justify="center",
)
titulo.pack(pady=20)

#nombre
tk.Label(ventana_registro, text="correo electronico:", font=("Arial", 12),bg="#3F779D", fg="white" ).pack(pady=5)
entry_nombre = tk.Entry(ventana_registro, font=("Arial", 12))
entry_nombre.pack()

# Edad
tk.Label(ventana_registro, text="Edad: ", font=("Arial", 12),bg="#3F779D", fg="white").pack(pady=5)
entry_edad = tk.Entry(ventana_registro, font=("Arial", 12))
entry_edad.pack()

# Correo
tk.Label(ventana_registro, text="Corro electronico: ", font=("Arial", 12), bg="#3F779D", fg="white").pack(pady=5)
entry_correo= tk.Entry(ventana_registro, font=("Arial", 12,))
entry_correo.pack()

# Boton de continuar
boton_continuar = tk.Button(
    ventana_registro,
    text="Continuar",
    font=("Arial", 14,"bold"),
    bg="#164A69",
    fg="white",
    relief="raised",
    bd=2,
    padx=10,
    pady=5,
    command=registrar_usuario
)
boton_continuar.pack(side="right", padx=50)

# Boton de regreso
boton_regresar = tk.Button(
    ventana_registro,
    text="Regresar",
    font=("Arial", 14, "bold"),
    bg="#607D8B",
    bd=2,
    padx=10,
    pady=5,

)
boton_regresar.pack(side="left", padx=50)

ventana_registro.mainloop ()