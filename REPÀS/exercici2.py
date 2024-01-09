preu = float(input("Introdueix un preu: "))
iva = float(input("Introdueix l'IVA que vols aplicar(4%, 10%, 21%): "))
preu_final = preu + (preu*(iva/100))

print("\nPreu amb IVA aplicat:")
print(f"\npreu:{preu}€")
print(f"\nIVA:{iva}%")
print(f"\nPreu final:{preu_final}€")