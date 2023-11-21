from tkinter import *
from tkinter import messagebox
#from baseDatos import Aplicacion
from uiMain.prestamoRecursos import PrestamoRecursos
from uiMain.reservaEvento import ReservaEvento
from uiMain.baseDatos import BaseDeDatos
from uiMain.gestionPrestamos import GestionPrestamo
from uiMain.gestionMultas import GestionMultas
from gestorAplicacion.clasesDeBiblioteca.Libro import Libro
from gestorAplicacion.clasesDeBiblioteca.Computador import Computador
from gestorAplicacion.clasesDeBiblioteca.BibliotecaDos import BibliotecaDos
from gestorAplicacion.clasesDeBiblioteca.Copia import Copia
from gestorAplicacion.clasesDeBiblioteca.PC import PC
from gestorAplicacion.clasesDeBiblioteca.Autor import Autor
from gestorAplicacion.clasesDeBiblioteca.Sala import Sala
from gestorAplicacion.clasesDeAdministracion.Sistema import Sistema
from gestorAplicacion.clasesDeAdministracion.Usuario import Usuario
from gestorAplicacion.clasesDeAdministracion.Prestamo import Prestamo
from gestorAplicacion.clasesDeAdministracion.Multa import Multa
from datetime import date
from baseDatos.Serializador import Serializador
from baseDatos.Deserializador import Deserializador



class ventanaInicial(Tk):

    def __init__(self, sistema):
        super().__init__()
        self.title("Inicio")
        self.geometry("1250x800")
        self.configure(background="#b9d279")
        self.iconbitmap("img\\R.ico")
        self.resizable(False, False)

        self.sistema = sistema

        """

        frameP1 = frame que contiene los frames de saludo y el de ingreso
        frameP2 = frame que contiene los frames de biografia y fotos
        frameP3 = frame contenido en frameP1, que contiene el saludo de bienvenida
        frameP4 = frame contenido en frameP1 que contiene el boton de ingreso
        frameP5 = frame contenido en frameP2 que contiene la biografia de desarrolladores
        frameP6 = frame contenido en frameP2 que contiene las fotos de los desarrolladores

        """


        frameP1 = Frame(self)
        frameP1.grid(row=0,column=0,padx=25,pady=5, sticky="n")
        frameP1['borderwidth'] = 5
        frameP1.configure(background="#b9d279")

        frameP2 = Frame(self)
        frameP2.grid(row=0,column=1,padx=25,pady=5, sticky="n")
        frameP2['borderwidth'] = 5
        frameP2.configure(background="#b9d279")

        frameP3=Frame(frameP1,height=70,width=500,bg="#b9d279")
        frameP3.grid(row=0,column=0)

        frameP4 = Frame(frameP1, bg = "#b9d279", width=400, height=400)
        frameP4.grid(row = 1, column = 0, pady=45)

        frameP5 = Frame(frameP2,height=70,width=500,bg="#7c9933")
        frameP5.grid(row=0,column=0) 


        frameP6 = Frame(frameP2, width=450, height=450, bg ="#7c9933")
        frameP6.grid(row = 1, column = 0, pady=40)


        saludo = Label(frameP3,text="Bienvenido al sistema de bibliotecas de la Universidad Nacional de Colombia",font=("arial", 17, "bold"),bg="#7c9933",wraplength=500,fg="#cedae0")
        saludo.pack(expand = True)

        imagenes = [PhotoImage(file = "img\\Sis1.png"),
                    PhotoImage(file = "img\\Sis2.png"),
                    PhotoImage(file = "img\\Sis3.png"),
                    PhotoImage(file = "img\\Sis4.png"),
                    PhotoImage(file = "img\\Sis5.png")]

        #imagen = PhotoImage(file = "loki.png")
        ImagenSistema = Label(frameP4, image= imagenes[0],width=420,height=420,wraplength=160,highlightbackground="#7c9933",highlightthickness=4, bg = "#b9d279")
        ImagenSistema.pack(side="top",pady=0)

        self.im_actual = 0

        def cambiarImagenesOG(evento):
            global im_actual
            if self.im_actual < 4:
                self.im_actual = self.im_actual+1
            else:
                self.im_actual = 0

            ImagenSistema.config(image=imagenes[self.im_actual])

        ImagenSistema.bind("<Enter>", cambiarImagenesOG)

        def Ingresar(self):
            self.destroy()
            ventPrincipal(sistema)

        botonIngreso=Button(frameP4,text="Ingresar",bg="#7c9933",font=("arial", 12, "bold"),fg="#cedae0", command=lambda: Ingresar(self))
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

        self.samuel = True


        img1 = Label(frameP6, image = fotosSamuel[0], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=2, bg = "#b9d279")
        img1.grid(column=0,row=0)
        img2 = Label(frameP6, image = fotosSamuel[1], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=2, bg = "#b9d279")
        img2.grid(column=1,row=0)
        img3 = Label(frameP6, image = fotosSamuel[2], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=2, bg = "#b9d279")
        img3.grid(column=0,row=1)
        img4 = Label(frameP6, image = fotosSamuel[3], width=220,height=220,wraplength=500,highlightbackground="#7c9933",highlightthickness=2, bg = "#b9d279")
        img4.grid(column=1,row=1)


        def cambiarImagenes(evento):
            global samuel
            if self.samuel:
                img1.config(image=fotosPablo[0])
                img2.config(image=fotosPablo[1])
                img3.config(image=fotosPablo[2])
                img4.config(image=fotosPablo[3])
                presentacion.config(text=biografias[0])
                self.samuel = False
                return

            img1.config(image=fotosSamuel[0])
            img2.config(image=fotosSamuel[1])
            img3.config(image=fotosSamuel[2])
            img4.config(image=fotosSamuel[3])
            presentacion.config(text=biografias[1])
            self.samuel = True
            return

        #frameP6.bind("<Enter>", cambiarImagenes)
        presentacion.bind("<Button-1>", cambiarImagenes)



        descripTexto = Label(frameP4,text="",font=("arial", 9, "bold"),bg="#b9d279",wraplength=500)
        descripTexto.pack(side="left")
        menuBar = Menu(self)
        self.option_add("*tearOff",  False)
        self.config(menu=menuBar)
        menu1= Menu(menuBar)
        menuBar.add_cascade(label="Inicio",menu=menu1)

        textDescrip="Este sistema permite el control y administracion de la base de datos del sistema de bibliotecas de la Universidad Nacional. En este sistema encontraras funcionalidades para el prestamo de material de la biblioteca, para agregar/eliminar material y para gestionar tus reservas/multas."
        menu1.add_command(label="Descripcion",command=lambda: descripTexto.config(text=textDescrip))

        def salirSerializar():
            Serializador.serializar(sistema)
            self.destroy()

        menu1.add_command(label="Salir",command=salirSerializar)

        


        self.mainloop()


