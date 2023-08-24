# 3 Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y la cantidad de veces que aparece (frecuencia).
def cadena_a_diccionario(cadena):
    palabras=cadena.split()
 
    diccionario={}
    for palabra in palabras:
        diccionario[palabra]= cadena.count(palabra)

    return diccionario

diccionario={}
diccionario= cadena_a_diccionario(" escribir un programa escribir un asi")
print (f"El diccionario creado es {diccionario}" )

#4 Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.
def key_mas_repetida_en_diccionario (diccionario):
    repeticiones= max(diccionario.values())
    for palabra in diccionario:
        if diccionario[palabra]==repeticiones:
            return (palabra, diccionario[palabra]) 

diccionario= cadena_a_diccionario("hola un escribir un programa escribir un asi")
mytupla= key_mas_repetida_en_diccionario (diccionario)
print (mytupla)
