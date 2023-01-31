from modulos.conexion import conect, cursor_db
from modulos.Fecha import Fecha

import json 

def obtener_banco(columna: str ="*") -> None:
    cursor = cursor_db()

def existe_registro(tabla: str, fecha: Fecha) -> bool:
    try:
        con = cursor_db()
        rs = con.execute(f'SELECT * FROM {tabla} where mes={fecha.mes} and anio={fecha.anio}')
        if len(rs) < 1:
            return False
        return True
    except:
        return False
    