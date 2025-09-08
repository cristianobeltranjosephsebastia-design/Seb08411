import psycopg2
conn = psycopg2.connect (
    host = "localhost",
    user = "postgres",
    password = "1234",
    database =  "Clase1",
    port = "5432"
)
print(conn)
print(" Conexion exitosa ")

