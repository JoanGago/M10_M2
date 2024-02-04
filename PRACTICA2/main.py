from create_table import creacio_table
from create import insert
from read import llegir
from update import act
from delete import borrar

def main():

    try:
        # Preguntem al usuari si la taula está creada.
        resposta_usr = input("La taula esta creada? (Si/No): ")

        if resposta_usr == "No":
            # Si no existeix la taula, es crea.
            creacio_table()
            
            
        while True:
            #Menu.
            print("1. Inserir un registre")
            print("2. Llegir un registre")
            print("3. Actualitzar un registre")
            print("4. Eliminar un registre")
            print("0. Surtir")

            opcio_escollida = input("Escull una de les seguents opcions: ")


            if opcio_escollida == "1":
                insert()
            elif opcio_escollida == "2":
                llegir()
            elif opcio_escollida == "3":
                act()
            elif opcio_escollida == "4":
                borrar()
            elif opcio_escollida == "0":
                break
            else:
                print("Error, aquesta opció no és valida.")

    except Exception as e:
        print(f"Hi ha hagut un error: {e}")


if __name__ == "__main__":
    main()