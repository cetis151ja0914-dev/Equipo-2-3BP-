import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

# -------- CONFIGURACIÓN DE COLORES Y FUENTE --------
COLOR_FONDO = "#A4A9FF"
COLOR_MENU = "#7690CC"
COLOR_TEXTO = "#FFFFFF"
FUENTE_TITULO = ("Arial", 16, "bold")
FUENTE_TEXTO = ("Arial", 12)

# -------- VENTANA PRINCIPAL --------
root = tk.Tk()
root.title("Equipo 2")
root.geometry("900x500")
root.config(bg=COLOR_FONDO)

# -------- FRAME MENÚ LATERAL --------
menu_frame = tk.Frame(root, bg=COLOR_MENU, width=200)
menu_frame.pack(side="left", fill="y")

# -------- FRAME CONTENIDO --------
contenido_frame = tk.Frame(root, bg=COLOR_FONDO)
contenido_frame.pack(side="right", fill="both", expand=True)

# -------- FUNCIÓN PARA CAMBIAR DE PÁGINA --------+
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_children():
        widget.destroy()
    paginas[nombre]()

# -------- FUNCIÓN DE ADVERTENCIA PARA INVITADO --------
def advertencia_invitado():
    messagebox.showwarning(
        "Advertencia - Modo Invitado",
        "⚠️ Al registrarte como invitado, tus respuestas no se guardarán y no recibirás resultados personalizados.\n"
        "Se recomienda registrarse con un usuario para obtener recomendaciones completas."
    )
    mostrar_pagina("Test")  # Ir directamente al test

# -------- PÁGINAS --------
def pagina_bienvenida():
    tk.Label(
        contenido_frame,
        text="📸 Bienvenido al software de detección de adicción a tomar fotografías 📸",
        font=FUENTE_TITULO,
        bg=COLOR_FONDO
    ).pack(pady=30)

    tk.Label(
        contenido_frame,
        text=(
            "Este test tiene como propósito evaluar los niveles de dependencia o\n"
            "adicción a tomar fotografías, permitiendo reconocer si esta práctica se realiza por gusto,\n"
            "necesidad o hábito. Los resultados servirán para fomentar el autocontrol\n"
            "y el uso responsable de la tecnología."
        ),
        bg=COLOR_FONDO,
        font=FUENTE_TEXTO,
        justify="center"
    ).pack(pady=10)

    # Imagen de bienvenida
    try:
        global imagen_bienvenida
        imagen_bienvenida = PhotoImage(file="descarga.png")
        img_label = tk.Label(contenido_frame, image=imagen_bienvenida, bg="#7690CC")
        img_label.pack(pady=10)
    except Exception:
        aviso = tk.Label(contenido_frame, text="⚠️ La imagen no se encontró", bg="#7690CC", fg="gray")
        aviso.pack()

    # Botones de navegación
    ttk.Button(contenido_frame, text="Registro ➡️", command=lambda: mostrar_pagina("Registro")).pack(pady=10)
    ttk.Button(contenido_frame, text="Invitado ➡️", command=advertencia_invitado).pack(pady=10)

