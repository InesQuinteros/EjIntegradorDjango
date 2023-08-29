'''8. Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase 
CuantaJoven que deriva de la clase creada en el punto 7. 
Cuando se crea esta nueva clase, además del titular y la cantidad se debe guardar 
una bonificación que estará expresada en tanto por ciento. 
Crear los siguientes métodos para la clase: 
 Un constructor. 
 Los setters y getters para el nuevo atributo. 
 En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, 
por lo tanto hay que crear un método es_titular_valido() que devuelve verdadero 
si el titular es mayor de edad pero menor de 25 años y falso en caso contrario. 
 Además, la retirada de dinero sólo se podrá hacer si el titular es válido. 
 El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la cuenta.'''

from cuenta import Cuenta

class CuentaJoven(Cuenta):
    def __init__(self, nombre="", edad=0, dni="", cantidad=0.0, bonificacion=0):
        super().__init__(nombre, edad, dni, cantidad)
        self.__bonificacion= bonificacion

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, bonificacion):
        self.__bonificacion=bonificacion
    
    def es_titular_valido(self):
        if self.edad > 17 and self.edad < 25:
            return True
        else:
            return False
    
    def retirar(self, cantidad):
        if self.es_titular_valido():
            Cuenta().retirar(cantidad)
            return f"El retiro de $ {cantidad} fue efectuado exitosamente"
        else:
            return "El titular no es valido para retirar dinero"
    
    def mostrar(self):
        return f"Cuenta joven. bonificacion {str(self.bonificacion)}"

print ("---------------CuentaJoven------")

cj1=CuentaJoven("Cande", 20, "11223344", 456, 454)
print(cj1.nombre)
print(f"cj1.es_titular_valido() -> {cj1.es_titular_valido()}")
print (f"cj1.mostrar()-> {cj1.mostrar()}")
print (cj1.retirar(12))

cj1=CuentaJoven("Gonza", 15, "11223344", 456, 15.78)
print(cj1.nombre)
print(f"cj1.es_titular_valido() -> {cj1.es_titular_valido()}")
print (f"cj1.mostrar()-> {cj1.mostrar()}")
print (cj1.retirar(12))