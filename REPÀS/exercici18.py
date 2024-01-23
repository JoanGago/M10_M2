# Demanar a l’usuari posar 2 paraules. Afegir aquestes a una tupla i 
# mostrar per pantalla quantes vegades apareix cada lletra.


paraula1 = input("Introdueix la primera paraula: ")
paraula2 = input("Introdueix la segona paraula: ")

tupla_paraules = (paraula1, paraula2)

comptador = {}
for paraula in tupla_paraules:
    for lletra in paraula:
        comptador[lletra] = comptador.get(lletra, 0) + 1
        
print("Nombre de vegades que apareix cada lletra:")

for lletra, comptador in comptador.items():
    print(f"{lletra}: {comptador}")