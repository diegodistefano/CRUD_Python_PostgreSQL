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

# Crear sentencia SQL
sqlSelectAll = 'SELECT * FROM personas'

#Usar medoto execute 
cursor.execute(sqlSelectAll)

# Cantidad de cambios
registro = cursor.fetchall()

# Guardar modificaciones
for fila in registro:
    print(fila)

# Cerrar las conexiones
cursor.close()
conexion.close()

