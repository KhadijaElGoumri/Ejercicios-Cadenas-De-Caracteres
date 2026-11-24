#Si tenemos una cadena con un nombre y apellidos, realizar un programa que muestre las
#iniciales en mayúsculas.
#khadija el goumri
#fecha(24-11-2026)
nombre = input("Introduce tu nombre y apellidos: ")

palabras = nombre.split()

for palabra in palabras:
    print(palabra[0].upper(), end="")