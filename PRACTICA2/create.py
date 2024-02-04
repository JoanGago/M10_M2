from connection import conexio_bd, tancar_conexio_bd

def insert():
    try:
        cursor = conexio_bd()
        #Inserim un registre a la taula transformers.
        
        sql_insert = ''' INSERT INTO public.transformers(transformer_id, transformer_name, transformer_alias, bando, residencia, estatus_actual)
                                    VALUES ('1', 'Orion Pax', 'Optimus Primer', 'Autobots', 'Tierra', 'Vivo')                         
        '''
        print(sql_insert)
        print("S'ha inserit un registre correctament.")
        cursor.execute(sql_insert)
        cursor.connection.commit()
        tancar_conexio_bd(cursor.connection)
    
    except Exception as e:
        print(f"Hi ha hagut un error al inserir el registre: {e}")