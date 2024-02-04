from connection import conexio_bd, tancar_conexio_bd

def borrar():
    try:
        cursor = conexio_bd()

        #Eliminem un registre de la taula transformers.
        sql_delete = ''' DELETE FROM public.transformers WHERE transformer_id=1
        '''
        print("S'ha eliminat el registre correctament.")
        cursor.execute(sql_delete)
        cursor.connection.commit()
        tancar_conexio_bd(cursor.connection)

    except Exception as e:
        print(f"Hi ha hagut un error al borrar un registre: {e}")