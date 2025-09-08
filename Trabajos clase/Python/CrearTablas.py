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

cursor = conn.cursor()
Tablas = "CREATE TABLE usuario (id SERIAL PRIMARY KEY, Nombre VARCHAR, Direccion VARCHAR);", 
"CREATE TABLE registro (id_registro SERIAL PRIMARY KEY, Usuario VARCHAR, Password VARCHAR, Email VARCHAR, Tipo_Documento VARCHAR, Num_documento INT);",
"CREATE TABLE fecha de control (id_solicitud INT PRIMARY KEY, fecha_solicitud DATE, Tiempo_solicitud TIME, Nombre_usuario VARCHAR, Documento INT);",
"CREATE TABLE funcionalidad ()"

cursor.execute
conn.commit()
cursor.close()
conn.close()
 