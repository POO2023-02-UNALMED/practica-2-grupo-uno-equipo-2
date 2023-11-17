from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.paquete2.Prestamo import Prestamo
from datetime import date

class ReservaEvento(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]


        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Reserva de sala para evento", fg="black", bg="white")
        titulo.pack()


        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        descripcion = """
                    En esta opcion podras realizar una reserva de evento en una de las salas de nuestras
                    bibliotecas, ademas de esto, podras reservar material que pueda ser de utilidad en tu evento
                    """
        
        Label(frame2, text=descripcion, bg="white", fg="black").grid(row=0,column=0)

        self.frame3 = Frame(self, bg="white")
        self.frame3.grid(row=2,column=0)
        self.basica = Button(self.frame3, text="Busqueda básica", command=self.funcBusquedaBasica)
        self.porCriterio = Button(self.frame3, text= "Busqueda por criterios", command=self.funcBusquedaPorCriterio)
        self.porLista = Button(self.frame3, text= "Busqueda por lista")
        self.basica.grid(row=0,column=0, padx=50, pady=15)
        self.porCriterio.grid(row=0,column=1,padx=50, pady=15)
        self.porLista.grid(row=0, column=2, padx=50, pady=15)

        """"""


    def reservarSala(self):
        pass

    def funcBusquedaBasica(self):
        self.frame4 = BusquedaBasica(self, self.sistema)
        self.frame4.grid(row=3, column=0)

    def funcBusquedaPorCriterio(self):
        pass

class BusquedaBasica(Frame):
    def __init__(self, root, sistema):
        super().__init__(root, width=1100, height=700, bg="white")
        self.root = root
        self.sistema = sistema
        self.nombreSedes = [biblioteca.get_nombre() for biblioteca in sistema.get_bibliotecas()]
        self.palabraLibro = StringVar(value="Libro")
        Label(self, text= "Seleccione la sede en la que desea realizar su evento: ", bg="white").grid(row=0, column=0)
        self.sedeSel = None 
        self.sedeSelObj = None
        self.salaSelObj = None
        self.salas = ttk.Combobox(self, values=self.nombreSedes, foreground="black", state="readonly")
        self.salas.grid(row=0,column=1)
        self.salas.bind("<<ComboboxSelected>>", func= self.sede)


    def sede(self, event):
        self.sedeSel = self.salas.get()
        for biblioteca in self.sistema.get_bibliotecas():
                if biblioteca.get_nombre() == self.sedeSel:
                  self.sedeSelObj = biblioteca     
        Label(self, text="Las salas disponibles para evento en esta biblioteca son:").grid(row=1, column=0)
        self.opciones = ttk.Combobox(self, values=self.sedeSelObj.get_salas())
        self.opciones.grid(row=1, column=1)
        self.opciones.bind("<<ComboboxSelected>>", func= self.sala)

    def sala(self, evento):
        self.salaSel = self.opciones.get()
        for sala in self.sedeSelObj.get_salas():
                if sala.get_nombre() == self.salaSel:
                  self.salaSelObj = sala
        confirmacion = messagebox.askyesno(title= "Confirmación", message=f"Deseas Reservar el {self.salaSelObj.get_nombre()} con capacidad para {int(self.salaSelObj.get_capacidad())} personas?")
        if not confirmacion:
            return
        Label(self, text="Seleccione el material que desea reservar para el evento: ").grid(row=2, column=0)
        self.opcionMaterial = ttk.Combobox(self, values=["Libro", "Computador"])
        self.opcionMaterial.grid(row=2, column=1)
        self.opcionMaterial.bind("<<ComboboxSelected>>", func= self.reservar)

    def reservar(self, evento):
        opcionEscogida = self.opcionMaterial.get()
        libroSel = None
        if opcionEscogida == "Libro":
            Label(self, text="Ingrese el titulo del libro que desea reservar para su evento: ").grid(row=3, column=0)
            libro = Entry(self)
            libro.grid(row=3,column=1)
            for lib in self.sistema.get_libros():
                if lib.get_nombre() == libro:
                    confirmacion = messagebox.askyesno(title= "Confirmación", message=f"¿Deseas reservar el libro {libro} en tu evento?")
                    if not confirmacion:
                        return
                    else:
                        libroSel = lib
            if not libroSel:
                messagebox.showerror(title="Error", message="El libro no existe")
                return
            for copia in self.sedeSelObj.get_copias():
                if copia.get_nombre() == libroSel.get_nombre:
                    copiaSel = copia
            prestamo = Prestamo(self.sistema.get_user(), "Evento", date.today(), None, self.sedeSelObj)
            self.sistema.get_user().get_prestamos().append(prestamo)
            self.sedeSelObj.get_copais().remove(copiaSel)

        
                
                




