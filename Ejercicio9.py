#Realizar un programa que compruebe si una cadena contiene una subcadena. Las dos
#cadenas se introducen por teclado.
#khadija el goumri
#fecha(24-11-2026)
cadena = input("Introduce una cadena: ")
subcadena = input("Introduce la subcadena que quieres buscar: ")

if subcadena in cadena:
    print("La cadena contiene la subcadena")
else:
    print("La cadena no contiene la subcadena")