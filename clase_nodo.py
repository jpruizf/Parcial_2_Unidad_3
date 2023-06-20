from clase_inmueble import Inmueble

class Nodo:
    __inmueble: Inmueble
    __siguiente: object
    def __init__(self, inmueble):
        self.__inmueble = inmueble
        self.__siguiente = None
    def set_siguiente(self, siguiente):
        self.__siguiente = siguiente
    def get_siguiente(self):
        return self.__siguiente
    def get_datos(self):
        return self.__inmueble