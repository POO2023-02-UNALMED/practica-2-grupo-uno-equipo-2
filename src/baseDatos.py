import tkinter as tk
from tkinter import Frame, Label, messagebox
from gestorAplicacion.paquete2.Sistema import *
from gestorAplicacion.paquete1.Biblioteca import *
from gestorAplicacion.paquete1.Recurso import *
from gestorAplicacion.paquete1.Libro import *
from gestorAplicacion.paquete1.Computador import *
from gestorAplicacion.paquete1.Copia import *
from gestorAplicacion.paquete1.PC import *

class BaseDatos(Frame):

    def __init__(self, root, sistema):
        super().__init__(root, height=70,width=500,bg="white", borderwidth = 10, highlightthickness=3, highlightbackground="#7c9933")
        self.root = root
        self.sistema = sistema

        self.sede_var = tk.StringVar()
        self.accion_var = tk.StringVar()
        self.recurso_var = tk.StringVar()

        self.frame = tk.Frame(self.root, height=70, width=500, bg="white", borderwidth=10, highlightthickness=3, highlightbackground="#7c9933")
        self.frame.grid(row=0, column=0)

        tk.Label(self.frame, text="Sede:").pack()
        tk.OptionMenu(self.frame, self.sede_var, *['Medellín', 'Bogotá']).pack()

        tk.Label(self.frame, text="Acción:").pack()
        tk.Radiobutton(self.frame, text='Agregar', variable=self.accion_var, value='Agregar').pack()
        tk.Radiobutton(self.frame, text='Eliminar', variable=self.accion_var, value='Eliminar').pack()

        tk.Label(self.frame, text="Recurso:").pack()
        tk.OptionMenu(self.frame, self.recurso_var, *['Libro', 'Copia', 'Computador', 'PC']).pack()

        tk.Button(self.frame, text='Ejecutar', command=self.ejecutar).pack()
    
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