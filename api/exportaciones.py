from modulos.conexion import conect
import psycopg2
from modulos.Funciones import mes_numero_a_letra
from modulos.Fecha import Fecha

def lista_partidas()-> list:
    try:
        connection = conect()
        cursor = connection.cursor()
        sql = "SELECT codigo_partida FROM partidas_exportacion where activa=TRUE"
        cursor.execute(sql)
        lista_partidas = []
        for cod_part in cursor.fetchall():
            lista_partidas.append(cod_part[0])
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error to PostgreSQL", error)
    else:
        return lista_partidas
    finally:
        if connection is not None:
            connection.close()

def insertar_datos_exportaciones(datos: list) -> bool:
    try:
        connection = conect()
        cursor = connection.cursor()
        print("conexion establecida")
        sql = "SELECT insertar_datos_exportaciones(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        for dato in datos:
            cursor.execute(sql, dato)
            print(dato)
        connection.commit()
        print("COMMIT, carga completa..!!")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error to PostgreSQL", error)
        connection.rollback()
        print("ROLLBACK")
        print(dato)
        raise error
    else:
        return True
    finally:
        if connection is not None:
            connection.close()

def verificar_datos():
    
    try:
        connection = conect()
        cursor = connection.cursor()
        sql="select anho, mes, count(codigo_moneda) from datos_exportaciones group by anho, mes order by anho DESC, mes DESC"
        cursor.execute(sql)
        registros = []
        for campo in cursor.fetchall():
            # print(campo)
            registros.append([campo[0], mes_numero_a_letra(campo[1], "largo"), campo[2] ])
        # print(registros)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error to PostgreSQL", error)
    else:
        return registros
    finally:
        if connection is not None:
            connection.close()

def eliminar_datos(fecha: Fecha) -> bool:
    try:
        connection = conect()
        cursor = connection.cursor()
        print("conexion establecida")
        sql = f"DELETE FROM datos_exportaciones WHERE mes={int(fecha.mes)} and anho= {int(fecha.anio)}"
        cursor.execute(sql)
        connection.commit()
        print("COMMIT, carga completa..!!")
        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print("Error to PostgreSQL", error)
        connection.rollback()
        print("ROLLBACK")
        raise error
    else:
        return True
    finally:
        if connection is not None:
            connection.close()