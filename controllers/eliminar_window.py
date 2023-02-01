import os
from PySide6.QtCore import Qt, QDate
from PySide6.QtWidgets import QWidget, QFileDialog, QMessageBox
from views.general_custom_ui import GeneralCustomUi

from views.eliminar_widget import eliminar_widget
from modulos.MessageBox import si_no_mensaje, mensaje_simple
from modulos.Fecha import Fecha
from api.exportaciones import eliminar_datos
from modulos.Funciones import listar_fechas_por_mes

class EliminarController(QWidget, eliminar_widget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		self.BtnGenerar.clicked.connect(self.generar)

	def generar(self):
		inicio = self.ETDesde.text()
		fin = self.ETHasta.text()
		
		button = si_no_mensaje("Advertencia..!!","Esta acción es irreversible, desea continuar?")

		if button == QMessageBox.Yes:
			print("Yes!")
		else:
			print("No!")
			return
		fechas = listar_fechas_por_mes(Fecha(inicio) , Fecha(fin))
		for index, fecha in enumerate(fechas):
			print( fecha)
			eliminar_datos(Fecha(fecha))
			self.PBEstado.setValue( int( ((index + 1) / len(fechas)) * 100))

	