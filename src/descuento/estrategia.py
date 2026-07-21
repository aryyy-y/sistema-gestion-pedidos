from abc import ABC, abstractmethod

class EstrategiaDescuento(ABC):
    @abstractmethod
    def calcular(self, subtotal: float) -> float:
        pass

class DescuentoPorcentaje(EstrategiaDescuento):
    def __init__(self, porcentaje: float):
        self.porcentaje = porcentaje

    def calcular(self, subtotal: float) -> float:
        return subtotal * (self.porcentaje / 100)

class DescuentoFijo(EstrategiaDescuento):
    def __init__(self, monto: float):
        self.monto = monto

    def calcular(self, subtotal: float) -> float:
        return min(self.monto, subtotal)
    