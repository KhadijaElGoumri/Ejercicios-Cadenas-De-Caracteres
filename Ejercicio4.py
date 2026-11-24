#Suponiendo que hemos introducido una cadena por teclado que representa una frase
#(palabras separadas por espacios), realiza un programa que cuente cuantas palabras
#tiene.
#khadija el goumri
#fecha(24-11-2026)
frase = input("Introduce una frase: ")

palabras = frase.split()

print("Número de palabras:", len(palabras))