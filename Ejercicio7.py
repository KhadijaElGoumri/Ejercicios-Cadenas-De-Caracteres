#Pide una cadena y dos caracteres por teclado (valida que sea un carácter), sustituye la
#aparición del primer carácter en la cadena por el segundo carácter.
#khadija el goumri
#fecha(24-11-2026)
cadena = input("Introduce una cadena: ")
caracter1 = input("Carácter que quieres cambiar: ")
caracter2 = input("Carácter nuevo: ")

if len(caracter1) != 1 or len(caracter2) != 1:
    print("Error: introduce un solo carácter")
else:
    resultado = cadena.replace(caracter1, caracter2)
    print(resultado)