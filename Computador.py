from .Recurso import Recurso

class Computador(Recurso):
    totalPCs = 0

    def __init__(self, nombre, idRecurso, marca, gama):
        super().__init__(nombre, idRecurso)
        self.marca = marca
        self.gama = gama
        Computador.totalPCs += 1

    def tipo_recurso(self):
        return "Computador"

    def __str__(self):
        return self.get_nombre()

    def get_marca(self):
        return self.marca

    def set_marca(self, marca):
        self.marca = marca

    def get_gama(self):
        return self.gama

    def set_gama(self, gama):
        self.gama = gama

    @staticmethod
    def get_total_pcs():
        return Computador.totalPCs
