import pandas as pd
from modulos.Fecha import Fecha
from modulos.Funciones import mes_letras_a_numeros
from api.exportaciones import lista_partidas, insertar_datos_exportaciones
import traceback

class Exportaciones():
    def __init__(self, path: str, sep: str = "\t") -> None:
        data = pd.read_csv(path, sep=sep)
        data.dropna(how='all', axis= 1, inplace=True)
        data.dropna(how='all', axis= 0, inplace=True)

        # data = data.iloc[:,:4]
        self.data = data
        fecha = data.columns[2].lower()
        fecha= fecha.replace("kilos netos", "").replace(" ","")
        mes, anio = fecha.split("-")
        self.fecha = Fecha(f"01/{mes_letras_a_numeros(mes)}/{anio}")
        data = data.iloc[:,:4]
        data.columns= ['nombre', 'pais', 'kilo_neto', 'fob']
        data = data[~data['nombre'].isna()]
        data['cod_partida']= data.apply(lambda x: self.cod_partida(x['nombre']), axis= 1)
        data['den_partida']= data.apply(lambda x: self.den_partida(x['nombre']), axis= 1)
        data['cod_moneda']= "USD"
        data['fuente']= "BCP"
        data['mes']= int(self.fecha.mes)
        data['anho']= int(self.fecha.anio)
        self.data = data[['cod_partida', 'den_partida', 'pais', 'mes', 'anho', 'kilo_neto', 'fob', 'cod_moneda', 'fuente']]
    
    def get_fecha(self ) -> Fecha:
        return self.fecha
    def head(self, limit: int = 0)-> pd.DataFrame:
        if not isinstance(limit, int) or limit < 0:
            raise Exception("El limite debe ser un numero entero positivo ")
        else:
            if limit == 0:
                return self.data.head()
            else:
                return self.data.head(limit)
    def tail(self, limit: int = 0)-> pd.DataFrame:
        if not isinstance(limit, int) or limit < 0:
            raise Exception("El limite debe ser un numero entero positivo ")
        else:
            if limit == 0:
                return self.data.tail()
            else:
                return self.data.tail(limit)
    def sample(self, limit: int = 0)-> pd.DataFrame:
        if not isinstance(limit, int) or limit < 0:
            raise Exception("El limite debe ser un numero entero positivo ")
        else:
            if limit == 0:
                return self.data.sample()
            else:
                return self.data.sample(limit)
    def data(self)-> pd.DataFrame:
        return self.data
    
    def save(self) -> bool:
        try:
            lista = lista_partidas()
            permitidos = self.data[self.data['cod_partida'].isin( lista)]
            no_permitidos = self.data[~(self.data['cod_partida'].isin( lista))]
            print(len(lista))
            print("permitidos", permitidos.shape)
            print("no permitidos", no_permitidos.shape)
            datos = list(permitidos.itertuples(index=False, name=None))
            # print(type(tuplas))
            # print(tuplas)
            if insertar_datos_exportaciones(datos):
                return {'resultado': True, 'cargados':permitidos.shape[0], 'excluidos': no_permitidos.shape[0], 'total':self.data.shape[0]}
            

        except Exception as e:
            traceback.print_exc()
            return {'resultado':False, 'mensaje': str(e)}
        
    def cod_partida(self, texto: str, reg: str = " - "):
        if not pd.isna(texto):
            return texto.split(reg)[0].strip()
    def den_partida(self, texto: str, reg: str = " - "):
        if len(texto.split(reg)) > 1 :
            return texto.split(reg)[1].strip()
        else:
            return None
