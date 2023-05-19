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
sqlSelectOne = 'SELECT * FROM personas WHERE idpersona=%s'

# Consulta de datos al usuario
idpersona = input('Ingrese el ID del usuario a mostrar: ')

#Usar medoto execute 
cursor.execute(sqlSelectOne, idpersona)

# Cantidad de cambios
registro = cursor.fetchone()

# Guardar modificaciones
print(registro)

# Cerrar las conexiones
cursor.close()
conexion.close()

