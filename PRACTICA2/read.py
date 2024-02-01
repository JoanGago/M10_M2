from connection import connection, conn
sql_insert = ''' SELECT transformer_id, transformer_name, transformer_alias, bando, residencia, estatus_actual
                FROM public.transformers
'''

connection.execute(sql_insert)

result = connection.fetchall()

for i in result:
    print("transformer_id: ", i[0],)
    print("transformer_name: ", i[1],)
    print("transformer_alias: ", i[2],)
    print("bando: ", i[3],)
    print("residencia: ", i[4],)
    print("estatus_actual: ", i[5], "\n")
