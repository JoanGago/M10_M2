paraula1 = str(input("Introdueix una paraula: "))
paraula2 = str(input("Introdueix un altre paraula: "))


print(paraula1.replace(paraula1[:2], paraula2[:2]))
print(paraula2.replace(paraula2[:2], paraula1[:2]))