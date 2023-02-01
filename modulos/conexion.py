import psycopg2
import json
import traceback

with open("./modulos/datos_conexion.json") as file:
	archivo = json.load(file)
	BD = archivo

# BD = {
# 	"host": "192.168.0.15",
# 	"user": "mfinversiones",
# 	"password": "Mf_1nv3rs10n3s",
# 	"database": "bolban_mndev"
# }
def test_connection(host: str, database: str, port:str, user: str, password:str)-> bool:
	try:
		connection = None
		connection = psycopg2.connect(user= user,
									  password= password,
									  host= host,
									  port= port,
									  database=database)
		if connection.cursor():
			return True
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error to PostgreSQL", error)
		return False
def guardar_conexion(host: str, database: str, port:str, user: str, password:str)-> bool:
	try:
		with open("./modulos/datos_conexion.json", 'w') as file:
			json.dump({"host": host,
				"database": database,
				"port": port,
				"user": user,
				"password": password
			}, file)
			BD = {"host": host,
				"database": database,
				"port": port,
				"user": user,
				"password": password
			}
	except:
		traceback.print_exc()
		return False
	else:
		return True

def conect(database: str = None):
	try:
		connection = None
		connection = psycopg2.connect(user=BD['user'],
									  password=BD['password'],
									  host=BD['host'],
									  port=BD['port'],
									  database=BD['database'])
		return connection
	except (Exception, psycopg2.DatabaseError) as error:
		print("Error to PostgreSQL", error)
		return None
def cursor_db(database: str = None) :
	try:
		return conect(database).connect()
	except:
		return None
