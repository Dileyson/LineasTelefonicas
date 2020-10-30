import sys

from PyQt5.QtCore import QRegExp
from PyQt5.QtWidgets import QMainWindow, QApplication, QDialog, QMessageBox
#QMainWindow: Para adminiistrar la ventana
#QApplication: Para administrar la aplicación
from PyQt5 import uic #Para cargar el archivo .ui
from PyQt5.QtGui import QFont, QRegExpValidator, QIntValidator  # Para trabajar con fuentes
#import LineaTelefonica
from Mundo import Empresa, LineaTelefonica




class MainLineaTelefonica(QMainWindow):
	def __init__(self):
		QMainWindow.__init__(self)
		uic.loadUi("gui/MainWindowsLineaTelefonica.ui", self)
		self.setFixedSize(self.size())
		self.setWindowTitle("Cambiando el titulo de la ventana")
		qfont = QFont("Arial", 7, QFont.Bold)
		self.setFont(qfont)
		self.empresa = Empresa()
		self.dialogo_agregar_llamada = DialogoAgregarLlamada()
		self.configurar()


	def closeEvent(self, event):
		resultado = QMessageBox.question(self, "Salir ...", "¿Seguro desea salir de la aplicación?", QMessageBox.Yes | QMessageBox.No)
		if resultado == QMessageBox.Yes: event.accept()
		else: event.ignore()


	def configurar(self):
		self.pbtn_agregar_llamada_linea1.clicked.connect(self.abrir_dialogo_agregar_llamada_linea1)
		self.pbtn_agregar_llamada_linea2.clicked.connect(self.abrir_dialogo_agregar_llamada_linea2)
		self.pbtn_agregar_llamada_linea3.clicked.connect(self.abrir_dialogo_agregar_llamada_linea3)
		self.pbtn_agregar_llamada_linea4.clicked.connect(self.abrir_dialogo_agregar_llamada_linea_celular)
		self.pbtn_reiniciar.clicked.connect(self.reiniciar_linea_base)

	def reiniciar_linea_base(self):
		self.empresa.darLinea1().reiniciar()
		self.empresa.darLinea2().reiniciar()
		self.empresa.darLinea3().reiniciar()
		self.empresa.darCelular().reiniciar()

		self.le_numero_llamada_linea1.setText(str(self.empresa.darLinea1().darNumeroLlamadas()))
		self.le_numero_minutos_linea1.setText(str(self.empresa.darLinea1().darNumeroMinutos()))

		self.le_numero_llamada_linea2.setText(str(self.empresa.darLinea2().darNumeroLlamadas()))
		self.le_numero_minutos_linea2.setText(str(self.empresa.darLinea2().darNumeroMinutos()))

		self.le_numero_llamada_linea3.setText(str(self.empresa.darLinea3().darNumeroLlamadas()))
		self.le_numero_minutos_linea3.setText(str(self.empresa.darLinea3().darNumeroMinutos()))

		self.le_costo_linea1.setText(str(self.empresa.darLinea1().darCostoLlamadas()))
		self.le_costo_linea2.setText(str(self.empresa.darLinea2().darCostoLlamadas()))
		self.le_costo_linea3.setText(str(self.empresa.darLinea3().darCostoLlamadas()))

		self.le_valor_totales.setText(str(self.empresa.darTotalCostoLlamadas()))
		self.le_numero_llamada_totales.setText(str(self.empresa.darTotalNumeroLlamadasDesdeLineasNoAlternativas()))
		self.le_numero_minutos_totales.setText(str(self.empresa.darTotalMinutos()))
		self.le_costo_promedio_totales.setText(str(self.empresa.darCostoPromedioMinuto()))

		self.le_numero_llamada_linea4.setText(str(self.empresa.darCelular().darNumeroLlamadas()))
		self.le_numero_minutos_local_linea4.setText(str(self.empresa.darCelular().darNumeroMinutosLocal()))
		self.le_numero_minutos_celulares_linea4.setText(str(self.empresa.darCelular().darNumeroMinutosCelular()))
		self.le_costo_linea4.setText(str(self.empresa.darLinea3().darCostoLlamadas()))
		self.le_valor_totales.setText(str(self.empresa.darTotalMinutosDesdeLineasAlternativas()))


	def abrir_dialogo_agregar_llamada_linea1(self):
		respuesta= self.dialogo_agregar_llamada.exec()
		if respuesta==QDialog.Accepted:
			numero_minutos_hablados = int(self.dialogo_agregar_llamada.le_numero_minutos_hablados.text())
			self.empresa.agregarLlamadaLocalLinea1(numero_minutos_hablados)
			#print(self.empresa.darLinea1().darNumeroLlamadas())
			self.le_numero_llamada_linea1.setText(str(self.empresa.darLinea1().darNumeroLlamadas()))
			self.le_numero_minutos_linea1.setText(str(self.empresa.darLinea1().darNumeroMinutos()))
			self.le_costo_linea1.setText(str(self.empresa.darLinea1().darCostoLlamadas()))
			self.le_valor_totales.setText(str(self.empresa.darTotalCostoLlamadas()))
			self.le_numero_llamada_totales.setText(str(self.empresa.darTotalNumeroLlamadasDesdeLineasNoAlternativas()))
			self.le_numero_minutos_totales.setText(str(self.empresa.darTotalMinutos()))
			self.le_costo_promedio_totales.setText(str(self.empresa.darCostoPromedioMinuto()))
		else:
			print("r")
			#self.le_costo_linea1.setText(numero_minutos_hablados)
			pass

	def abrir_dialogo_agregar_llamada_linea2(self):
		respuesta = self.dialogo_agregar_llamada.exec()

		if respuesta == QDialog.Accepted:
			numero_minutos_hablados = int(self.dialogo_agregar_llamada.le_numero_minutos_hablados.text())
			self.empresa.agregarLlamadaLocalLinea2(numero_minutos_hablados)
			#print(self.empresa.darLinea1().darNumeroLlamadas())
			self.le_numero_llamada_linea2.setText(str(self.empresa.darLinea2().darNumeroLlamadas()))
			self.le_numero_minutos_linea2.setText(str(self.empresa.darLinea2().darNumeroMinutos()))
			self.le_costo_linea2.setText(str(self.empresa.darLinea2().darCostoLlamadas()))
			self.le_valor_totales.setText(str(self.empresa.darTotalCostoLlamadas()))
			self.le_numero_llamada_totales.setText(str(self.empresa.darTotalNumeroLlamadasDesdeLineasNoAlternativas()))
			self.le_numero_minutos_totales.setText(str(self.empresa.darTotalMinutos()))
			self.le_costo_promedio_totales.setText(str(self.empresa.darCostoPromedioMinuto()))
		else:
			pass

	def abrir_dialogo_agregar_llamada_linea3(self):
		respuesta = self.dialogo_agregar_llamada.exec()
		#global numero_minutos_hablados
		if respuesta == QDialog.Accepted:
			numero_minutos_hablados = int(self.dialogo_agregar_llamada.le_numero_minutos_hablados.text())
			self.empresa.agregarLlamadaLocalLinea3(numero_minutos_hablados)
			#print(self.empresa.darLinea1().darNumeroLlamadas())
			self.le_numero_llamada_linea3.setText(str(self.empresa.darLinea3().darNumeroLlamadas()))
			self.le_numero_minutos_linea3.setText(str(self.empresa.darLinea3().darNumeroMinutos()))
			self.le_costo_linea3.setText(str(self.empresa.darLinea3().darCostoLlamadas()))
			self.le_valor_totales.setText(str(self.empresa.darTotalCostoLlamadas()))
			self.le_numero_llamada_totales.setText(str(self.empresa.darTotalNumeroLlamadasDesdeLineasNoAlternativas()))
			self.le_numero_minutos_totales.setText(str(self.empresa.darTotalMinutos()))
			self.le_costo_promedio_totales.setText(str(self.empresa.darCostoPromedioMinuto()))
		else:
			print("r")
			#self.le_costo_linea1.setText(numero_minutos_hablados)
			pass

	def abrir_dialogo_agregar_llamada_linea_celular(self):
		respuesta = self.dialogo_agregar_llamada.exec()
		if respuesta == QDialog.Accepted:
			numero_minutos_hablados = int(self.dialogo_agregar_llamada.le_numero_minutos_hablados.text())
			self.empresa.agregarLlamadaCelularCelular(numero_minutos_hablados)
			self.le_numero_llamada_linea4.setText(str(self.empresa.darCelular().darNumeroLlamadas()))
			self.le_numero_minutos_local_linea4.setText(str(self.empresa.darCelular().darNumeroMinutosLocal()))
			self.le_numero_minutos_celulares_linea4.setText(str(self.empresa.darCelular().darNumeroMinutosCelular()))
			self.le_costo_linea4.setText(str(self.empresa.darLinea3().darCostoLlamadas()))
			self.le_numero_minutos_totales_alternativo.setText(str(self.empresa.darTotalMinutosDesdeLineasAlternativas()))
			self.le_numero_llamada_totales_alternativo.setText(str(self.empresa.darTotalNumeroLlamadasDesdeLineasAlternativas()))
			self.le_numero_minutos_totales_alternativo.setText(str(self.empresa.darTotalMinutosDesdeLineasAlternativas()))
			self.le_numero_minutos_totales_alternativo.setText(str(self.empresa.darCostoPromedioMinutosDeLineasAlternativas()))
		else:
			print("r")
			pass
class DialogoAgregarLlamada(QDialog):
	def __init__(self):
		QDialog.__init__(self)
		uic.loadUi("gui/DialogoAgregarLlamada1.ui", self)
		self.setFixedSize((self.size()))
		self.__configurar()

	def __configurar(self):
		self.le_numero_minutos_hablados.setValidator(QIntValidator(1, 999, self.le_numero_minutos_hablados))


if __name__== "__main__":
	app = QApplication(sys.argv)
	win = MainLineaTelefonica()
	win.show()
	sys.exit(app.exec_())


