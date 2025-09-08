import psycopg2
conn = psycopg2.connect (
    host = "localhost",
    user = "postgres",
    password = "1234",
    database =  "Clase1",
    port = "5432"
)
cursor = conn.cursor()
cursor.execute("select * from usuario;")
for usuario in cursor.fetchall():
    print(f"id: {usuario[0]}, Nombre: {usuario[1]}, Direccion: {usuario[2]}")
conn.commit()
cursor.close()
conn.close()
 