import tkinter as tk
from tkinter import Frame, Label, messagebox
from FieldFrame import FieldFrame
from gestorAplicacion.paquete2.Sistema import *
from gestorAplicacion.paquete1.Biblioteca import *
from gestorAplicacion.paquete1.Recurso import *
from gestorAplicacion.paquete1.Libro import *
from gestorAplicacion.paquete1.Computador import *
from gestorAplicacion.paquete1.Copia import *
from gestorAplicacion.paquete1.PC import *

class BaseDeDatos(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema

        self.sede_var = tk.StringVar()
        self.accion_var = tk.StringVar()
        self.recurso_var = tk.StringVar()

        frame1 = Frame(self, bg="#7c9933")
        frame1.grid(row=0, column=0)
        titulo = Label(frame1, text="Gestión de Base de Datos", fg="black", bg="white")
        titulo.pack()


        frame2 = Frame(self)
        frame2.grid(row=1,column=0)
        descripcion = """
                    En este apartado podrás realizar cambios en la Base de Datos
                    de la biblioteca, añadiendo o eliminando recursos.
                    """
        
        Label(frame2, text=descripcion, bg="white", fg="black").grid(row=0,column=0)

        frame3 = Frame(self, bg="white")
        frame3.grid(row=2, column=0)
        tk.Label(frame3, text="Sede:", bg="white").pack()
        tk.OptionMenu(frame3, self.sede_var, *['Medellín', 'Bogotá']).pack()

        tk.Label(frame3, text="Acción:").pack()
        tk.Radiobutton(frame3, text='Agregar', variable=self.accion_var, value='Agregar').pack()
        tk.Radiobutton(frame3, text='Eliminar', variable=self.accion_var, value='Eliminar').pack()

        tk.Label(frame3, text="Recurso:").pack()
        tk.OptionMenu(frame3, self.recurso_var, *['Libro', 'Copia', 'Computador', 'PC']).pack()

        self.campos = []  # Esta lista almacenará los campos de entrada actuales

        self.accion_var.trace('w', lambda *args: self.actualizar_campos(frame3))
        self.recurso_var.trace('w', lambda *args: self.actualizar_campos(frame3))

        frame4 = Frame(self, bg="white")
        frame4.grid(row=3, column=0)
        tk.Button(frame4, text='Ejecutar', command= lambda: self.ejecutar_cambio()).pack()

    def ejecutar_cambio(self):
        accion = self.accion_var.get()
        recurso = self.recurso_var.get()

        if accion == "Agregar":
            if recurso == "Libro":
                pass
            elif recurso == "Copia":
                pass
            elif recurso == "Computador":
                pass
            elif recurso == "PC":
                pass
        elif accion == "Eliminar":
            if recurso == "Libro":
                pass
            elif recurso == "Copia":
                pass
            elif recurso == "Computador":
                pass
            elif recurso == "PC":
                pass

    def actualizar_campos(self, frame):
        # Elimina los campos de entrada actuales
        for campo in self.campos:
            campo.destroy()
        self.campos = []

        accion = self.accion_var.get()
        recurso = self.recurso_var.get()

        if accion == 'Agregar':
            if recurso == 'Libro':
                # Crea y empaqueta los campos de entrada para agregar un libro
                self.campos.append(Agregar(frame, "Criterios", ["Nombre", "ID", "ISBN", "Autor", "Año"], "Valor", self.sistema, "Libro"))
                self.campos[-1].crearBoton("Aceptar", self.comprobar, 0)
                self.campos[-1].crearBoton("Borrar", self.comprobar, 1)
                self.campos[-1].pack()

            elif recurso == 'Copia':
                # Crea y empaqueta los campos de entrada para agregar una copia
                self.campos.append(Agregar(frame, "Criterios", ["ID", "Libro", "Ubicación"], "Valor", self.sistema, "Copia"))
                self.campos[-1].crearBoton("Aceptar", self.comprobar, 0)
                self.campos[-1].crearBoton("Borrar", self.comprobar, 1)
                self.campos[-1].pack()

            elif recurso == 'Computador':
                # Crea y empaqueta los campos de entrada para agregar un computador
                self.campos.append(Agregar(frame, "Criterios", ["Nombre", "ID", "Marca", "Gama"], "Valor", self.sistema, "Computador"))
                self.campos[-1].crearBoton("Aceptar", self.comprobar, 0)
                self.campos[-1].crearBoton("Borrar", self.comprobar, 1)
                self.campos[-1].pack()

            elif recurso == 'PC':
                # Crea y empaqueta los campos de entrada para agregar un PC
                self.campos.append(Agregar(frame, "Criterios", ["ID", "Modelo", "Ubicacion"], "Valor", self.sistema, "PC"))
                self.campos[-1].crearBoton("Aceptar", self.comprobar, 0)
                self.campos[-1].crearBoton("Borrar", self.comprobar, 1)
                self.campos[-1].pack()

        elif accion == "Eliminar":
            if recurso == "Libro":
                self.campos.append(tk.Label(frame, text="Seleccione Libro a Eliminar, Esto Eliminará Todas Sus Copias"))  # Esto debería ser una lista desplegable con todos los computadores
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()
            elif recurso == "Copia":
                self.campos.append(tk.Label(frame, text="Seleccione Copia a Eliminar"))  # Esto debería ser una lista desplegable con todos los computadores
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()
            elif recurso == "Computador":
                self.campos.append(tk.Label(frame, text="Seleccione Computador a Eliminar, Esto Eliminará Los PC De Este Modelo"))  # Esto debería ser una lista desplegable con todos los computadores
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()
            elif recurso == "PC":
                self.campos.append(tk.Label(frame, text="Seleccione PC a Eliminar"))  # Esto debería ser una lista desplegable con todos los computadores
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()
        # tk.Button(frame3, text='Ejecutar', command=self.ejecutar).pack()
    
    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

    def comprobar(self):
        pass

class Agregar(FieldFrame):
    def __init__(self, root, criteriosTitulo, lista, valorTitulo, sistema, recurso):
        super().__init__(root, criteriosTitulo, lista, valorTitulo)
        self.sistema = sistema
        self.recurso = recurso
        