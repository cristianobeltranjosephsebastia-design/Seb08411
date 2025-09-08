import psycopg2
conn = psycopg2.connect (
    host = "localhost",
    user = "postgres",
    password = "1234",
    database =  "Clase1",
    port = "5432"
)
cursor = conn.cursor()
Insert= " INSERT INTO usuario (Nombre , Direccion) VALUES (%s ,%s) "
Valores = [
(" Nicolas "," Nicolas@gmail.com "),
(" Luis ", " Luisfernandoa@gmail.com "),
(" Mateo "," mateoolarte@gmail.com "),
(" Luisa ","LuisaF@gmail.com "),
(" Santiago "," Santi5@gmail.com ")
]
cursor.executemany(Insert, Valores)
conn.commit()
cursor.close()
conn.close()

 
 