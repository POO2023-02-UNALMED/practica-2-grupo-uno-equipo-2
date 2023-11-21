from .Biblioteca import Biblioteca
from .Sala import Sala
from .Recurso import Recurso

class Evento:
    tipos = ["CHARLA", "PRESENTACION", "ESTUDIO"]

    def __init__(self, tipo, sede, sala):
        self.tipo = Evento.tipos[tipo]
        self.biblioteca = sede
        self.sala = sala
        self.material = []

    def get_biblioteca(self):
        return self.biblioteca

    def get_material(self):
        return self.material

    def get_sala(self):
        return self.sala

    def get_tipo(self):
        return self.tipo

    def set_biblioteca(self, biblioteca):
        self.biblioteca = biblioteca

    def set_material(self, material):
        self.material = material

    def set_sala(self, sala):
        self.sala = sala

    def set_tipo(self, tipo):
        self.tipo = tipo

    @staticmethod
    def get_tipos():
        return Evento.tipos
