#Demanar a l’usuari un número de l’1 al 10 i mostrar per pantalla la seva taula 
#de multiplicar fins el 10. Exemple: l’usuari marca 3, es mostra per pantalla: 3,6,9,12,15,18,21,24,27 i 30
numero = int(input("Introdueix un numero entre el 1 i 10: "))

if int(numero) < 1 or int(numero) > 10:
    print("El numeor no esta dintre del rang.")
else:
    count = 1
    while count <= 10:
        taula_multiplicar = []
        taula_multiplicar.append(numero * count)
        count += 1
        print(taula_multiplicar)
        




