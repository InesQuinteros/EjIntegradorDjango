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

class Cuenta(Persona):
    def __init__(self, nombre="", edad=0, dni="", cantidad=0.0):
        super().__init__(nombre, edad, dni)
        self.__cantidad = cantidad
    
    def get_titular(self):
        return Persona().mostrar()

    @property
    def cantidad(self, cantidad):
        return self.__cantidad

    def mostrar(self):
        return f"Titular: {self.nombre} Cantidad: {self.__cantidad}"
    
    def depositar(self, cantidad):
        if cantidad > 0:
            self.__cantidad += cantidad

    def retirar(self, cantidad):
        self.__cantidad -= cantidad

print ("-----------------cuenta-----------")
c1 = Cuenta("NombreCuenta",22,"22222222",45 )
print (c1.mostrar())
c1.nombre="Cande"
c1.depositar(100)
print (c1.nombre)
print (c1.mostrar())
c1.retirar(25)
print (c1.mostrar())
