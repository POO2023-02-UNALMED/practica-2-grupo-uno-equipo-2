from .Computador import Computador
from .Prestable import Prestable

class PC(Computador, Prestable):
    def __init__(self, modelo, estado, sede):
        super().__init__(modelo.get_nombre(), modelo.get_id_recurso(), modelo.get_marca(), modelo.get_gama())
        self.modelo = modelo
        self.disponibleEvento = True
        self.disponibleParticular = True
        self.sede = sede

    def get_modelo(self):
        return self.modelo

    def set_modelo(self, modelo):
        self.modelo = modelo

    def is_disponible_evento(self):
        return self.disponibleEvento

    def is_disponible_particular(self):
        return self.disponibleParticular

    def set_disponible_evento(self, disponibleEvento):
        self.disponibleEvento = disponibleEvento

    def set_disponible_particular(self, disponibleParticular):
        self.disponibleParticular = disponibleParticular

    def get_sede(self):
        return self.sede

    def set_sede(self, sede):
        self.sede = sede

    def is_prestado(self):
        return not (self.disponibleEvento and self.disponibleParticular)

    def get_id(self):
        return self.get_id_recurso()

    def tipo_recurso(self):
        return "PC"