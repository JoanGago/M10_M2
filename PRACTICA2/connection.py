import psycopg2

def conexio_bd():

    try:
        #Ens connectem a la base de dades.
        conn = psycopg2.connect(
            database="postgres",
            user="user_postgres",
            password='pass_postgres',
            host='localhost',
            port='5432'
        )

        #Per fer la connexió s'utilitza el mètode cursor()
        c = conn.cursor()
        return c
    
    except Exception as e:
        print(f"Hi ha hagut un error al conectar-se a la base de dades: {e}")

def tancar_conexio_bd(conn):
    #Tanquem la conexió a la base de dades.
    try:
        conn.close()
    except Exception as e:
        print(f"Hi ha hagut un error al tancar la conexió a la base de dades: {e}")