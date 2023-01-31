import modulos.Funciones as fn
from modulos.funciones_emaggi import obtener_lista_bol_financieras_balances
from modulos.Fecha import Fecha
from modulos.Bancos import get_balance, get_ratios, get_adicional
from modulos.api_bolban import verificar_integridad, listar_tablas
from modulos.Funciones import respaldar_datos
from configuraciones.configuraciones import TIPO_SALIDA, RUTAS
from modulos.Informes import Informe
import modulos.Bancos as Bancos
from openpyxl.utils import get_column_letter
import os
import pandas as pd
from modulos.conexion import cursor_db

def test1():

    master = "./assets/docs/master_bancos.xlsx"
    template = "./assets/docs/test_01.xlsx"
    url = os.path.realpath(template)
    print(os.path.realpath(template))
    titulos = [
        "Balance General",
        "Estado de Resultados",
        "Ratios",
        "Información Adicional"
        ]

    informe = Informe(master)
    # informe.generar_informe_banco("Banco Nacional de Fomento",Fecha("01/01/2022") )
    if not os.path.isfile(url):
        informe.crear_nuevo_informe("test_01_v2")
    informe.set_titles(titulos, 1)
    fecha = Fecha("01/08/2022")
    datos = Bancos.informe_balance(fecha)

    for banco, valor in datos.items():
        informe.set_data(banco, valor, url, fecha)
        

def test2():
    estados = fn.datos_por_fecha_sql(fecha, "estados_resultados", 'Sistema')
    estados = estados[['cuenta', 'cuenta_mf', 'tipo', 'valor']]
    estados = estados.pivot(index='cuenta_mf', columns='tipo', values='valor')
    estados.reset_index(inplace=True)
    print(estados['cuenta_mf'])
    print(estados.columns)

def test3():
    balances = fn.datos_por_fecha_sql(fecha, "balances")
    sistema = balances[balances['banco']=='SISTEMA']
    bnf = balances[balances['banco']=='Banco Nacional de Fomento']
    balances = sistema.copy()
    balances = balances [['banco', 'cuenta_mf', 'tipo', 'valor']]
    balances = balances.pivot(index='cuenta_mf', columns='tipo', values='valor')
    balances.reset_index(inplace=True)
    balances = balances.rename(columns={'cuenta_mf':'cuenta','total': 'balances', 'moneda nacional':'balances-MN', 'moneda extrajera':'balances-ME'})
    # continuar desde aqui
    sistema = sistema[['banco', 'cuenta_mf', 'tipo', 'valor']]
    sistema = sistema.pivot(index='cuenta_mf', columns='tipo', values='valor')
    sistema.reset_index(inplace=True)
    sistema = sistema.rename(columns={'cuenta_mf':'cuenta','moneda nacional':'sistema-mn', 'moneda extranjera': 'sistema-me', 'total':'sistema-total'})
    bnf = bnf[['banco', 'cuenta_mf', 'tipo', 'valor']]
    bnf = bnf.pivot(index='cuenta_mf', columns='tipo', values='valor')
    bnf.reset_index(inplace=True)
    bnf = bnf.rename(columns={'cuenta_mf':'cuenta','moneda nacional':'bnf-mn', 'moneda extranjera': 'bnf-me', 'total':'bnf-total'})
    balance_exc_bnf= pd.merge(sistema, bnf, how='inner', on='cuenta')

    balance_exc_bnf['balances-exc-bnf-me']= balance_exc_bnf['sistema-me'] - balance_exc_bnf['bnf-me']
    balance_exc_bnf['balances-exc-bnf-mn']= balance_exc_bnf['sistema-mn'] - balance_exc_bnf['bnf-mn']
    balance_exc_bnf['balances-exc-bnf']= balance_exc_bnf['sistema-total'] - balance_exc_bnf['bnf-total']
    balance_exc_bnf= balance_exc_bnf[['cuenta','balances-exc-bnf-me', 'balances-exc-bnf-mn', 'balances-exc-bnf']]

    print(balance_exc_bnf.head(10))
    
def test4():
    fecha = Fecha("01/01/2015")
    fin = Fecha("01/11/2022")
    lista = fn.listar_fechas_por_mes(fecha, fin)
    
    rango = obtener_lista_bol_financieras_balances(fecha, fin, "bancos")
    carpeta= "datos/"
    for index, archivo in enumerate(rango):
        try:
            nuevo_archivo = carpeta + archivo
            print(lista[index])
            dic = {"fecha":lista[index], 'sheet_name': '5'}
            datos = get_adicional(nuevo_archivo, dic)
            respaldar_datos(datos, "adicionales", TIPO_SALIDA[1])
            print("ok")
        except ValueError:
            traceback.print_exc()
if __name__=="__main__":
    import traceback

    fecha = Fecha("01/01/2022")
    fin = Fecha("01/11/2022")
    lista = fn.listar_fechas_por_mes(fecha, fin)
    
    rango = obtener_lista_bol_financieras_balances(fecha, fin, "bancos")
    adicional = fn.datos_por_fecha_sql(fecha, "adicionales", 'Sistema')
    adicional = adicional[['cuenta', 'val_num']]
    adicional = adicional.rename(columns={'val_num':'adicional'})
    print(adicional.head())