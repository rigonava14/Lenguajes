print("BIENVWENIDO AL MUNDO DE GUMBALL ")
conjunto = ["a", "b","*"]
conjuntoB = conjunto
conjuntoC = []
potencia = int(input("Inserte una potencia = "))
datosConjuntoFinal = pow(len(conjunto),potencia)

while len(conjunto) < datosConjuntoFinal:
    contadorjsjsjjs=0
    while contadorjsjsjjs < len(conjunto):
        for i in conjuntoB:
            conjuntoC.append(conjunto[contadorjsjsjjs] + i)
        contadorjsjsjjs += 1
    conjunto = []
    conjunto = conjuntoC
    conjuntoC = []
print("Potencia de Conjunto:", conjunto) 

