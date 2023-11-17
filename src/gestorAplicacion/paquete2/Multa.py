from datetime import date

class Multa:
    numero_multas = 0  # Variable de clase para llevar un registro del número de multas

    def __init__(self, tipo, fecha_impuesta, usuario):
        self.id_multa = Multa.numero_multas
        self.tipo = tipo
        self.fecha_impuesta = fecha_impuesta
        self.usuario = usuario
        Multa.numero_multas += 1

    def get_id_multa(self):
        return self.id_multa

    def get_tipo(self):
        return self.tipo

    def set_tipo(self, tipo):
        self.tipo = tipo

    def get_fecha_impuesta(self):
        return self.fecha_impuesta

    def get_usuario(self):
        return self.usuario

    def pagar_multa(self):
        # Eliminar la multa del registro del usuario
        self.usuario.eliminar_multa(self)
        # Notificar al usuario sobre el pago exitoso de la multa
        return f"La multa de ID: {self.id_multa} con tipo '{self.tipo}' y Fecha {self.fecha_impuesta} ha sido pagada."
