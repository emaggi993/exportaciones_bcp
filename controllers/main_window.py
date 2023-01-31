from PySide6.QtWidgets import QWidget
from PySide6.QtGui import QPixmap

from views.main_window import MainWindow
from views.general_custom_ui import GeneralCustomUi
from controllers.agregar_boletin import AgregarBoletinForm
from controllers.regenerar_base import RegenerarController
from controllers.config_widget import Config_Widget
class MainWidowsForm(QWidget, MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui = GeneralCustomUi(self)

        self.btn_agregar_nuevo.clicked.connect(self.open_agregar_boletin_window)
        self.btn_rehacer_rango.clicked.connect(self.open_regenerar_bd)
        self.btn_configuracion.clicked.connect(self.open_configuracion)
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
