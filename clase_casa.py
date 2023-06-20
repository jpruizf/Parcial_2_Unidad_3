from clase_inmueble import Inmueble

class Casa(Inmueble):
    __metros: float
    def __init__(self):
        super().__init__()
        self.__metros = 0.0
    def get_metros(self):
        '''retorna los metros cuadrados'''
        return self.__metros
    def precio_contruccion(self):
        '''retorna precio construccion'''
        return self.get_metros() * 1.80 * 2000