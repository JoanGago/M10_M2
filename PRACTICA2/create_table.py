from connection import conn
from connection import connection
#Creacio taula user

sql = '''CREATE TABLE TRANSFORMERS{
                transformer_id SERIAL PRIMARY KEY,
                transformer_name VARCHAR(255) NOT NULL,
                transformer_alias VARCHAR(255) NOT NULL,
                bando VARCHAR(255) NOT NULL,
                residencia VARCHAR(255) NOT NULL,
                estatus_actual VARCHAR(255) NOT NULL
}'''

print(sql)

connection.execute(sql)
print(connection)

conn.commit()