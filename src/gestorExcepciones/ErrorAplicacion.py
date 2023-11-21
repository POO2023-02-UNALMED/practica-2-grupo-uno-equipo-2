class ErrorAplicacion(Exception):
    def __init__(self, error):
        self.error = "Error en la aplicacion: " + error
    
    def getError(self):
        return self.error