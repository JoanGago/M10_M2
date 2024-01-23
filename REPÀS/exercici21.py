# Demanar a l’usuari que posi 10 números separats per espais. Afegir aquests números a una llista.
# Calcular la suma de tots els números i la seva mitjana i afegir aquests 2 números a la llista.
# Mostrar per pantalla la llista.

# Exemple mostra per pantalla.
# Números de l’usuari:
# suma total:
# mitjana:

numeros = input("Introdueix 10 numeros separats per un espai: ")
list_numeros = list(map(float, numeros.split()))

suma_tot = sum(list_numeros)
mitjana = suma_tot / len(list_numeros)
mitjana = round(mitjana, 2)

list_numeros.append(suma_tot)
list_numeros.append(mitjana)

print("Números de l'usuari:", list_numeros)
print("Suma total:", suma_tot)
print("Mitjana:", mitjana)
