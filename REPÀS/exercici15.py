numeros = []

while True:
    num = int(input("Introdueix un numero (Per finalitzar el programa posa 0): "))
    if num == 0:
        break
    numeros.append(num)
    numeros.sort(reverse=True)
tupla = tuple(numeros)
print("Tupla ordenada:", tupla)
