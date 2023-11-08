from tkinter import *

root = Tk()
root.title("Inicio")
root.geometry("1100x800")
root.configure(background="#b9d279")

"""

frameP1 = frame que contiene los frames de saludo y el de ingreso
frameP2 = frame que contiene los frames de biografia y fotos
frameP3 = frame contenido en frameP1, que contiene el saludo de bienvenida
frameP4 = frame contenido en frameP1 que contiene el boton de ingreso
frameP5 = frame contenido en frameP2 que contiene la biografia de desarrolladores
frameP6 = frame contenido en frameP2 que contiene las fotos de los desarrolladores

"""


frameP1 = Frame(root)
frameP1.grid(row=0,column=0,padx=(5,0),pady=5, sticky="n")
frameP1['borderwidth'] = 5
frameP1.configure(background="#b9d279")

frameP2 = Frame(root)
frameP2.grid(row=0,column=1,padx=(5,0),pady=5, sticky="n")
frameP2['borderwidth'] = 5
frameP2.configure(background="#b9d279")

frameP3=Frame(frameP1,height=70,width=500,bg="#085870")
frameP3.grid(row=0,column=0)

frameP4 = Frame(frameP1, bg = "#b9d279")
frameP4.grid(row = 1, column = 0)

frameP5 = Label(frameP2,height=70,width=500,bg="#7c9933")
frameP5.grid(row=0,column=0)


frameP6 = Frame(frameP2)
frameP6.grid(row = 1, column = 0)


saludo = Label(frameP3,text="Bienvenido al sistema de bibliotecas de la Universidad Nacional de Colombia",font=("arial", 18, "bold"),bg="#7c9933",wraplength=500,fg="#cedae0")
saludo.pack(expand = True)

imagen = PhotoImage(file = "loki.png")
ImagenSistema = Label(frameP4, image= imagen,width=500,wraplength=160,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
ImagenSistema.pack(side="top",pady=0)

def cambiarDeVentana():
    pass

botonIngreso=Button(frameP4,text="Ingresar",command=cambiarDeVentana,bg="#7c9933",font=("arial", 12, "bold"),fg="#cedae0")
botonIngreso.pack(side="top",pady=(10,20))

biografias = ["Hola, soy juan dadadadadadadadadadadadadadadadadadadadad", "Y Samuel y que tales bababababababababbabab"]

presentacion = Label(frameP5, text = biografias[0], font=("arial", 18, "bold"), bg="#7c9933", wraplength = 500, fg="#cedae0")
presentacion.pack(expand = True)

fotoo = PhotoImage(file = "finger.png")
imagenBiografia = Label(frameP6, image = fotoo, width=500,wraplength=500,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
imagenBiografia.pack(side="top", pady = 0)






descripTexto = Label(frameP4,text="",font=("arial", 10, "bold"),bg="#b9d279",wraplength=400)
descripTexto.pack(side="top",fill="x",pady=10)
root.menuBar = Menu(root)
root.option_add("*tearOff",  False)
root.config(menu=root.menuBar)
menu1= Menu(root.menuBar)
root.menuBar.add_cascade(label="Archivo",menu=menu1)
menu1.add_command(label="Salir",command=lambda:root.destroy())
        
textDescrip="Este sistema permite el control y administracion de la base de datos del sistema de bibliotecas de la Universidad Nacional. En este sistema encontraras funcionalidades para el prestamo de material de la biblioteca, para agregar/eliminar material y para gestionar tus reservas/multas."
menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))
        

root.mainloop()