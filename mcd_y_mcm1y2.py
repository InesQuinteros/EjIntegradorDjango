# 1 mcd  (usando el algoritmo de Euclides)
def mcd (numero1, numero2):
    print ("Entre a mcd")
    if numero1 > numero2 :
        nmayor=numero1
        nmenor=numero2
    else:
        nmayor=numero2
        nmenor=numero1
    
    resto= nmayor % nmenor
    while resto != 0:
        nmayor=nmenor
        nmenor=resto
        resto= nmayor % nmenor
    return nmenor

numero1=30
numero2=12
resultado=mcd(numero1, numero2)
print (f"El MCD de {numero1} y {numero2} es {resultado}")
print (resultado)
print ("ahora voy a cam")

#2 MDM usando mcd
def mcm (numero1, numero2):
    print (numero1)
    resultado_mcd = mcd (numero1, numero2)
    
    if (resultado_mcd==0):
        return "error"
    return (numero1 * numero2 )/ resultado_mcd

numero1=30
numero2=12
resultado = mcm (numero1, numero2)
print (f"El MCM de {numero1} y {numero2} es {resultado}")
