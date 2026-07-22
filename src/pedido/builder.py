from src.pedido.pedido import Pedido
from src.pago.pago import EstrategiaPago
from src.descuento.estrategia import EstrategiaDescuento


class PedidoBuilder:
    def __init__(self):
        self._subtotal = 0.0
        self._estrategia_pago = None
        self._descuento = None

    def con_subtotal(self, subtotal: float) -> "PedidoBuilder":
        self._subtotal = subtotal
        return self

    def con_pago(self, estrategia_pago: EstrategiaPago) -> "PedidoBuilder":
        self._estrategia_pago = estrategia_pago
        return self

    def con_descuento(self, descuento: EstrategiaDescuento) -> "PedidoBuilder":
        self._descuento = descuento
        return self

    def construir(self) -> Pedido:
        if self._estrategia_pago is None:
            raise ValueError("El pedido requiere una estrategia de pago")
        return Pedido(
            subtotal=self._subtotal,
            estrategia_pago=self._estrategia_pago,
            descuento=self._descuento,
        )
