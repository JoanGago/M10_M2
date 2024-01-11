tupla = ("gener", "febrer", "març", "abril", "maig", "juny", "juliol", "agost", "setembre", "octubre", "novembre", "desembre")


while True:
    numero = int(input("Introdueix un numero entre el 0 i 12: "))
    if int(numero == 0):
        print("Programa finalitzat.")
        break
    elif int(numero > 12):
        print("Només hi han 12 mesos!!!!!!")
    else:
        print(tupla[numero -1])
    



