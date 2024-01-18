# Igual que l’anterior però a la tupla afegir la frase sense els caràcters repetits
# i mostrar el contingut de la tupla. Exemple: Usuari indica la paula caracteristica.
# Es mostra per pantalla carteis.

frase = input("Introdueix una frase: ")

frase_sin_espacios = frase.replace(" ", "")

frase_sense_char_rep = ""

for char in frase_sin_espacios:
    if char not in frase_sense_char_rep:
        frase_sense_char_rep += char

tupla_resultado = (frase_sense_char_rep)


print("Tupla sense càracters repetits: ", tupla_resultado)
