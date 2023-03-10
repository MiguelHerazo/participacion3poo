import math
#Cree una clase Vehículo que contenga los atributos de instancia velocidad_maxima y kilometraje.



class vehiculo:
    def __init__(self, velocidad_maxima:float, kilometraje: int):
        self.velocidad_maxima = velocidad_maxima
        self.kilometraje = kilometraje

#Cree una clase Punto que represente un punto en el plano cartesiano.

class Punto:
    def puntoc(self, x, y):
        self.x: int = x
        self.y: int = y

#A la clase del punto anterior, defínale los siguientes métodos:
#- Un método mostrar que imprima por consola las coordenadas del punto
    def mostrarp(self,x, y):
        print(f"El Punto se encuentra en las coordenadas {x}:{y}")
#- Un método mover que cambie las coordenadas del punto

    def mover(self, x,x2,y,y2):
        self.x2 :int = x + 2
        self.y2 :int = y + 5

#- Un método calcular_distancia que calcule la distancia de la instancia actual con otro punto.
    def calculardistancia(self):
        distanciax = (self.x2 - self.x)
        distanciay = (self.y2 - self.y)
        return  distanciax, distanciay


#Cree una clase Rectángulo la cual contiene dos atributos de instancia que representan los puntos que definen sus esquinas. Agregue métodos a la clase Rectángulo para calcular su perímetro, calcular su área e indicar si el rectángulo es un cuadrado.
class Rectangulo:
    def esquinas(self,x1: int,y1:int,x2:int,y2:int):
        self.x1:int = x1
        self.y1:int = y1
        self.x2:int = x2
        self.y2:int = y2

    def perimetro(self,x1,x2,y1,y2):
        distanciax = (self.x2 - self.x1)
        distanciay = (self.y2 - self.y1)
        return (distanciax * 2) + (distanciay * 2)

    def area(self,x1,x2,y1,y2):
        distanciax = (self.x2 - self.x1)
        distanciay = (self.y2 - self.y1)
        return distanciax * distanciay

    def es_cuadrado(self,x1,x2,y1,y2):
        distanciax = (self.x2 - self.x1)
        distanciay = (self.y2 - self.y1)
        if distanciax == distanciay:
            return 'es cuadrado'
        else:
            return "no es cuadrado"

#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
class circulo:
    def __init__(self, centro:int, radio:int):
        self.centro = centro
        self.radio = radio

    def areaciruculo(self, radio):
        return math.pi * (radio * radio)

    def perimetro(self,radio):
        return (2 * math.pi) * radio

    def pertenece(self, punto, radio):
        pass



#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
class Carta:

#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
class CuentaBancaria:

    def __int__(self, numero_cuenta, propietario, balance):
        self.numero_cuenta = numero_cuenta
        self.propietario = propietario
        self.balance = balance

    def depositar(self):

    def retirar(self):

    def aplicar_cuota_manejo(self,balance):
      

    def mostrar_detalles(self):
