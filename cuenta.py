'''7. Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular 
(que es una persona) y cantidad (puede tener decimales). El titular será obligatorio y 
la cantidad es opcional. Crear los siguientes métodos para la clase: 
 Un constructor, donde los datos pueden estar vacíos. 
 Los setters y getters para cada uno de los atributos. 
El atributo no se puede modificar directamente, sólo ingresando o retirando dinero. 
 mostrar(): Muestra los datos de la cuenta. 
 ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es negativa, 
no se hará nada. 
 retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números rojos.'''

from persona import Persona

class Cuenta:
    def __init__(self, titular, cantidad=0.0):
        self.__titular = titular
        self.__cantidad = cantidad

    def get_titular(self):
        return self.__titular

    def get_cantidad(self):
        return self.__cantidad

    def mostrar(self):
        print(f"Titular: {self.__titular.get_nombre()}")
        print(f"Cantidad: {self.__cantidad}")

    def depositar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad


titular = Persona("Ines")
cuenta = Cuenta(titular, 10000.0)
cuenta.mostrar()

cuenta.depositar(5000.0)
cuenta.mostrar()

cuenta.retirar(3000.0)
cuenta.mostrar()
