import random

num_random = random.randint(1,100)

intents = 0

while True:
    intents += 1
    num_introduit = int(input("Introdueix un numero del 1 al 100: "))
    
    if num_introduit == num_random:
        print(f"Has adivinat el numero secret. Intents: {intents}")
        break
    elif num_introduit > num_random:
        print(f"El numero és més petit que {num_introduit}.")
    else:
        print(f"El numero és més gran que {num_introduit}.")

