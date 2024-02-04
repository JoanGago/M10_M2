from connection import conexio_bd, tancar_conexio_bd

def act():
    try:
        cursor = conexio_bd()
        #Actualitzem un registre de la taula transformers.
        sql_update = ''' UPDATE public.transformers SET estatus_actual='Muerto' WHERE transformer_id=1
        '''

        cursor.execute(sql_update)
        cursor.connection.commit()
        result = cursor.rowcount
        print("id modificada: .", result, "Actualització efectuada sense errors")

        tancar_conexio_bd(cursor.connection)
    
    except Exception as e:
        print(f"Hi ha hagut un error al actualitzar un registre: {e}")
