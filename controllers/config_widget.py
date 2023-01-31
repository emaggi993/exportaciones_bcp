import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog
from views.general_custom_ui import GeneralCustomUi

from views.config_widget import config_widget

from modulos.MessageBox import si_no_mensaje, mensaje_simple

class Config_Widget(QWidget, config_widget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		pass

	
		
	def __test(self):
		
		
		
		# get_balance( filename, {"fecha":fecha, "progress_bar":self.PBEstado, "duplicado":duplicado})
		self.limpiar_ventana()