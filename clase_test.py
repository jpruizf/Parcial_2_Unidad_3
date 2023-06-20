import unittest
from clase_lista import Lista
from clase_inmueble import Inmueble
class Test(unittest.TestCase):
    def menu(self):
        lista = Lista()
        print("1. Insertar inmueble")
        print("2. Agregar inmueble")
        print("3. Ver datos inmuebles")
        print("4. Ver datos en detalles de los inmuebles a la venta")
        print("5. Testear funcion importe de venta")
        opcion = input("Seleccione una de las opciones dadas: ")
        while opcion !='0':
            if opcion == '1':
                posicion = int(input("Posicion >> "))
                inmueble = Inmueble()
                lista.insertar_inmueble(posicion,inmueble)
            elif opcion == '2':
                inmueble = Inmueble()
                lista.agregar_inmueble(inmueble)
            elif opcion == '3':
                cant_dormitorios = int(input("Cantidad de dormitorios >> "))
                lista.mostrar_datos_ventas(cant_dormitorios)
            elif opcion == '4':
                lista.coleccion()
            elif opcion == '5':
                self.assertEqual(lista.get_info(),7000000)
            print("1. Insertar inmueble")
            print("2. Agregar inmueble")
            print("3. Ver datos inmuebles")
            print("4. Ver datos en detalles de los inmuebles a la venta")
            print("5. Testear funcion importe de venta")