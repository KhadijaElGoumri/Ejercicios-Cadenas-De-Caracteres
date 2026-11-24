#Realizar un programa que comprueba si una cadena leída por teclado comienza por una
#subcadena introducida por teclado.
#khadija el goumri
#fecha(24-11-2026)
cadena = input("Introduce una cadena: ")
subcadena = input("Introduce lo que quieres buscar al principio: ")

if cadena.startswith(subcadena):
    print("La cadena comienza por esa subcadena")
else:
    print("La cadena no comienza por esa subcadena")