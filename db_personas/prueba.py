# importacion del modulo
import psycopg2

# Conexion a Base de Datos
conexion = psycopg2.connect(user = 'postgres',
                            password = 'admin',
                            host = '127.0.0.1',
                            port = '5432',
                            database = 'db_personas')

# Utilizar cursor
cursor = conexion.cursor()

#Crear sentencia SQL
sqlSelect = 'SELECT * FROM personas'

#Utilizar metodo execute
cursor.execute(sqlSelect)

#Mostrar resultado
registro = cursor.fetchall()
print(registro)

#Cerrar conexion
cursor.close()
conexion.close()

