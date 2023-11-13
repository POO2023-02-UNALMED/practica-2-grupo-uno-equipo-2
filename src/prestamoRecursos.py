from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry

class PrestamoRecursos(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="#7c9933")
        self.root = root
        self.sistema = sistema
        palabraLibro = StringVar(value="Libro")
        def busquedaBasica():
            for widget in frame4.winfo_children():
                    widget.destroy()
            def computadorOLibro(event):
                if opciones.get() == "Libro":
                    consulta.config(text="Ingrese el titulo del libro a consultar: ")
                else:
                    consulta.config(text="Ingrese el modelo del computador a consultar: ")

            def confirmarExistencia():
                nombre = entrada.get()
                if opciones.get() == "Libro":
                    for libro in sistema.get_libros():
                        if nombre == libro.get_nombre():
                            respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{libro.get_nombre()}'?")
                            if not respuesta: 
                                return 
                            else:
                                reservarRecurso(libro)
                                return
                    return messagebox.showerror("Error", "la biblioteca no cuenta con este recurso")
                else: 
                    for computador in sistema.get_computadores():
                        if nombre == computador.get_nombre():
                            respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{computador.get_nombre()}'?")
                            if not respuesta: 
                                return 
                            else:
                                reservarRecurso(computador)
                                return
                    return messagebox.showerror("Error", "la biblioteca no cuenta con este recurso")
                
            def reservarRecurso(recurso):
                for widget in frame4.winfo_children():
                    widget.destroy()
                sedes = []
                for biblioteca in sistema.get_bibliotecas():
                    for copia in biblioteca.get_copias():
                        if recurso.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                            sedes.append(biblioteca.get_nombre())
                        
                Label(frame4, text="Reserva de recurso", font=("Arial", 30)).grid(row=0, column=0, columnspan=2)
                Label(frame4, text= f"El {recurso.get_tipo_de_recurso()} {recurso.get_nombre()} está disponible en las siguientes sedes: ").grid(row=1,column=0)
                opcionSede = ttk.Combobox(frame4, values=sedes, foreground="black", state="readonly")
                opcionSede.grid(row=2, column=0) 
                sedeSeleccionada = ""
                def selecc(event):
                    global sedeSeleccionada
                    sedeSeleccionada = opcionSede.get()
                opcionSede.bind("<<ComboboxSelected>>", selecc)

                Label(frame4, f"Ingrese la fecha hasta la cual desea realizar el prestamo: ")
                
                                

            

            Label(frame4, text="Seleccione el material que desea consultar: ", fg="black").grid(row=0,column=0)
            opciones = ttk.Combobox(frame4, values=["Libro", "Computador"], textvariable=palabraLibro, foreground="black", state="readonly")
            opciones.grid(row=0,column=1)
            opciones.bind("<<ComboboxSelected>>", computadorOLibro)
            consulta = Label(frame4,text="Ingrese el titulo del libro a consultar: ")
            consulta.grid(row=1,column=0)
            entrada = Entry(frame4)
            entrada.grid(row=1,column=1)

            botonBuscar = Button(frame4, text="Buscar", command= confirmarExistencia)
            botonBuscar.grid(row=2,column=0)
            



        frame4 = Frame(self)
        frame4.grid(row=3,column=0)
        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Consulta de disponibilidad para prestamo", fg="white", bg="#7c9933")
        titulo.pack()
        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        desc =  """
                En esta opcion podras consultar la disponibilidad para prestamo de los diferentes recursos de la biblioteca, 
                usando criterios como Sede, Titulo, Autor, Fecha. Para de esta manera generar un prestamo a nombre del usuario.
                """

        descripcion = Label(frame1, text=desc, fg="white", bg="#7c9933")
        descripcion.pack(anchor="center")

        frame3 = Frame(self, bg="#7c9933")
        frame3.grid(row=2,column=0)
        basica = Button(frame3, text="Busqueda básica", command=busquedaBasica)
        porCriterio = Button(frame3, text= "Busqueda por criterios")
        basica.grid(row=0,column=0, padx=100, pady=15)
        porCriterio.grid(row=0,column=1,padx=100, pady=15)

    
        
        