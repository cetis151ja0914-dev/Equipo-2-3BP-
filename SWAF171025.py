import tkinter as ttk
#color
color_fondo ="#424242"
color_menu = "#424242"
color_text ="#FFFFFF"
fuente_text = ("Arial", 16,"bold")
fuente_titulo = ("Arial", 12,"bold")


#funcion de navegacion cambiar pagina
#def ir_a(pagina_actual, pagina_siguiente):
    #pagina_actual.withdraw()
    #pagina_siguiente.deiconify()

#def regresar(pagina_actual, pagina_anterior):
   # pagina_actual.withdraw()
    #pagina_anterior.deiconify()
def mostrar_pagina(nombre):
    for widget in contenido_frame.winfo_clindren(): #tiene pagina conbinada Y CADA ELEMENTO SE LLAMA HIJO
        widget.destroy()
        paginas[nombre]()

#v3ntana principal
root= tk.Tk()
root.title("Aplicacion para detctar???")
root.geometry("900x500")
root.config(bg=color_fondo)

#venta principal}
menu_frame=tk.Frame(root,bg=color_fondo, width=200)
menu_frame.pack(side="left", fill="y")

#contenido frame
contenido_frame= tk.Frame(root, bg=color_fondo)
contenido_frame.pack("right", fill="both", expand=True)

# Ventana 1: Bienvenida
def pagina_bienvenida():
    ttk.Label(contenido_frame "Bienvenidos a la pagina principal ")
tk.Label(contenido_frame, text="Bienvenido al software de detección de adicciones tecnológicas").pack(pady=20)
tk.Label(contenido_frame, text="Aquí colocamos la descripción de tu software").pack(pady=10)


# Ventana 2: Registro
def pagina_registro():
tk.Label(contenido_frame, text="REGISTRO DE USUARIO").pack(pady=20)
tk.Label(contenido_frame, text="Nombre: ").pack()
tk.Entry(contenido_frame).pack()
tk.Entry(contenido_frame).pack()tk.Label(ventana2, text="Correo electrónico: ").pack()
tk.Entry(contenido_frame).pack()

#tk.Button(ventana2, text="Regresar", command=lambda: regresar(ventana2, ventanabien)).pack(side="left", padx=50, pady=40)
#ttk.Button(ventana2, text="Continuar", command=lambda: ir_a(ventana2, ventana3)).pack(side="right", padx=50, pady=40)

# Ventana 3: Test
def pagina_test():

tk.Label(contenido_frame, text="Esta es la ventana donde se incluirá el test para adicciones").pack(pady=20)
tk.Label(contenido_frame, text="Responde las siguientes preguntas", wraplength=500).pack(pady=20)

#tk.Button(ventana3, text="Regresar", command=lambda: regresar(ventana3, ventana2)).pack(side="left", padx=50, pady=40)
#tk.Button(ventana3, text="Continuar", command=lambda: ir_a(ventana3, ventana4)).pack(side="right", padx=50, pady=40)

# Ventana 4: Resultados
ventana4 = tk.Toplevel(ventanabien)
ventana4.title("4-VENTANA DE RESULTADOS")
ventana4.geometry("600x400")

ttk.Label(contenido_frame, text="Resultados del test").pack(pady=20)
ttk.Button(contenido_frame, text="Regresar", command=lambda: regresar(ventana4, ventana3)).pack(side="left", padx=50, pady=40)
ttk.Button(contenido_frame, text="Continuar", command=lambda: ir_a(ventana4, ventana5)).pack(side="right", padx=50, pady=40)


# Ventana 5: Síntomas y señales
ventana5 = tk.Toplevel(ventanabien)
ventana5.title("5-VENTANA DE SÍNTOMAS Y SEÑALES")
ventana5.geometry("600x400")

tk.Label(ventana5, text="Esta es la ventana donde se mostrarán los síntomas y señales de la adicción").pack(pady=20)
tk.Button(ventana5, text="Regresar", command=lambda: regresar(ventana5, ventana4)).pack(side="left", padx=50, pady=40)
tk.Button(ventana5, text="Continuar", command=lambda: ir_a(ventana5, ventana6)).pack(side="right", padx=50, pady=40)

# Ventana 6: Historias inspiradoras
ventana6 = tk.Toplevel(ventanabien)
ventana6.title("6-HISTORIAS INSPIRADORAS")
ventana6.geometry("600x400")

tk.Label(ventana6, text="Historias inspiradoras y recomendaciones").pack(pady=20)
#tk.Button(ventana6, text="Regresar", command=lambda: regresar(ventana6, ventana5)).pack(side="left", padx=50, pady=40)
#tk.Button(ventana6, text="Cerrar", command=ventana6.destroy).pack(side="right", padx=50, pady=40)



#diccionario de paginas
paginas={
    "Bienvenida" :pagina_bienvenida,
    "Registro" :pagina_registro,
    "Test" :pagina_test,
    "Resultados":pagina_resultados,
    "sintomas":pagina_sintomas,
    "Historias":pagina_Historia,
    "Ayuda":pagina_ayuda,
}

#botones del menu lateral
for nombre in paginas:
    ttk.Button(menu_frame, text=nombre, command=lambda n=nombre: mostrar_pagina (n)).pack(fill="x", pady=5, padx=10)

ttk.Button(menu_frame, text="salir", command=root.quit).pack(side="bottom", pady=10) #bottom significa abajo

#mostrazr ventana
pagina_bienvenida()
root.mainloop()  # Ejecutar la ventana de bienvenida
