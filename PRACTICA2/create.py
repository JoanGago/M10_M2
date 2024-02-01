from connection import connection, conn
sql_insert = ''' INSERT INTO public.transformers(transformer_id, transformer_name, transformer_alias, bando, residencia, estatus_actual)
                            VALUES ('1', 'Orion Pax', 'Optimus Primer', 'Autobots', 'Tierra', 'Vivo')                         
'''

connection.execute(sql_insert)
conn.commit()