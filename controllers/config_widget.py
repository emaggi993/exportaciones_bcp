import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog
from views.general_custom_ui import GeneralCustomUi

from views.config_widget import config_widget

from modulos.MessageBox import si_no_mensaje, mensaje_simple
from modulos.conexion import BD, test_connection, guardar_conexion

class Config_Widget(QWidget, config_widget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()
		self.set_data()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		self.btn_test.clicked.connect(self.__test)
		self.BtnGenerar.clicked.connect(self._guardar)

	def set_data(self):
		self.le_base.setText(BD['database'])
		self.le_host.setText(BD['host'])
		self.le_user.setText(BD['user'])
		self.le_puerto.setText(BD['port'])
		self.BtnGenerar.setText("Guardar")
	
		
	def __test(self):
		# self.BtnGenerar.setEnabled(False)
		puerto = "5432"
		if self.le_puerto.text() != None and self.le_puerto.text() != '':
			puerto = self.le_puerto.text() 
		password = BD['password']
		if self.le_password.text() != None and self.le_password.text() != '' :
			password = self.le_password.text()
		if test_connection(
			self.le_host.text(),
			self.le_base.text(),
			puerto,
			self.le_user.text(),
			password
		):
			mensaje_simple("TEST", "Conexión éxitosa")
		else:
			mensaje_simple("TEST", "No se ha podido conectar")
			# self.BtnGenerar.setEnabled(False)
		
		# get_balance( filename, {"fecha":fecha, "progress_bar":self.PBEstado, "duplicado":duplicado})
	def _guardar(self):
		puerto = "5432"
		if self.le_puerto.text() != None:
			puerto = self.le_puerto.text() 
		password = BD['password']
		if self.le_password.text() != None:
			password = self.le_password.text()
		if guardar_conexion(
			self.le_host.text(),
			self.le_base.text(),
			puerto,
			self.le_user.text(),
			password
		):
			mensaje_simple("Enhorabuena", "Guardado correctamente")
		else:
			mensaje_simple("Error", "No se ha podido guardar los datos")