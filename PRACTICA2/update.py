from connection import connection, conn

sql_update = ''' UPDATE public.transformers SET estatus_actual='Muerto' WHERE transformer_id=1
'''

connection.execute(sql_update)
conn.commit()
result = connection.rowcount
print("id modificada: ", result, "Actualització efectuada sense errors")
