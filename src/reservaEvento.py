from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from gestorAplicacion.paquete2.Prestamo import Prestamo
from datetime import date
from FieldFrame import FieldFrame

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
        self.frame4 = Frame(self)



    def reservarSala(self):
        pass

    def funcBusquedaBasica(self):
        self.kill(self.frame4)
        self.frame4 = BusquedaBasica(self, self.sistema)
        self.frame4.grid(row=3, column=0)

    def funcBusquedaPorCriterio(self):
        self.kill(self.frame4)
        self.frame4 = BusquedaPorCriterio(self, self.sistema)
        self.frame4.grid(row=3, column=0)


    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

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
        self.opcionMaterial.bind("<<ComboboxSelected>>", func= self.buscar)

    def buscar(self, evento):
        opcionEscogida = self.opcionMaterial.get()
        self.lab = Label(self, text="")
        self.lab.grid(row=3, column=0)
        if opcionEscogida == "Libro":
            self.lab.config(text="Ingrese el titulo del libro que desea reservar: ")
            self.libro = Entry(self)
            self.libro.grid(row=3,column=1)
            Button(self, text= "Buscar", command= self.reservarLibro).grid(row=4, column=0)
        else:
            self.lab.config(text="Ingrese el modelo del computador que desea reservar: ")
            self.computador = Entry(self)
            self.computador.grid(row=3,column=1)
            Button(self, text= "Buscar", command= self.reservarComputador).grid(row=4, column=0)
            

    def reservarLibro(self):
        libroSel = None 
        for lib in self.sistema.get_libros():
                if lib.get_nombre() == self.libro.get():
                    confirmacion = messagebox.askyesno(title= "Confirmación", message=f"¿Deseas reservar el libro {self.libro.get()} en tu evento?")
                    if not confirmacion:
                        return
                    else:
                        libroSel = lib
        if not libroSel:
            messagebox.showerror(title="Error", message="El libro no existe")
            return
        for copia in self.sedeSelObj.get_copias():
            if copia.get_nombre() == libroSel.get_nombre():
                copiaSel = copia
        prestamo = Prestamo(self.sistema.get_user(), "Evento", date.today(), None, self.sedeSelObj)
        self.sistema.get_user().get_prestamos().append(prestamo)
        self.sedeSelObj.get_copias().remove(copiaSel)

    def reservarComputador(self):
        computadorSel = None 
        for pc in self.sistema.get_computadores():
                if pc.get_nombre() == self.computador.get():
                    confirmacion = messagebox.askyesno(title= "Confirmación", message=f"¿Deseas reservar el computador {self.computador.get()} en tu evento?")
                    if not confirmacion:
                        return
                    else:
                        computadorSel = pc
        if not computadorSel:
            messagebox.showerror(title="Error", message="El computador no existe")
            return
        for pc in self.sedeSelObj.get_PCs():
            if pc.get_nombre() == computadorSel.get_nombre():
                pcSel = pc
        prestamo = Prestamo(self.sistema.get_user(), "Evento", date.today(), None, self.sedeSelObj)
        self.sistema.get_user().get_prestamos().append(prestamo)
        self.sedeSelObj.get_PCs().remove(pcSel)
        messagebox.askokcancel(title="Reserva realizada", message="¡Reserva realizada con exito! Mucha suerte en tu evento :)")


class BusquedaPorCriterio(Frame):
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
        self.opcionMaterial.bind("<<ComboboxSelected>>", func= self.buscar)

    def buscar(self, evento):
        self.frameCriterios = FieldFrame(self, "Criterios", ["hola", "chao"], "Valor")
        self.frameCriterios.grid(row=3, column=0, columnspan=2)

                




