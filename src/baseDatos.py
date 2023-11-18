import tkinter as tk
from tkinter import Frame, Label, messagebox
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
                self.campos.append(tk.Label(frame, text="Nombre del libro:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="ID del recurso:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="ISBN:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Autor:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Año:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

            elif recurso == 'Copia':
                # Crea y empaqueta los campos de entrada para agregar una copia
                self.campos.append(tk.Label(frame, text="ID de la copia:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Libro:"))  # Esto debería ser una lista desplegable con todos los libros
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Ubicación:"))  # Esto debería ser una lista desplegable con todas las sedes
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

            elif recurso == 'Computador':
                # Crea y empaqueta los campos de entrada para agregar un computador
                self.campos.append(tk.Label(frame, text="Nombre del computador:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="ID del recurso:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Marca:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Gama:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

            elif recurso == 'PC':
                # Crea y empaqueta los campos de entrada para agregar un PC
                self.campos.append(tk.Label(frame, text="ID del PC:"))
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Modelo:"))  # Esto debería ser una lista desplegable con todos los computadores
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

                self.campos.append(tk.Label(frame, text="Ubicación:"))  # Esto debería ser una lista desplegable con todas las sedes
                self.campos[-1].pack()
                self.campos.append(tk.Entry(frame))
                self.campos[-1].pack()

        # tk.Button(frame3, text='Ejecutar', command=self.ejecutar).pack()
    
    def kill(self, frame):
        if frame.winfo_children():
            for widget in frame.winfo_children():
                    widget.destroy()

    """
        def __init__(self, root, sistema):
        self.bibliotecas = sistema.get_bibliotecas()
        self.crear_interfaz()

    def crear_interfaz(self):
        self.sede_var = tk.StringVar()
        self.accion_var = tk.StringVar()
        self.recurso_var = tk.StringVar()

        frame = tk.Frame(self.root, height=70, width=500, bg="white", borderwidth=10, highlightthickness=3, highlightbackground="#7c9933")
        frame.pack()

        tk.Label(frame, text="Sede:").pack()
        tk.OptionMenu(frame, self.sede_var, *['Medellín', 'Bogotá']).pack()

        tk.Label(frame, text="Acción:").pack()
        tk.Radiobutton(frame, text='Agregar', variable=self.accion_var, value='Agregar').pack()
        tk.Radiobutton(frame, text='Eliminar', variable=self.accion_var, value='Eliminar').pack()

        tk.Label(frame, text="Recurso:").pack()
        tk.OptionMenu(frame, self.recurso_var, *['Libro', 'Copia', 'Computador', 'PC']).pack()

        tk.Button(frame, text='Ejecutar', command=self.ejecutar).pack()


    def ejecutar(self):
        sede = self.sede_var.get()
        accion = self.accion_var.get()
        recurso = self.recurso_var.get()
        biblioteca = next((b for b in self.bibliotecas if b.get_sede() == sede), None)
        if biblioteca:
            if accion == 'Agregar':
                if recurso == 'Libro':
                    biblioteca.agregar_libro(Recurso(recurso))
                elif recurso == 'Copia':
                    biblioteca.agregar_copia(Recurso(recurso))
                elif recurso == 'Computador':
                    biblioteca.agregar_computador(Recurso(recurso))
                elif recurso == 'PC':
                    biblioteca.agregar_pc(Recurso(recurso))
                messagebox.showinfo('Información', f'Se agregó un {recurso} a la biblioteca de {sede}')
            elif accion == 'Eliminar':
                if recurso == 'Libro':
                    recurso_a_eliminar = next((r for r in biblioteca.libros if r.tipo == recurso), None)
                    if recurso_a_eliminar:
                        biblioteca.eliminar_libro(recurso_a_eliminar)
                elif recurso == 'Copia':
                    recurso_a_eliminar = next((r for r in biblioteca.copias if r.tipo == recurso), None)
                    if recurso_a_eliminar:
                        biblioteca.eliminar_copia(recurso_a_eliminar)
                elif recurso == 'Computador':
                    recurso_a_eliminar = next((r for r in biblioteca.computadores if r.tipo == recurso), None)
                    if recurso_a_eliminar:
                        biblioteca.eliminar_computador(recurso_a_eliminar)
                elif recurso == 'PC':
                    recurso_a_eliminar = next((r for r in biblioteca.pcs if r.tipo == recurso), None)
                    if recurso_a_eliminar:
                        biblioteca.eliminar_pc(recurso_a_eliminar)
                if recurso_a_eliminar:
                    messagebox.showinfo('Información', f'Se eliminó un {recurso} de la biblioteca de {sede}')
                else:
                    messagebox.showerror('Error', f'No hay {recurso} en la biblioteca de {sede} para eliminar')

"""