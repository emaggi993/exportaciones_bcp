import os
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from views.general_custom_ui import GeneralCustomUi

from views.regenerar_bd import regenerar_widget
from modulos.MessageBox import si_no_mensaje, mensaje_simple
from modulos.Fecha import Fecha

class RegenerarController(QWidget, regenerar_widget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		self.BtnGenerar.clicked.connect(self.generar)
		self.BTNSeleccionarCarpeta.clicked.connect(self.seleccionar_carpeta)

	def generar(self):
		pass

	def __Generar(self, file: str, fecha: Fecha)-> None:
		pass
	
	def seleccionar_carpeta(self):
		editText = self.ETUbicacionArchivos
		editText.setText(None)
		fname= QFileDialog.getExistingDirectory(
				self,
				"Open a folder",
				None,
				QFileDialog.ShowDirsOnly
				)
		editText.setText(fname)
		
	def limpiar_pantalla( self):
		self.PBEstado.setValue(0)
		self.label_info.setText(None)