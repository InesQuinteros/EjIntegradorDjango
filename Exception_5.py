5# Sabiendo que ValueError es la excepción que se lanza cuando no podemos convertir una cadena de texto en su valor numérico, escriba una función get_int() que lea un valor entero del usuario y lo devuelva, iterando mientras el valor no sea correcto.
def get_int_iterativo():
    es_entero=False
    while es_entero==False:
        try:
            entero= int(input("Ingrese un número entero:"))
            es_entero=True
        except ValueError:
            print (("Ingreso inválido. Debe ser un número entero"))
    return entero

numero_entero=get_int_iterativo()
print (f"El número entero ingresado es {numero_entero}")

def get_int_recursivo():
    try:
        entero= int(input("Ingrese un número entero:"))
        return entero
    except ValueError:
        print (("Ingreso inválido. Debe ser un número entero"))
        return get_int_recursivo()

numero_entero=get_int_recursivo()
print (f"El número entero ingresado en funcion recursiva  es {numero_entero}")
