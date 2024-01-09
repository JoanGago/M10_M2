valor1 = int(input("Introdueix un valor: "))
valor2 = int(input("Introdueix un altre valor: "))

if valor1 > valor2:
    print(f"{valor1} és més gran que {valor2}")
elif valor1 < valor2:
    print(f"{valor2} és més gran que {valor1}")
else:
    print("El dos valors són iguals")
