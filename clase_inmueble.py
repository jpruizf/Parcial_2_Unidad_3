class Inmueble:
    __localidad: str
    __direccion: str
    __superficie: float
    def __init__(self):
        self.__localidad = ""
        self.__direccion = ""
        self.__superficie = 0.0
    def get_superficie(self):
        return self.__superficie
    def get_info(self):
        return f"localidad: {self.__localidad}|| direccion: {self.__direccion}"