numeros = input("Introdueix 10 numeros separats per un espai: ")

numeros_separats = [int(num) for num in numeros.split()]

if len(numeros_separats) == 10:
    numeros_separats.sort(reverse=True)
    tupla_ordenada = tuple(numeros_separats)
    print("Tupla ordenada de major a menor:", tupla_ordenada)
else:
    print("Has d'introduir 10 numeros.")
