'''
6. Crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construya los siguientes métodos para la clase:
 Un constructor, donde los datos pueden estar vacíos.
 Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.
 mostrar(): Muestra los datos de la persona.
 Es_mayor_de_edad(): Devuelve un valor lógico indicando si es mayor de edad.
'''

class Persona:
    def __init__(self, nombre="", edad=0, dni=""):
        self.__nombre = nombre
        self.__edad = edad
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter    
    def nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de caracteres.")

    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            print("Error: La edad debe ser un número entero no negativo.")

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, dni):
        if isinstance(dni, str) and( len(dni) == 8 or len(dni) == 7):
            if dni.isdigit():
              self.__dni = dni
            else:
              print ("Error: El DNI debe ser una cadena de datos numéricos")  
        else:
            print("Error: El DNI debe ser una cadena de  7 u 8 caracteres.")

    def mostrar(self):
        return f"Nombre: {self.__nombre}, Edad:{str(self.__edad)}, DNI: {self.__dni}"

    def es_mayor_de_edad(self):
        return self.edad >= 18

persona1 = Persona()
print(f"Nombre: {persona1.nombre}")
print(f"Edad: {persona1.edad}")
print(f"DNI: {persona1.dni}")
print (persona1.mostrar())
persona1.nombre="Ines"
persona1.edad= 20
persona1.dni="1234567"
print (persona1.mostrar())
print("Es mayor de edad:"+ str(persona1.es_mayor_de_edad()))
