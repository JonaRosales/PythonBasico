#Ejercicio 1
print("Programa de contraseña")
print("")
contraseña = "contraseña"
password = input("Introduce la contraseña: ")
if contraseña == password.lower():
    print("La contaseña coincide")
else:
    print("La contraseña no coincide")

#Ejercicio 2
nombre = input("¿Cúal es tu nombre? ")
sexo = input("¿Cuál es tu sexo? Ingresa H si eres hombre o Ingresa M si eres mujer. ")
if sexo == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print("Tu grupo es " + grupo)