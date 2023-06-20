from clase_nodo import Nodo
class Lista:
    __comienzo: Nodo
    def __init__(self):
        self.__comienzo = None
    def insertar_inmueble(self, posicion, inmueble):
        self.__comienzo = Nodo(inmueble)
        aux = self.__comienzo
        while aux is not None:
            if posicion > aux and posicion is not None:
                aux.set_siguiente(inmueble)
                aux = aux.get_siguiente()
    def agregar_inmueble(self, inmueble):
        self.__comienzo = Nodo(inmueble)
        aux = self.__comienzo
        while aux is not None:
            if aux.get_siguiente() is None:
                aux.set_siguiente(inmueble)
                aux = aux.get_siguiente()
    def mostrar_datos_ventas(self, dormitorios):
        aux = self.__comienzo
        while aux is not None:
            if dormitorios > type(aux.get_datos().get_dormitorio()):
                print(type(float(aux.get_datos().importe_venta())))
                print(type(aux.get_datos()))
                aux = aux.get_siguiente()
    def coleccion(self):
        d =dict()
        aux = self.__comienzo
        while aux is not None:
            d = ({'direccion': f'{type(aux.get_datos().get_direccion())}','superficie': f'{type(aux.get_datos().get_superficie())}','importe' : f'{type(aux.get_datos().importe_venta())}'})
            print(d)
    def get_info(self):
        return self.__comienzo.get_datos().importe_venta()