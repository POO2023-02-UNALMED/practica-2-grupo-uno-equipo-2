class Biblioteca:
    totalSedes = 0

    def __init__(self, nombre, sede):
        self.nombre = nombre
        self.sede = sede
        self.salas = []
        self.libros = []
        self.computadores = []
        self.prestamos = []
        self.copias = []
        self.pcs = []
        Biblioteca.totalSedes += 1

    def get_nombre(self):
        return self.nombre

    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_sede(self):
        return self.sede

    def set_sede(self, sede):
        self.sede = sede

    def get_libros(self):
        return self.libros

    def set_libros(self, libros):
        self.libros = libros

    def get_copias(self):
        return self.copias

    def set_copias(self, copias):
        self.copias = copias

    def get_computadores(self):
        return self.computadores

    def set_computadores(self, computadores):
        self.computadores = computadores

    def get_prestamos(self):
        return self.prestamos

    def set_prestamos(self, prestamos):
        self.prestamos = prestamos

    def añadir_sala(self, sala):
        self.salas.append(sala)

    def añadir_copia(self, copia):
        self.copias.append(copia)

    def añadir_pc(self, pc):
        self.pcs.append(pc)

    def get_salas(self):
        return self.salas

    @staticmethod
    def get_total_sedes():
        return Biblioteca.totalSedes

    @staticmethod
    def set_total_sedes(total_sedes):
        Biblioteca.totalSedes = total_sedes

    def hay_copia(self, nombre_libro, proposito):
        estado = False
        for copia in self.copias:
            if copia.get_nombre().lower() == nombre_libro.lower():
                if proposito == "Evento" and copia.is_disponible_evento():
                    estado = True
                elif proposito == "Particular" and copia.is_disponible_particular():
                    estado = True
        return estado

    def hay_pc(self, nombre_computador, proposito):
        estado = False
        for pc in self.pcs:
            if pc.get_nombre().lower() == nombre_computador.lower():
                if proposito == "Evento" and pc.is_disponible_evento():
                    estado = True
                elif proposito == "Particular" and pc.is_disponible_particular():
                    estado = True
        return estado

    def hallar_copia_por_nombre(self, nombre):
        for copia in self.copias:
            if copia.get_nombre().lower() == nombre.lower():
                return copia
        return None

    def hallar_pc_por_nombre(self, nombre):
        for pc in self.pcs:
            if pc.get_nombre().lower() == nombre.lower():
                return pc
        return None

    def lista_copias_unicas(self):
        return list({c.get_nombre(): c for c in self.copias}.values())

    def lista_pcs_unicos(self):
        return list({pc.get_nombre(): pc for pc in self.pcs}.values())

    def remover_copia(self, copia):
        self.copias.remove(copia)

    def remover_pc(self, pc):
        self.pcs.remove(pc)
