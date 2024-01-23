# Crear un diccionari on la clau (key) sigui un nom i el valor (value) l’edat.
# S’haura de demanar a l’usuari que posi contactes (noms i edats). 
# Si algun nom es repeteix no s’fageirà al diccionari (indicant-ho a l’usuari). 
# Es deixarà d’inserir contactes quan l’usuari indiqui que no vol afegir-ne més.

diccionari_contactes = {}

while True:
    nom = input("Introdueix un nom ('stop' per finalitzar): ")

    if nom == 'stop':
        break

    if nom in diccionari_contactes:
        print(f"{nom}. Aquest nom ja està a la llista de contactes. No s'afegirà.")

    else:
        edat = int(input(f"Edat de {nom}: "))
        diccionari_contactes[nom] = edat

print("Contactes:", diccionari_contactes)