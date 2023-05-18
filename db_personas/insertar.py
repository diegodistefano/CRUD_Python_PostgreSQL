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
sqlInsert = 'INSERT INTO personas(nombre,apellido,edad) VALUES(%s,%s,%s)'

#Solicitud de datos al usuario
nombre = input('Ingrese el nombre: ')
apellido = input('Ingrese el apellido: ')
edad = input('Ingrese la edad: ')

# Recoleccion de datos
datos = (nombre, apellido, edad)

#Usar medoto execute 
cursor.execute(sqlInsert, datos)

# Guardar registro
conexion.commit()

# Registros insertados
registros = cursor.rowcount

# Mostrar mensaje
print(f'Registro insertado: {registros}')

# Cerrar las conexiones
cursor.close()
conexion.close()
