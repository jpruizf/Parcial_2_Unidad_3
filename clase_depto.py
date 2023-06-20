from clase_inmueble import Inmueble

class Departamento(Inmueble):
    __dormitorio: int
    __num_monoblock: int
    __num_depto: int
    __num_piso: int
    def __init__(self):
        super().__init__()
        self.__dormitorio = 0
        self. __num_monoblock = 0
        self.__num_depto = 0
        self.__num_piso = 0
    def get_dormitorio(self):
        '''retorna cantidad de dormitorios'''
        return self.__dormitorio
    def get_atributos(self):
        '''retorna todos los atributos'''
        return f"numero de monoblock {self.__num_monoblock}||numero de departamento {self.__num_depto}||piso {self.__num_piso}"
    def precio_construccion(self):
        '''retorna precio de contruccion'''
        return self.get_dormitorio() * 1700