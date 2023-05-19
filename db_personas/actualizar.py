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
sqlUpdate = 'UPDATE personas SET nombre=%s,apellido=%s,edad=%s WHERE idpersona=%s'

#Consulta de datos al usuario
idpersona = input('Ingrese el ID del usuario: ')
nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
edad = input('Ingrese la edad: ')

# Recoleccion de datos
datos = (nombre, apellido, edad, idpersona)

#Usar medoto execute 
cursor.execute(sqlUpdate, datos)

# Guardar modificaciones
conexion.commit()

# Cantidad de cambios
actualizacion = cursor.rowcount

# Mostrar mensaje
print(f'Registros actualizados: {actualizacion}')

# Cerrar las conexiones
cursor.close()
conexion.close()
