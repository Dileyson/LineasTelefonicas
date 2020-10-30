class LineaTelefonicaC():

	def __init__(self):
		self.numeroLlamadas = 0
		self.numeroMinutos = 0
		self.costoLlamadas = 0
		
	def reiniciar(self):
		self.inicializar()

	def inicializar(self):
		self.numeroLlamadas = 0
		self.numeroMinutos = 0
		self.costoLlamadas = 0

	def darCostoLlamadas(self):
		return self.costoLlamadas

	def darNumeroLlamadas(self):
		return self.numeroLlamadas

	def darNumeroMinutos(self):
		return self.numeroMinutos

	def agregarLlamadalocaal(self, minutos):
		Empresa.EmpresaC.matodo1()
		self.numeroLlamadas = self.numeroLlamadas + 1
		self.numeroMinutos = self.numeroMinutos + 4 #4 es minuto
		self.costoLlamadas = self.costoLlamadas + ( 4 * 35 )

	def agregarLlamadaLargaDistancia(self, minutos):
		self.numeroLlamadas = self.numeroLlamadas + 1
		self.numeroMinutos = self.numeroMinutos + minutos
		self.costoLlamadas = self.costoLlamadas + ( minutos * 380 )

	def agregarLlamadaCelular(self, minutos):
		self.numeroLlamadas = self.numeroLlamadas + 1
		self.numeroMinutos = self.numeroMinutos + minutos;
		self.costoLlamadas = self.costoLlamadas + ( minutos * 999 )

import LineaTelefonica


class EmpresaC():

    def __init__(self):
        self.linea1 = LineaTelefonica.LineaTelefonicaC
        self.linea2 = LineaTelefonica.LineaTelefonicaC
        self.linea3 = LineaTelefonica.LineaTelefonicaC

    def inicializar(self):
        self.linea1.inicializar()
        self.linea2.inicializar()
        self.linea3.inicializar()

    def reiniciar(self):
        self.linea1.reiniciar()
        self.linea2.reiniciar()
        self.linea3.reiniciar()

    def darLinea1(self):
        return self.linea1

    def darLinea2(self):
        return self.linea2

    def darLinea3(self):
        return self.linea3

    def agregarLlamadaLocalLinea1(self, minutos):
        self.linea1.agregarLlamadalocaal(minutos)

    def agregarLlamadaLocalLinea2(self, minutos):
        self.linea2.agregarLlamadalocaal(minutos)

    def agregarLlamadaLocalLinea3(self, minutos):
        self.linea3.agregarLlamadalocaal(minutos)

    def agregarLlamadaDistanciaLinea1(self, minutos):
        self.linea1.agregarLlamadaLargaDistancia(minutos)

    def agregarLlamadaDistancaiLinea2(self, minutos):
        self.linea2.agregarLlamadaLargaDistancia(minutos)

    def agregarLlamadaDistancaiLinea3(self, minutos):
        self.linea3.agregarLlamadaLargaDistancia(minutos)

    def agregarLlamadaCelularLinea1(self, minutos):
        self.linea1.agregarLlamadaCelular(minutos)

    def agregarLlamadaCelularLinea2(self, minutos):
        self.linea2.agregarLlamadaCelular(minutos)

    def agregarLlamadaCelularLinea3(self, minutos):
        self.linea3.agregarLlamadaCelular(self, minutos)

    def darTotalNumeroLlamadas(self):
        total = self.linea1.darNumeroLlamadas() + self.linea2.darNumeroLlamadas() + self.linea3.darNumeroLlamadas()
        return total

    def darTotalMinutos(self):
        total = self.linea1.darNumeroMinutos() + self.linea2.darNumeroMinutos() + self.linea3.darNumeroMinutos()
        return total

    def darTotalCostoLlamadas(self):
        total = self.linea1.darCostoLlamadas() + self.linea2.darCostoLlamadas() + self.linea3.darCostoLlamadas()
        return total

    def darCostoPromedioMinuto(self):
        promedio = self.darTotalCostoLlamadas() / self.darTotalMinutos()
        return promedio

    def matodo1(self):
        return "Respuesta 1"

    def matodo2(self):
        return "Respuesta 2"
