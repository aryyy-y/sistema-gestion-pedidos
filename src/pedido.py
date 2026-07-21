from src.pago.pago import EstrategiaPago
from src.descuento.estrategia import EstrategiaDescuento

class Pedido:
    def __init__(self, subtotal: float, estrategia_pago: EstrategiaPago, descuento: EstrategiaDescuento = None):
        self.subtotal = subtotal
        self.estrategia_pago = estrategia_pago
        self.descuento = descuento

    def calcular_total(self) -> float:
        total = self.subtotal
        if self.descuento:
            total -= self.descuento.calcular(self.subtotal)
        return max(0.0, total)

    def confirmar_pedido(self) -> bool:
        total = self.calcular_total()
        return self.estrategia_pago.procesar_pago(total)
    