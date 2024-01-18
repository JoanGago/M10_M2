#Demanar a l’usuari una frase. El programa eliminarà els espais i s'afegirà a una tupla. Mostrar per pantalla el contingut de la tupla.

frase = input("Introdueix una frase: ")

frase_sin_espacios = frase.replace(" ", "")

tupla = (frase_sin_espacios)

print("Tupla de caracters:", tupla)