import pandas as pd
from modulos.Fecha import Fecha


def mes_letras_a_numeros(texto: str ):
	meses = {
		"enero": "01",
		"febrero": "02",
		"marzo":"03",
		"abril": "04",
		"mayo":"05",
		"junio": "06",
		"julio": "07",
		"agosto": "08",
		"septiembre": "09",
		"octubre": "10",
		"noviembre":"11",
		"diciembre": "12"
	}
	if texto.lower() in meses.keys():
		return meses[texto.lower()]
	else:
		return None

def mes_numero_a_letra(mes: int, formato: str)-> str:
	'''
	parametros
		mes:
			1,2,3,..,12
		formato:
			corto, largo
				corto: 'ene', 'feb',..,'dic'
				largo: 'enero', 'febrero',...,'diciembre'
	'''
	# print(mes)
	if int(mes) > 0 and int(mes) < 13:
		largo = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre", "octubre","noviembre", "diciembre"]
		corto= ['ene', 'feb', 'mar', 'abr', 'may', 'jun', 'jul', 'ago', 'sep', 'oct', 'nov', 'dic']
		if formato == 'largo':
			return largo[mes - 1].title()
		elif formato == 'corto':
			return corto[mes - 1].upper()
	else:
		return None

def listar_fechas_por_mes(fecha_inicio: Fecha, fecha_fin: Fecha) -> list:
	from datetime import datetime
	from dateutil.relativedelta import relativedelta
	inicio = datetime(int(fecha_inicio.anio), int(fecha_inicio.mes), int(fecha_inicio.dia))
	fin = datetime(int(fecha_fin.anio), int(fecha_fin.mes), int(fecha_fin.dia))
	relativo = inicio
	datos = []
	datos.append(str(relativo.strftime("%d/%m/%Y")))
	while relativo < fin:
		relativo = relativo + relativedelta(months=1)
		datos.append(Fecha(str(relativo.strftime("%d/%m/%Y"))))
	return datos