class ventPrincipal(Tk):
      def __init__(self,sistema):
            super().__init__()
            self.title("Sistema de Gestión de Bibliotecas")
            self.geometry("1250x800")
            self.configure(background="#b9d279")
            self.iconbitmap("img\\R.ico")

            def Volver():
                self.destroy()
                ventanaInicial(sistema)

            def kill(root):
                for widget in root.winfo_children():
                        if isinstance(widget, Frame):
                            widget.destroy()

            def prestamoDeRecursos():
                kill(self)
                p = PrestamoRecursos(self, sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def ReservaDeEvento():
                kill(self)
                p = ReservaEvento(self,sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def BaseDatos():
                kill(self)
                p = BaseDeDatos(self,sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def gestionPrestamos():
                kill(self)
                p = GestionPrestamo(self, sistema)
                p.grid(row=0, column=0,rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def gestionarMultas():
                kill(self)
                p = GestionMultas(self, sistema)
                p.grid(row=0, column=0, rowspan=2)
                p.place(relx=0.5,rely=0.5,anchor="center")

            def Funny():
                respuesta = False
                while(respuesta != True):
                    respuesta = messagebox.askyesno("Guzmán, David, Oswaldo", "¿Samuel Gutiérrez y Juan Pérez se merecen un 5.0 por este trabajo?")
                messagebox.showwarning("OJO","Esperamos que sea verdad :)")



            frame = Frame(self, bg="#b9d279")
            frame.pack(padx=10,pady=10)

            bienvenida = Label(frame, text="¡Bienvenido al sistema de bibliotecas de la Universidad Nacional de Colombia!", bg= "#8cac39", fg= "white", font=("arial", 15, "bold"))
            bienvenida.pack(anchor="center")
            img = PhotoImage(file="img\\logo.png")
            contenedorImg = Label(frame, image = img, bg = "#b9d279")
            contenedorImg.pack(anchor="center", pady=(27,20))
            texto = "El sistema de bibliotecas de la universidad ofrece las siguientes cinco funcionalidades: \n1. Reserva de Recurso: Esta función permite a los usuarios reservar recursos disponibles \nen la biblioteca, como libros, revistas y documentos electrónicos. \n\n2. Reserva para Evento: Los usuarios pueden reservar espacios dentro de la biblioteca para \neventos como reuniones de estudio, presentaciones y conferencias. \n\n3. Gestión de Base de Datos: Esta funcionalidad permite a los administradores de la \nbiblioteca gestionar la base de datos de la biblioteca, incluyendo la adición, eliminación \ny modificación de registros de recursos. \n\n4. Gestión de Préstamos: Esta función permite a los usuarios solicitar préstamos de recursos \nde la biblioteca y a los administradores gestionar estos préstamos, incluyendo la emisión, \nrenovación y devolución de recursos. \n\n5. Gestión de Multas: Esta funcionalidad permite a los administradores de la biblioteca emitir \ny gestionar multas por retrasos en la devolución de recursos prestados. Estas funcionalidades \nhacen que el sistema de bibliotecas de la universidad sea eficiente y fácil de usar para todos \nlos usuarios."

            descripcion = Label(frame, text=texto, bg="#8cac39", fg = "white", font=("arial", 11, "bold"),justify="left", padx= 20, pady=20)
            descripcion.pack(padx=25,pady=10, expand=False)



            menuBar2 = Menu(self)
            self.option_add("*tearOff",  False)
            self.config(menu=menuBar2)
            menu2= Menu(menuBar2)

            menuBar2.add_cascade(label="Archivo",menu=menu2)
            menu2.add_command(label="Aplicacion",command=lambda: messagebox.showinfo("Aplicacion","Este sistema permite el control y administracion de la base de datos del sistema de bibliotecas de la Universidad Nacional. En este sistema encontraras funcionalidades para el prestamo de material de la biblioteca, para agregar/eliminar material y para gestionar tus reservas/multas."))
            menu2.add_command(label="Salir",command=lambda:Volver())

            menu3 = Menu(menuBar2)
            menuBar2.add_cascade(label="Procesos y Consultas",menu=menu3)
            menu3.add_command(label="Préstamo de Recursos",command= prestamoDeRecursos)
            menu3.add_command(label="Reserva de Recursos para Eventos",command= ReservaDeEvento)
            menu3.add_command(label="Gestión Base de Datos",command= BaseDatos)
            menu3.add_command(label="Gestión de Prestamos y Reservas",command= gestionPrestamos)
            menu3.add_command(label="Gestión de Multas",command=gestionarMultas)



            menu4 = Menu(menuBar2)
            menuBar2.add_cascade(label="Ayuda",menu=menu4)
            menu4.add_command(label="Acerca de",command=lambda: Funny())

            self.mainloop()

      
if __name__ == "__main__":
    sistema = Sistema()
    Deserializador.deserializar(sistema)
    #app = Aplicacion(sistema)
    """
    autor1 = Autor("Yuval Noah Harari", "Israel", "Historia")
    autor2 = Autor("J.K. Rowling", "Reino Unido", "Fantasía")
    autor3 = Autor("Harper Lee", "Estados Unidos", "Ficción")
    autor4 = Autor("José Saramago", "Portugal", "Realismo mágico")
    autor5 = Autor("Rebecca Solnit", "Estados Unidos", "Ensayo")
    autor6 = Autor("Miguel de Cervantes", "España", "Ficción")
    autor7 = Autor("Orson Scott Card", "Estados Unidos", "Ciencia ficción")
    autor8 = Autor("Julio Cortázar", "Argentina", "Ficción")
    autor9 = Autor("F. Scott Fitzgerald", "Estados Unidos", "Ficción")
    autor10 = Autor("Yuval Noah Harari", "Israel", "Ensayo")
    autor11 = Autor("Gabriel García Márquez", "Colombia", "Realismo mágico")
    autor12 = Autor("George Orwell", "Reino Unido", "Distopía")

    autores = [autor1, autor2, autor3, autor4, autor5, autor6, autor7, autor8, autor9, autor10, autor11, autor12]

    libros = [
        Libro("Sapiens: De animales a dioses", 1, "978-0-307-58973-2", autor1, 2014),
        Libro("Harry Potter y la piedra filosofal", 2, "978-0-7475-3269-6", autor2, 1997),
        Libro("Cien años de soledad", 3, "978-84-204-3471-6", autor11, 1967),
        Libro("1984", 4, "978-3-16-148410-0", autor12, 1949),
        Libro("Matar a un ruiseñor", 5, "978-0-553-21311-6", autor3, 1960),
        Libro("Ensayo sobre la ceguera", 6, "978-1-84749-593-7", autor4, 1995),
        Libro("Los hombres me explican cosas", 7, "978-1-933633-92-9", autor5, 2014),
        Libro("Don Quijote de la Mancha", 8, "978-84-204-9184-8", autor6, 1605),
        Libro("El juego de ender", 9, "978-0-06-112008-4", autor7, 1985),
        Libro("Crónica de una muerte anunciada", 10, "978-84-339-7049-4", autor11, 1981),
        Libro("Rayuela", 11, "978-84-3760494-7", autor8, 1963),
        Libro("El gran Gatsby", 12, "978-0-8129-7449-8", autor9, 1925),
        Libro("El amor en los tiempos del cólera", 13, "978-84-204-5298-7", autor11, 1985),
        Libro("To Kill a Mockingbird", 14, "978-0-525-43396-9", autor3, 1960),
    ]

    computadores = [
        Computador("Samsung JX", 0, "Samsung", "Alta"),
        Computador("HP Pavilion", 1, "HP", "Media"),
        Computador("Dell Inspiron", 2, "Dell", "Baja"),
        Computador("Lenovo ThinkPad", 3, "Lenovo", "Alta"),
        Computador("Asus VivoBook", 4, "Asus", "Media"),
        Computador("Acer Aspire", 5, "Acer", "Baja"),
    ]

    bibliotecas = [
        BibliotecaDos("Efe Gomez", "Medellín"),
        BibliotecaDos("Gabriel Garcia Marquez", "Bogota")
    ]

    librosSedeMedellin = [libros[0],libros[1],libros[2],libros[3],libros[4],libros[7],libros[10],libros[13]]
    bibliotecas[0].set_libros(librosSedeMedellin)

    librosSedeBogota = [libros[0],libros[1],libros[2],libros[5],libros[6],libros[7],libros[10],libros[11], libros[12], libros[13]]
    bibliotecas[1].set_libros(librosSedeBogota)

    computadoresSedeMedellin = [computadores[0], computadores[1], computadores[2], computadores[3]]
    bibliotecas[0].set_computadores(computadoresSedeMedellin)

    computadoresSedeBogota = [computadores[0], computadores[1], computadores[2], computadores[3], computadores[5]]
    bibliotecas[1].set_computadores(computadoresSedeBogota)


    bibliotecas[0].añadir_sala(Sala(bibliotecas[0], "Auditorio 1", 30))
    bibliotecas[0].añadir_sala(Sala(bibliotecas[0], "Auditorio 2", 50))
    bibliotecas[0].añadir_sala(Sala(bibliotecas[0], "Auditorio 3", 10))
    bibliotecas[1].añadir_sala(Sala(bibliotecas[1], "Auditorio 4", 150))
    bibliotecas[1].añadir_sala(Sala(bibliotecas[1], "Auditorio 5", 30))
    bibliotecas[1].añadir_sala(Sala(bibliotecas[1], "Auditorio 6", 60))


    # Copias sede Medellin
    bibliotecas[0].añadir_copia(Copia(0, libros[0], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(1, libros[0], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(2, libros[1], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(3, libros[2], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(4, libros[3], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(5, libros[3], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(6, libros[4], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(7, libros[7], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(8, libros[10], bibliotecas[0]))
    bibliotecas[0].añadir_copia(Copia(9, libros[13], bibliotecas[0]))

    #Copias sede Bogota
    bibliotecas[1].añadir_copia(Copia(0, libros[0], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(1, libros[1], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(2, libros[2], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(3, libros[5], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(4, libros[6], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(5, libros[7], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(6, libros[7], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(7, libros[10], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(8, libros[11], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(9, libros[11], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(10, libros[12], bibliotecas[1]))
    bibliotecas[1].añadir_copia(Copia(11, libros[13], bibliotecas[1]))

    #PCs a sede Medellin
    bibliotecas[0].añadir_pc(PC(computadores[0], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[0], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[0], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[1], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[1], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[1], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[2], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[2], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))
    bibliotecas[0].añadir_pc(PC(computadores[3], True, bibliotecas[0]))

    #Pcs a sede Bogota

    bibliotecas[1].añadir_pc(PC(computadores[0], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[1], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[2], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[2], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[3], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[3], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[5], True, bibliotecas[1]))
    bibliotecas[1].añadir_pc(PC(computadores[5], True, bibliotecas[1]))

    user = Usuario()
    user.get_prestamos().append(Prestamo(user, Copia(12, libros[2], bibliotecas[1]), "Particular", date.today(), date(2023, 12, 31), bibliotecas[1]))
    user.get_prestamos().append(Prestamo(user, PC(computadores[2], True, bibliotecas[1]), "Particular", date.today(), date(2023, 12, 31), bibliotecas[0]))

    user.get_multas().append(Multa("Retraso", date.today(), user, 3000))
    user.get_multas().append(Multa("Uso indebido", date.today(), user, 10000))

    sistema.set_autores(autores)
    sistema.set_bibliotecas(bibliotecas)
    sistema.set_computadores(computadores)
    sistema.set_libros(libros)
    sistema.set_user(user)

    
    Serializador.serializar(sistema)
    """
    ventanaInicial(sistema)