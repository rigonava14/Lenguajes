print("Hola Mundo")
arreglo = [1,2,45,65,89,74]
w=0
for t in arreglo:
    w+=t
print(w)

#Ejercicio 2
array=[ [1, 2,3],[4,4,4],[3,3,3] ]
Mul = int(input("Inserte un numero = "))
s=0
for x in array:
    for j in  x:
        y = Mul*j
        s += y
        
print(s)