def pagina_registro():
    tk.Label(contenido_frame, text="📝 Registro de Usuario", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    
    # Campos de registro
    for campo in ["Nombre", "Edad", "Correo electrónico"]:
        tk.Label(contenido_frame, text=f"{campo}:", bg=COLOR_FONDO, font=FUENTE_TEXTO).pack()
        tk.Entry(contenido_frame, width=40).pack(pady=5)

    # Botones de navegación
    frame_botones = tk.Frame(contenido_frame, bg=COLOR_FONDO)
    frame_botones.pack(pady=20)

    ttk.Button(frame_botones, text="⬅️ Regresar", command=lambda: mostrar_pagina("Bienvenida")).grid(row=0, column=0, padx=10)
    ttk.Button(frame_botones, text="Continuar ➡️", command=lambda: mostrar_pagina("Test")).grid(row=0, column=1, padx=10)

# -------- PREGUNTAS DEL TEST --------
preguntas = [
    ("¿Con qué frecuencia tomas fotografías en un día normal?", ["a) Casi nunca", "b) Algunas  veces","c) Muy seguido" ,"d) Todo el tiempo"]),
    ("¿Sientes ansiedad si no puedes usar tu cámara o teléfono para tomar fotos?", ["a) No", "b) A veces", "c) Sí, mucho"]),
    ("¿Subes tus fotos a redes sociales inmediatamente después de tomarlas?", ["a) Nunca", "b) A veces", "c) Siempre"]),
    ("¿Has recibido comentarios de que tomas demasiadas fotos?", ["a) No", "b) Algunas veces", "c) Sí"]),
    ("¿Te cuesta disfrutar momentos sin tomar una foto?", ["a) No", "b) Un poco", "c) Sí, mucho"]),
    ("¿Con qué frecuencia sientes la necesidad de tomar fotos en cualquier lugar o momento?",["a) Casi nunca","b) A veces","Frecuentemente","c) Todo el tiempo"]),
    ("¿Qué haces cuando no puedes tomar una foto en una situación que te gustaría capturar?",["a) No me afecta","b) Me molesta un poco","c) Me frustro","d) Me siento ansioso o incómodo"]),
    ("¿Revisas constantemente las fotos que tomas para publicarlas en redes sociales?",["a) Nunca","b) Rara vez","c) Casi siempre","d) Siempre"]),
    ("¿Tomas fotos para conservar recuerdos o más bien para obtener aprobación de los demás (likes, comentarios)?",["a) Solo para recuerdos personales","b) Por ambas razones","c) Principalmente por aprobación","d) Siempre por aprobación"]),
    ("¿Has dejado de disfrutar un momento porque estabas concentrado en tomar la foto perfecta?",["a) Nunca","b) Alguna vez","c) Varias veces","d) Casi siempre"]),
]

# -------- FUNCIÓN PARA MOSTRAR LAS PREGUNTAS --------
def iniciar_test():
    for widget in contenido_frame.winfo_children():
        widget.destroy()

    tk.Label(contenido_frame, text="🧠 Test de Detección de Adicción a Tomar Fotografías", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)

    respuestas_usuario.clear()

    for i, (pregunta, opciones) in enumerate(preguntas):
        tk.Label(contenido_frame, text=f"{i+1}. {pregunta}", bg=COLOR_FONDO, font=FUENTE_TEXTO, justify="left").pack(anchor="w", padx=30, pady=5)
        var = tk.StringVar(value="")  # Valor inicial vacío
        respuestas_usuario.append(var)
        for op in opciones:
            ttk.Radiobutton(contenido_frame, text=op, variable=var, value=op).pack(anchor="w", padx=50)

    ttk.Button(contenido_frame, text="Finalizar Test", command=finalizar_test).pack(pady=20)

def finalizar_test():
    # Aquí podrías calcular resultados según las respuestas
    messagebox.showinfo("Test completado", " Gracias por completar el test.\nTus respuestas han sido registradas.")
    mostrar_pagina("Bienvenida")

# Lista para guardar las respuestas
respuestas_usuario = []

def pagina_test():
    tk.Label(contenido_frame, text="📷 Test de Detección de Adicción a Tomar Fotografías", font=FUENTE_TITULO, bg=COLOR_FONDO).pack(pady=20)
    tk.Label(
        contenido_frame,
        text="Presiona el botón para comenzar el test.",
        wraplength=600,
        bg=COLOR_FONDO,
        font=FUENTE_TEXTO
    ).pack(pady=10)

    ttk.Button(contenido_frame, text="Iniciar Test ", command=iniciar_test).pack(pady=20)

    # Botones de navegación
    frame_botones = tk.Frame(contenido_frame, bg=COLOR_FONDO)
    frame_botones.pack(pady=30)
    ttk.Button(frame_botones, text="⬅️ Regresar", command=lambda: mostrar_pagina("Registro")).grid(row=0, column=0, padx=10)
    ttk.Button(frame_botones, text="Salir", command=root.quit).grid(row=0, column=1, padx=10)

# -------- DICCIONARIO DE PÁGINAS --------
paginas = {
    "Bienvenida": pagina_bienvenida,
    "Registro": pagina_registro,
    "Test": pagina_test,
}

# -------- BOTONES DE MENÚ LATERAL --------
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina(n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="Salir", command=root.quit).pack(side="bottom", pady=10)

# -------- MOSTRAR PÁGINA INICIAL --------
pagina_bienvenida()

root.mainloop()
