import os
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget
from PySide6.QtWidgets import QMessageBox, QFileDialog
from views.general_custom_ui import GeneralCustomUi

from views.agregar_boletin_widget import AgregarBoletinWidget

from modulos.MessageBox import si_no_mensaje, mensaje_simple
from modulos.exportaciones import Exportaciones
from modulos.Fecha import Fecha
import traceback
from controllers.template_table import TemplateTable

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
		
		index = self.cb_separador.currentIndex()
		if index == 0:
			sep = "\t"
		elif index == 1:
			sep = ","
		elif index == 2:
			sep= ";"
		else:
			mensaje_simple("Error", "No se definio un separador")
			return
		editText = self.ETNombreArchivo
		editText.setText(None)
		self.LArchivo.setText(None)
		self.LCheck.setText(None)
		fname= QFileDialog.getOpenFileName(None, 'Seleccionar Archivo',filter='(*.csv)')
		try:
			self.exportaciones = Exportaciones(fname[0], sep)
			fecha = self.exportaciones.get_fecha()
			editText.setText(fname[0])
			if isinstance(fecha, Fecha):
				self.LArchivo.setText(str(fecha))
				self.LCheck.setText("✅")
				datos_muestra =  self.exportaciones.head(10)
				tabla = TemplateTable()
				tabla.settings_table(datos_muestra.columns, (200,100,200,200,200,200), datos_muestra.values)
				tabla.show()
			else:
				mensaje_simple("Error", "No es un archivo válido")
		except Exception as e:
			traceback.print_exc()
			mensaje_simple("Error", f"Ha ocurrido un error: {str(e)}")
		

	
	def limpiar_ventana(self):
		self.LArchivo.setText(None)
		self.LCheck.setText(None)
		self.ETNombreArchivo.setText(None)
		self.PBEstado.setValue(0)
		self.cb_separador.setCurrentIndex(0)
		
	def __Generar(self):
		resultado = self.exportaciones.save()
		if resultado['resultado']:
			mensaje_simple("Carga finalizada", f'''
- Cargados {resultado['cargados']} datos,
- Excluidos {resultado['excluidos']} datos,
- Total de datos = {resultado['total']}
			''')
		
		
		# get_balance( filename, {"fecha":fecha, "progress_bar":self.PBEstado, "duplicado":duplicado})
		self.limpiar_ventana()
	def validar_datos(filename: str) -> bool:
		'''
		Devuelve True o False si es un archivo de exportaciones del bcp

		parametro:
			filename: path del archivo
		return
			True o False
		'''
		pass