import pymysql
import sqlalchemy
import json

with open("./modulos/datos_conexion.json") as file:
	archivo = json.load(file)
	# BD = archivo["PROD"]
	BD = archivo["TEST"]

# BD = {
# 	"host": "192.168.0.15",
# 	"user": "mfinversiones",
# 	"password": "Mf_1nv3rs10n3s",
# 	"database": "bolban_mndev"
# }
def conect(database: str = None):
	try:
		host= BD['host']
		user= BD['user']
		password= BD['password']
		if database == None:
			database= BD['database']
		port= str(3306)
		return sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
	except:
		return None
def cursor_db(database: str = None):
	try:
		return conect(database).connect()
	except:
		return None
