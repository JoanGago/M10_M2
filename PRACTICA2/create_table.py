from connection import conexio_bd


def creacio_table():
    try:
        cursor = conexio_bd()
        #Creacio taula Transformers a la BD.
        sql = '''CREATE TABLE IF NOT EXISTS TRANSFORMERS(
                        transformer_id SERIAL PRIMARY KEY,
                        transformer_name VARCHAR(255) NOT NULL,
                        transformer_alias VARCHAR(255) NOT NULL,
                        bando VARCHAR(255) NOT NULL,
                        residencia VARCHAR(255) NOT NULL,
                        estatus_actual VARCHAR(255) NOT NULL
        )'''

        print(sql)

        # Utilizem el cursor per executar la consulta
        cursor.execute(sql)

        # Commit per fer efectius els canvis de la query.
        cursor.connection.commit()

        print("La taula s'ha creat amb exit.")

    except Exception as e:
        print(f"Hi ha hagut un error en la creació de la taula: {e}")