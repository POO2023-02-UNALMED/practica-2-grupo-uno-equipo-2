from tkinter import *
    
root = Tk()
root.title("Inicio")
root.geometry("1100x700")
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
frameP1.grid(row=0,column=0,padx=25,pady=5, sticky="n")
frameP1['borderwidth'] = 5
frameP1.configure(background="#b9d279")

frameP2 = Frame(root)
frameP2.grid(row=0,column=1,padx=25,pady=5, sticky="n")
frameP2['borderwidth'] = 5
frameP2.configure(background="#b9d279")

frameP3=Frame(frameP1,height=70,width=500,bg="#085870")
frameP3.grid(row=0,column=0)

frameP4 = Frame(frameP1, bg = "#b9d279", width=400, height=400)
frameP4.grid(row = 1, column = 0, pady=45)

frameP5 = Label(frameP2,height=70,width=500,bg="#7c9933")
frameP5.grid(row=0,column=0)


frameP6 = Frame(frameP2, width=450, height=450)
frameP6.grid(row = 1, column = 0, pady=40)


saludo = Label(frameP3,text="Bienvenido al sistema de bibliotecas de la Universidad Nacional de Colombia",font=("arial", 18, "bold"),bg="#7c9933",wraplength=500,fg="#cedae0")
saludo.pack(expand = True)

imagenes = [PhotoImage(file = "img\\Sis1.png"),
               PhotoImage(file = "img\\Sis2.png"),
               PhotoImage(file = "img\\Sis3.png"),
               PhotoImage(file = "img\\Sis4.png"),
               PhotoImage(file = "img\\Sis5.png")]

#imagen = PhotoImage(file = "loki.png")
ImagenSistema = Label(frameP4, image= imagenes[0],width=420,height=420,wraplength=160,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
ImagenSistema.pack(side="top",pady=0)

im_actual = 0

def cambiarImagenesOG(evento):
    global im_actual
    if im_actual < 4:
        im_actual = im_actual+1
    else:
        im_actual = 0
    
    ImagenSistema.config(image=imagenes[im_actual])

ImagenSistema.bind("<Enter>", cambiarImagenesOG)


def Ingresar(root):
    root.destroy()
    seg = Tk()
    seg.title("Sistema de Gestión de Bibliotecas")
    seg.geometry("1100x700")
    seg.configure(background="#b9d279")
    Label(seg, text="Esta es la segunda ventana").pack()
    seg.mainloop()


def cambiarDeVentana():
    pass

botonIngreso=Button(frameP4,text="Ingresar",bg="#7c9933",font=("arial", 12, "bold"),fg="#cedae0", command=lambda: Ingresar(root))
botonIngreso.pack(side="top",pady=(10,20))

biografias = [
                "Juan es un desarrollador de software. Nació en Turbo, y tiene un gato amarillo llamado Loki. Le gusta aprender cosas nuevas y resolver problemas complejos con su código. Además de demostrar interés por el campo de la Inteligencia Artificial.",
                "Samuel es un desarrollador de software apasionado por los videojuegos. Nació en Medellín, y tiene una gata negra llamada Pólvora. Tiene experiencia en varios lenguajes de programación, y es Técnico en Desarrollo de Software."]

presentacion = Label(frameP5, text = biografias[1], font=("arial", 13, "bold"), bg="#7c9933", wraplength = 500, fg="#cedae0", width= 50)
presentacion.pack(expand = True)


fotosSamuel = [PhotoImage(file = "img\\devSam1.png"),
               PhotoImage(file = "img\\devSam2.png"),
               PhotoImage(file = "img\\devSam3.png"),
               PhotoImage(file = "img\\devSam4.png")]

fotosPablo = [PhotoImage(file = "img\\devPab1.png"),
              PhotoImage(file = "img\\devPab2.png"),
              PhotoImage(file = "img\\devPab3.png"),
              PhotoImage(file = "img\\devPab4.png")]

samuel = True


img1 = Label(frameP6, image = fotosSamuel[0], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
img1.grid(column=0,row=0)
img2 = Label(frameP6, image = fotosSamuel[1], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
img2.grid(column=1,row=0)
img3 = Label(frameP6, image = fotosSamuel[2], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
img3.grid(column=0,row=1)
img4 = Label(frameP6, image = fotosSamuel[3], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
img4.grid(column=1,row=1)


def cambiarImagenes(evento):
    global samuel
    if samuel:
        img1.config(image=fotosPablo[0])
        img2.config(image=fotosPablo[1])
        img3.config(image=fotosPablo[2])
        img4.config(image=fotosPablo[3])
        presentacion.config(text=biografias[0])
        samuel = False
        return
    
    img1.config(image=fotosSamuel[0])
    img2.config(image=fotosSamuel[1])
    img3.config(image=fotosSamuel[2])
    img4.config(image=fotosSamuel[3])
    presentacion.config(text=biografias[1])
    samuel = True
    return

#frameP6.bind("<Enter>", cambiarImagenes)
presentacion.bind("<Button-1>", cambiarImagenes)



descripTexto = Label(frameP4,text="",font=("arial", 9, "bold"),bg="#b9d279",wraplength=500)
descripTexto.pack(side="left")
menuBar = Menu(root)
root.option_add("*tearOff",  False)
root.config(menu=menuBar)
menu1= Menu(menuBar)
menuBar.add_cascade(label="Archivo",menu=menu1)
textDescrip="Este sistema permite el control y administracion de la base de datos del sistema de bibliotecas de la Universidad Nacional. En este sistema encontraras funcionalidades para el prestamo de material de la biblioteca, para agregar/eliminar material y para gestionar tus reservas/multas."
menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))
menu1.add_command(label="Salir",command=lambda:root.destroy())
        

root.mainloop()