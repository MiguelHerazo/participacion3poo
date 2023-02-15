
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




#Cree una clase Circulo que tenga las propiedades centro y radio, las cuales se inicializan con parámetros en el constructor. Defina métodos en la clase para calcular el área, el perímetro e indicar si un punto pertenece al círculo o no.
class circulo:
    
#Cree una clase Carta que contenga dos propiedades valor y pinta, las cuales son asignadas solo al momento de la construcción del objeto (se pasan como parámetros en el constructor). Defina 4 constantes que representan los nombres de las 4 pintas que puede tener una carta.
#Cree una clase CuentaBancaria que contenga los siguientes atributos: numero_cuenta, propietarios y balance. Los tres atributos se deben inicializar en el constructor con valores recibidos como parámetros.
#Para la clase CuentaBancaria, cree un método depositar que maneje las acciones de depósito en la cuenta.
#Para la clase CuentaBancaria, cree un método retirar que maneje las acciones de retiro de la cuenta.
#Para la clase CuentaBancaria, cree un método aplicar_cuota_manejo que aplique un porcentaje del 2% sobre el balance de la cuenta
#Para la clase CuentaBancaria, cree un método mostrar_detalles que imprima por consola los detalles de la cuenta bancaria.
