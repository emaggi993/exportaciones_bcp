import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QTableWidget, QTableWidgetItem
from views.general_custom_ui import GeneralCustomUi

from views.template_table_widget import template_table_widget
from modulos.MessageBox import si_no_mensaje, mensaje_simple


class TemplateTable(QWidget, template_table_widget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)


	def settings_table(self, nombreColumnas: tuple, widthColumns: tuple, data: list) -> None:
		# EStablecer altura de las filas
		self.tabla.verticalHeader().setDefaultSectionSize(20)

		# Establecer las etiquetas de encabezado horizontal usando etiquetas
		self.tabla.setColumnCount(len(nombreColumnas))
		self.tabla.setHorizontalHeaderLabels(nombreColumnas)
		# Establecer ancho de las columnas
		for indice, ancho in enumerate(widthColumns, start=0):
			self.tabla.setColumnWidth(indice, ancho)
		self.tabla.resizeRowsToContents()
		self.insert_row(data)
	def insert_row(self, data):
		self.limpiarTabla()
		row= 0
		for fila in data:
			self.tabla.setRowCount( row + 1)
			for c, item in enumerate(fila):
				self.tabla.setItem(row, c, QTableWidgetItem(str(item)))
			row +=1
	def limpiarTabla(self):
		self.tabla.clearContents()
		self.tabla.setRowCount(0)

			
		

	