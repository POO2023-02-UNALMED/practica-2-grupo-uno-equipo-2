from tkinter import *

class FieldFrame(Frame):

    def __init__(self, root, tituloCriterios, criterios, tituloValores, valores = None, habilitado = None):
        super().__init__(root, width=200, height=200, bg="white")
        self.root = root
        self.tituloCriterios = tituloCriterios
        self.criterios = criterios
        self.tituloValores = tituloValores
        self.valores = []
        self.entradas = []
        self.habilitado = habilitado

        self.criteriosLabel = Label(self, text= self.tituloCriterios, bg="white")
        self.criteriosLabel.grid(row=0, column=0, padx= 50, pady= 10)

        self.valoresLabel = Label(self, text = self.tituloValores, bg="white")
        self.valoresLabel.grid(row=0, column=1, padx= 50, pady= 10)

        for i in range(len(self.criterios)):
            Label(self, text=self.criterios[i], bg="white").grid(row=(i+1), column = 0)
            valor = Entry(self, width=60)
            valor.grid(row=(i+1), column=1, padx= 50, pady= 10)
            self.entradas.append(valor)

        self.crearBoton("Limpiar campos", self.limpiarEntradas, 1)
        

    def crearBoton(self, texto, comando, col):
        Button(self, text=texto, command= comando).grid(row=(len(self.criterios)+1), column= col, padx= 50, pady= 10)
    
    def limpiarEntradas(self):
        for entrada in self.entradas:
            entrada.delete(0, last=END)

    def getValores(self, criterio):
        index = self.criterios.index(criterio)
        return self.entradas[index].get()
    
    

        


