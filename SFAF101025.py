# importar la biblioteca
import tkinter as tk 
from tkinter import ttk

# crear la ventana en python
ventana =tk.Tk()
#configuramos la ventana
ventana.title("Esta es mi primera ventana")
ventana.geometry("500x300")
#agregamos los widgets

ttk.Label(ventana,text="EQUIPO 2").grid(column=4,row=1)
ttk.Label(ventana,text="Aplica Metodologias Aguiles para el desarrollo de SW").grid(column=4,row=2)
ttk.Label(ventana,text="Jessica Gonzalez").grid(column=4,row=3)
ttk.Label(ventana,text="Araceli Torija ").grid(column=4,row=4)
ttk.Label(ventana,text="litzy huerta ").grid(column=4,row=5)
ttk.Label(ventana,text="citlaly mendez ").grid(column=4,row=6)
ttk.Label(ventana,text="Kevin Martinez").grid(column=4,row=7)
ttk.Label(ventana,text="America Nicole ").grid(column=4,row=8)

#activamos la ventana
ventana.resizable(0,0)
ventana.mainloop()

