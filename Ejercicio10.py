#Introducir una cadena de caracteres e indicar si es un palíndromo. Una palabra
#palíndroma es aquella que se lee igual adelante que atrás.
#khadija el goumri
#fecha(24-11-2026)
palabra = input("Introduce una palabra: ")

invertida = palabra[::-1]

if palabra == invertida:
    print("Es un palíndromo")
else:
    print("No es un palíndromo")






