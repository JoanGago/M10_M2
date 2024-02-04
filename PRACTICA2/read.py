from connection import conexio_bd, tancar_conexio_bd

def llegir():
    try:
        cursor = conexio_bd()

        #Llegim un registre de la taula transformers.
        sql_insert = ''' SELECT transformer_id, transformer_name, transformer_alias, bando, residencia, estatus_actual
                        FROM public.transformers
        '''

        cursor.execute(sql_insert)

        resultat = cursor.fetchall()

        for i in resultat:
            print("transformer_id: ", i[0],)
            print("transformer_name: ", i[1],)
            print("transformer_alias: ", i[2],)
            print("bando: ", i[3],)
            print("residencia: ", i[4],)
            print("estatus_actual: ", i[5], "\n")

        tancar_conexio_bd(cursor.connection)
    except Exception as e:
        print(f"Hi ha hagut un error al llegir el registre: {e}")