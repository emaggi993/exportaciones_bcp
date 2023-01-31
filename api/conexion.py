import pymysql
import sqlalchemy
def conect():
	host="192.168.0.15"
	user="mfinversiones"
	password="Mf_1nv3rs10n3s"
	database="bolban"
	port= str(3306)
	return sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}')
def cursor_db():
	return conect().cursor()
if __name__=="__main__":
	print(conect())