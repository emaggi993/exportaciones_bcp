import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog
from views.general_custom_ui import GeneralCustomUi

from views.agregar_boletin_widget import AgregarBoletinWidget

from modulos.MessageBox import si_no_mensaje, mensaje_simple

class AgregarBoletinForm(QWidget, AgregarBoletinWidget):
	def __init__(self, parent=None):
		super().__init__(parent)

		self.setupUi(self)
		self.ui = GeneralCustomUi(self)
		self.set_buttons()

	def mousePressEvent(self, event) -> None:
		self.ui.mouse_press_event(event)

	def set_buttons(self):
		self.BtnSeleccionarArchivo.clicked.connect(self.__buscarArchivo)
		self.BtnGenerar.clicked.connect(self.__Generar)

	def __buscarArchivo(self):
		editText = self.ETNombreArchivo
		editText.setText(None)
		self.LArchivo.setText(None)
		self.LCheck.setText(None)
		fname= QFileDialog.getOpenFileName(None, 'Seleccionar Archivo','')
		editText.setText(fname[0])
		

	
	def limpiar_ventana(self):
		self.LArchivo.setText(None)
		self.LCheck.setText(None)
		self.ETNombreArchivo.setText(None)
		self.RBFinanciera.setChecked(False)
		self.PBEstado.setValue(0)
		
	def __Generar(self):
		fecha = self.LArchivo.text()
		filename = self.ETNombreArchivo.text()
		if self.RBBanco.isChecked():
			tipo = "B"
		elif self.RBFinanciera.isChecked():
			tipo = "F"
		else:
			mensaje_simple("Error..", "Debe seleccionar un tipo")
			return 
		duplicado = False
		
		
		# get_balance( filename, {"fecha":fecha, "progress_bar":self.PBEstado, "duplicado":duplicado})
		self.limpiar_ventana()