from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
from datetime import date
from gestorAplicacion.paquete2.Prestamo import Prestamo
from FieldFrame import FieldFrame

class PrestamoRecursos(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema
        

        self.frame1 = Frame(self, bg="white", borderwidth = 1, highlightbackground = "#7c9933", highlightcolor= "#7c9933")
        self.frame1.grid(row=0, column=0)
        self.titulo = Label(self.frame1, text="Consulta de disponibilidad para prestamo", fg="black", bg="white")
        self.titulo.pack()
        self.frame2 = Frame(self, highlightbackground = "#7c9933")
        self.frame2.grid(row=1,column=0)
        self.desc =  """
                En esta opcion podras consultar la disponibilidad para prestamo de los diferentes recursos de la biblioteca, 
                usando criterios como Sede, Titulo, Autor, Fecha. Para de esta manera generar un prestamo a nombre del usuario.
                """

        self.descripcion = Label(self.frame1, text=self.desc, fg="black", bg="white")
        self.descripcion.pack(anchor="center")

        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row=2,column=0)


        self.basica = Button(self.frame3, text="Busqueda básica", command=self.funcBusquedaBasica)
        self.porCriterio = Button(self.frame3, text= "Busqueda por criterios", command=self.funcBusquedaPorCriterio)
        self.porLista = Button(self.frame3, text= "Busqueda por lista")
        self.basica.grid(row=0,column=0, padx=50, pady=15)
        self.porCriterio.grid(row=0,column=1,padx=50, pady=15)
        self.porLista.grid(row=0, column=2, padx=50, pady=15)
        self.frame4 = busquedaBasica(self, self.sistema)
        self.frame4.grid(row = 3, column=0)
    def funcBusquedaBasica(self):
        self.kill(self.frame4)
        self.frame4 = busquedaBasica(self, self.sistema)
        self.frame4.grid(row = 3, column=0)

    def funcBusquedaPorCriterio(self):
        self.palabraLibro = StringVar(value="Libro")
        self.kill(self.frame4)
        self.opciones = ttk.Combobox(self.frame4, values=["Libro", "Computador"], textvariable=self.palabraLibro, foreground="white", state="readonly")
        self.opciones.grid(row=0,column=1)
        self.seleccione = Label(self.frame4, text="Seleccione el material que desea consultar: ", bg="white", fg="black")
        self.seleccione.grid(row=0,column=0)
        

        def computadorOLibro(evento):
            if self.opciones.get() == "Libro":
                self.kill(self.frame4)
                self.frame4 = busquedaPorCriterio(self, "Criterios", ["Nombre", "ID", "ISBN", "Autor", "Año"], "Valor", self.sistema, "Libro")
                self.frame4.grid(row=3, column=0)
            else:
                self.kill(self.frame4)
                self.frame4 = busquedaPorCriterio(self, "Criterios", ["Modelo", "ID", "Marca", "Gama"], "Valor", self.sistema, "Computador")
                self.frame4.grid(row=3, column=0)
        self.opciones.bind("<<ComboboxSelected>>", computadorOLibro)


    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()


