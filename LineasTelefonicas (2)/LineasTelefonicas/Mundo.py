class LineaTelefonica:

    def __init__(self):
        self.numeroLlamadas = 0
        self.numeroMinutos = 0
        self.costoLlamadas = 0

    def reiniciar(self):
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
        self.numeroLlamadas = self.numeroLlamadas + 1
        self.numeroMinutos = self.numeroMinutos + minutos
        self.costoLlamadas = self.costoLlamadas + (minutos * 35)

    def agregarLlamadaLargaDistancia(self, minutos):
        self.numeroLlamadas = self.numeroLlamadas + 1
        self.numeroMinutos = self.numeroMinutos + minutos
        self.costoLlamadas = self.costoLlamadas + (minutos * 380)

    def agregarLlamadaCelular(self, minutos):
        self.numeroLlamadas = self.numeroLlamadas + 1
        self.numeroMinutos = self.numeroMinutos + minutos
        self.costoLlamadas = self.costoLlamadas + (minutos * 999)

    def modificarCostoLlamada(self, costoLlamada):
        self.costoLlamadas = costoLlamada


# --------------------Linea Celular-----------------------
class LineaCelular(LineaTelefonica):
    def _init_(self):
        super().__init__()
        self.numeroMinutosLocal = 0
        self.numeroMinutosCelular = 0
        self.saldoDisponible = 50000

    def darNumeroMinutosLocal(self):
        return self.numeroMinutosLocal

    def darNumeroMinutosCelular(self):
        return self.numeroMinutosCelular

    def darSaldoDisponible(self):
        return self.saldoDisponible

    def agregarLlamadaLocal(self, minutos):
        self.numeroLlamadas += 1
        self.numeroMinutos += minutos
        totalLlamadas = self.darCostoLlamadas() + (minutos * 20)
        self.modificarCostoLlamada(totalLlamadas)
        self.numeroMinutosLocal += minutos
        self.saldoDisponible = self.saldoDisponible - (minutos * 20)

    def agregarLlamadaCelular(self, minutos):
        LineaTelefonica.agregarLlamadaCelular(self, minutos)
        self.modificarCostoLlamada(self.darCostoLlamadas() - (minutos * 989))
        self.numeroMinutosCelular += minutos


# --------------------Empresa-----------------------------
class Empresa:

    def __init__(self):
        self.linea1 = LineaTelefonica()
        self.linea2 = LineaTelefonica()
        self.linea3 = LineaTelefonica()
        self.lineaCelular = LineaCelular()

    def reiniciar(self):
        self.linea1.reiniciar()
        self.linea2.reiniciar()
        self.linea3.reiniciar()
        self.lineaCelular.reiniciar()

    def reiniciarLineasAlternativas(self):
        self.lineaCelular.reiniciar()

    def darLinea1(self):
        return self.linea1

    def darLinea2(self):
        return self.linea2

    def darLinea3(self):
        return self.linea3

    def darCelular(self):
        return self.lineaCelular

    def agregarLlamadaLocalLinea1(self, minutos):
        self.linea1.agregarLlamadalocaal(minutos)

    def agregarLlamadaLocalLinea2(self, minutos):
        self.linea2.agregarLlamadalocaal(minutos)

    def agregarLlamadaLocalLinea3(self, minutos):
        self.linea3.agregarLlamadalocaal(minutos)

    def agregarLlamadaLocalCelular(self, minutos):
        if self.lineaCelular.darSaldoDisponible() > (minutos * 20):
            self.lineaCelular.agregarLlamadaLocal(minutos)
        else:
            raise SaldoInsuficienteError("no hay saldo suficiente para esta llamada")

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
        self.linea3.agregarLlamadaCelular(minutos)

    def agregarLlamadaCelularCelular(self, minutos):
        self.lineaCelular.agregarLlamadaCelular(minutos)

    def darTotalNumeroLlamadasDesdeLineasAlternativas(self):
        return self.lineaCelular.darNumeroLlamadas()

    def darTotalMinutosDesdeLineasAlternativas(self):
        return self.lineaCelular.darNumeroMinutos()

    def darCostoLlamadasDesdeLineasAlternativas(self):
        return self.lineaCelular.darCostoLlamadas()

    def darTotalNumeroLlamadasDesdeLineasNoAlternativas(self):
        total = self.linea1.darNumeroLlamadas() + self.linea2.darNumeroLlamadas() + self.linea3.darNumeroLlamadas()
        return total

    def darTotalMinutos(self):
        total = self.linea1.darNumeroMinutos() + self.linea2.darNumeroMinutos() + self.linea3.darNumeroMinutos()
        return total

    def darTotalCostoLlamadas(self):
        total = self.linea1.darCostoLlamadas() + self.linea2.darCostoLlamadas() + self.linea3.darCostoLlamadas()
        return total

    def darCostoPromedioMinuto(self):
        if(self.darTotalMinutos()>0):
            promedio = self.darTotalCostoLlamadas() / self.darTotalMinutos()
            return promedio
        else:
            raise DivisionPorCeroError("no hay llamadas para hacer este romedio")

    def darCostoPromedioMinutosDeLineasAlternativas(self):
        return self.darCostoLlamadasDesdeLineasAlternativas() / self.darTotalMinutosDesdeLineasAlternativas()

    def darSaldoDisponibleLineasAlternativas(self):
        return self.lineaCelular.darSaldoDisponible()

    def matodo1(self):
        return "Respuesta 1"

    def matodo2(self):
        return "Respuesta 2"


class LineasError(Exception):
    pass


class SaldoInsuficienteError(LineasError):
    def _init_(self, msg):
        self.msg = msg


class DivisionPorCeroError(LineasError):
    def _init_(self, msg):
        self.msg = msg
