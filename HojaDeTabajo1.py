#Ejercicio 1
print("Programa para crear una piramide")
print("")
numero= int(input("Introduzca un número para el tamaño de su piramide: "))
for i in range(numero):
    for j in range(i+1):
        print("*", end="")
    print("")


#Ejercicio 2
print("Programa para identificar si es un número primo")
print("")
numero_2= int(input("Introduzca un número entero: "))
i = 2
while numero_2 % i != 0:
    i += 1
if i == numero_2:
    print(str(numero_2) + " es primo")
else:
    print(str(numero_2) + " no es primo")