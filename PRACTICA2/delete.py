from connection import connection, conn

sql_delete = ''' DELETE FROM public.transformers WHERE transformer_id=1
'''

connection.execute(sql_delete)
conn.commit()