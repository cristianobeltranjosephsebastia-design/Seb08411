import psycopg2
conn = psycopg2.connect (
    host = "localhost",
    user = "postgres",
    password = "1234",
    database =  "Clase1",
    port = "5432"
)
cursor = conn.cursor()
Name = input(" Ingrese su nombre ") 
Email = input(" Ingrese su correo electronico ")
cursor.execute(" INSERT INTO usuario (Nombre , Direccion) VALUES (%s,%s)", (Name, Email))
conn.commit()
cursor.close()
conn.close()
 
 