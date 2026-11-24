#Pide una cadena y un carácter por teclado (valida que sea un carácter) y muestra cuantas
#veces aparece el carácter en la cadena
#khadija el goumri
#fecha(24-11-2026)
cadena = input("Introduce una cadena: ")
caracter = input("Introduce un carácter: ")

if len(caracter) != 1:
    print("Error: debes introducir un solo carácter")
else:
    cantidad = cadena.count(caracter)
    print("El carácter aparece", cantidad, "veces")