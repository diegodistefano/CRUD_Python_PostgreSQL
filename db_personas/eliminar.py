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
sqlDelete = 'DELETE FROM personas WHERE idpersona=%s'

# Consulta de datos al usuario
idpersona = input('Ingrese el ID del usuario a eliminar: ')

#Usar medoto execute 
cursor.execute(sqlDelete, idpersona)

# Guardar modificaciones
conexion.commit()

# Cantidad de cambios
eliminacion = cursor.rowcount

# Mostrar mensaje
print(f'Registros eliminados: {eliminacion}')

# Cerrar las conexiones
cursor.close()
conexion.close()
