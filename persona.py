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

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("Error: El nombre debe ser una cadena de caracteres.")

    def get_nombre(self):
        return self.__nombre

    def set_edad(self, edad):
        if isinstance(edad, int) and edad >= 0:
            self.__edad = edad
        else:
            print("Error: La edad debe ser un número entero no negativo.")

    def get_edad(self):
        return self.__edad

    def set_dni(self, dni):
        if isinstance(dni, str) and( len(dni) == 8 or len(dni) == 7):
            if dni.isdigit():
              self.__dni = dni
            else:
              print ("Error: El DNI debe ser una cadena de datos numéricos")  
        else:
            print("Error: El DNI debe ser una cadena de  7 u 8 caracteres.")

    def get_dni(self):
        return self.__dni

    def mostrar(self):
        print("Nombre:" + self.__nombre)
        print("Edad:"+str(self.__edad))
        print("DNI: "+self.__dni)

    def es_mayor_de_edad(self):
        return self.__edad >= 18

persona1 = Persona()
persona1.set_nombre("Ines")
persona1.set_edad(20)
persona1.set_dni("1234567")
persona1.mostrar()
print("Es mayor de edad:"+ str(persona1.es_mayor_de_edad()))
