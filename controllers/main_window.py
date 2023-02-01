from PySide6.QtWidgets import QWidget

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
from controllers.agregar_boletin import AgregarBoletinForm
from controllers.regenerar_base import RegenerarController
from controllers.config_widget import Config_Widget
from controllers.template_table import TemplateTable
from controllers.eliminar_window import EliminarController
from api.exportaciones import verificar_datos
class MainWidowsForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.btn_agregar_nuevo.clicked.connect(self.open_agregar_boletin_window)
        self.btn_rehacer_rango.clicked.connect(self.open_regenerar_bd)
        self.btn_configuracion.clicked.connect(self.open_configuracion)
        self.btn_verificar_bancos.clicked.connect(self.verificar_base)
        self.btn_delete.clicked.connect(self.eliminar_datos)
        self.setting()
    
    def mousePressEvent(self, event) -> None:
        self.ui.mouse_press_event(event)

    def open_agregar_boletin_window(self):
        window = AgregarBoletinForm()
        window.show()
    
    def open_regenerar_bd(self):
        windows = RegenerarController()
        windows.show()
    def open_configuracion(self):
        windows = Config_Widget()
        windows.show()
    def setting(self):
        pass
    def verificar_base(self):
        table = TemplateTable()
        data = verificar_datos()
        table.settings_table(("Año", "Mes", "Cantidad de registros"), (100,100,200), data)
        table.show()

    def eliminar_datos(self):
        windows = EliminarController()
        windows.show()
