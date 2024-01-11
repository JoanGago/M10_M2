numero = int(input("Introdueix un numero entre el 10 i 100: "))
count = 1

if int(numero < 10) | int(numero > 100):
    print("El numero esta fora del rang permes")
else:
    numeros = []
    while count <= numero:
        numeros.append(count)
        count += 1
        tupla = tuple(numeros)
        print(numeros)