class busquedaBasica(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white", highlightbackground = "#7c9933", highlightcolor= "#7c9933")
        self.root = root
        self.sistema = sistema
        self.palabraLibro = StringVar(value="Libro")
        self.seleccione = Label(self, text="Seleccione el material que desea consultar: ", bg="white", fg="black")
        self.seleccione.grid(row=0,column=0)
        def computadorOLibro(evento):
            if self.opciones.get() == "Libro":
                self.consulta.config(text="Ingrese el titulo del libro a consultar: ")
            else:
                self.consulta.config(text="Ingrese el modelo del computador a consultar: ")
        self.opciones = ttk.Combobox(self, values=["Libro", "Computador"], textvariable=self.palabraLibro, foreground="white", state="readonly")
        self.opciones.grid(row=0,column=1)
        self.opciones.bind("<<ComboboxSelected>>", computadorOLibro)
        self.consulta = Label(self,text="Ingrese el material a consultar: ", bg="white", fg="black")
        self.consulta.grid(row=1,column=0)
        self.entrada = Entry(self)
        self.entrada.grid(row=1,column=1)

        self.botonBuscar = Button(self, text="Buscar", command= self.confirmarExistencia)
        self.botonBuscar.grid(row=2,column=0)

    
    def confirmarExistencia(self):
        nombre = self.entrada.get()
        if self.opciones.get() == "Libro":
            for libro in self.sistema.get_libros():
                if nombre == libro.get_nombre():
                    respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{libro.get_nombre()}'?")
                    if not respuesta: 
                        return 
                    else:
                        self.reservarRecurso(libro)
                        return
            return messagebox.showerror("Error", "la biblioteca no cuenta con este recurso")
        else: 
            for computador in self.sistema.get_computadores():
                if nombre == computador.get_nombre():
                    respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{computador.get_nombre()}'?")
                    if not respuesta: 
                        return 
                    else:
                        self.reservarRecurso(computador)
                        return
            return messagebox.showerror("Error", "la biblioteca no cuenta con este recurso")
        

    def reservarRecurso(self, recurso):
            sedes = []
            for biblioteca in self.sistema.get_bibliotecas():
                for copia in biblioteca.get_copias():
                    if recurso.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                        sedes.append(biblioteca.get_nombre())

            Label(self, text="Reserva de recurso", font=("Arial", 30), bg="white", fg="black").grid(row=3, column=0, columnspan=2)
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black").grid(row=4,column=0, columnspan=2)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
            opcionSede.grid(row=5, column=0, columnspan=2) 
            sedeSeleccionada = None                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black")
            hur.grid(row=6,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=7,column=0, columnspan=2)

            fechaSeleccionada = None
            def seleccionarFecha(event):
                global fechaSeleccionada
                fechaSeleccionada = cal.get_date()
            cal.bind("<<CalendarSelected>>", seleccionarFecha)

            def realizarReserva():
                sedeSel = opcionSede.get()
                for sede in self.sistema.get_bibliotecas():
                    if sede.get_nombre() == sedeSel:
                        sedeSel = sede
                for copia in sedeSel.get_copias():
                    if copia.get_nombre() == recurso.get_nombre():
                        copiaSel = copia 
                self.sistema.get_user().get_prestamos().append(Prestamo(self.sistema.get_user(), "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_copias().remove(copiaSel)
                messagebox.askokcancel(title="Reserva realizada", message="¡Su reserva ha sido realizada con exito! No olvide devolver su recurso :)")
                
            botonReservar = Button(self, text="Reservar", command=realizarReserva)
            botonReservar.grid(row=8, column=0, columnspan=2)


class busquedaPorCriterio(FieldFrame):
    
    def __init__(self, root, criteriosTitulo, lista, valorTitulo, sistema, recurso):
        super().__init__(root, criteriosTitulo, lista, valorTitulo)
        self.sistema = sistema
        self.recurso = recurso
        self.crearBoton("Guardar", self.comprobar, 0)

    def comprobar(self):
        libroSel = None
        computadorSel
        if (len(self.valores) < len(self.criterios)):
            for i in range(len(self.criterios)):
                self.valores.append(self.entradas[i].get())
        print(self.valores)
        if self.recurso == "Libro":
            for libro in self.sistema.get_libros():
                print(libro.get_nombre() + self.valores[0])
                if (libro.get_nombre() == self.valores[0]) and (str(libro.get_id_recurso()) == self.valores[1]) and (libro.get_isbn() == self.valores[2]) and (libro.get_autor().get_nombre() == self.valores[3]) and (str(libro.get_año()) == self.valores[4]):
                    libroSel = libro
                    respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{libroSel.get_nombre()}'?")
                    if not respuesta: 
                        self.valores = []
                        return
            if not libroSel:
                self.valores = []
                return messagebox.showerror("Error", "la biblioteca no cuenta con este recurso")
            self.kill(self)
            self.reservarRecurso(libroSel)
        else: 
            for computador in self.sistema.get_computadores():
                print(computador.get_nombre() + self.valores[0])
                if (computador.get_nombre() == self.valores[0]) and (str(computador.get_id_recurso()) == self.valores[1]) and (computador.get_marca() == self.valores[2]) and (computador.get_gama().get_nombre() == self.valores[3]):
                    computadorSel = computador
                    respuesta = messagebox.askyesno("Confirmar", f"¿Desea reservar '{computadorSel.get_nombre()}'?")
                    if not respuesta: 
                        self.valores = []
                        return
            if not computadorSel:
                self.valores = []
                return messagebox.showerror("Error", "la biblioteca no cuenta con este recurso")
            self.kill(self)
            self.reservarRecurso(computadorSel)

    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()
        

    def reservarRecurso(self, recurso):
            sedes = []
            for biblioteca in self.sistema.get_bibliotecas():
                for copia in biblioteca.get_copias():
                    if recurso.get_nombre() == copia.get_nombre() and biblioteca.get_nombre() not in sedes:
                        sedes.append(biblioteca.get_nombre())

            Label(self, text="Reserva de recurso", font=("Arial", 30), bg="white", fg="black").grid(row=3, column=0, columnspan=2)
            Label(self, text= f"Seleccione la sede en la cual desea realizar el prestamo: ", bg="white", fg="black").grid(row=4,column=0, columnspan=2)
            opcionSede = ttk.Combobox(self, values=sedes, foreground="white", state="readonly")
            opcionSede.grid(row=5, column=0, columnspan=2) 
            sedeSeleccionada = None                            
            hur = Label(self, text= "Ingrese la fecha hasta la cual desea realizar el prestamo: ", bg="white", fg="black")
            hur.grid(row=6,column=0, columnspan=2)
            cal = Calendar(self, mindate=date.today())
            cal.grid(row=7,column=0, columnspan=2)

            fechaSeleccionada = None
            def seleccionarFecha(event):
                global fechaSeleccionada
                fechaSeleccionada = cal.get_date()
            cal.bind("<<CalendarSelected>>", seleccionarFecha)

            def realizarReserva():
                sedeSel = opcionSede.get()
                for sede in self.sistema.get_bibliotecas():
                    if sede.get_nombre() == sedeSel:
                        sedeSel = sede
                for copia in sedeSel.get_copias():
                    if copia.get_nombre() == recurso.get_nombre():
                        copiaSel = copia 
                self.sistema.get_user().get_multas().append(Prestamo(self.sistema.get_user(), "Particular", date.today(), fechaSeleccionada, sedeSel))
                sedeSel.get_copias().remove(copiaSel)
                
            botonReservar = Button(self, text="Reservar", command=realizarReserva)
            botonReservar.grid(row=8, column=0, columnspan=2)

    
    