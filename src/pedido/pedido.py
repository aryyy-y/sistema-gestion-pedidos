from abc import ABC, abstractmethod
from src.pago.pago import EstrategiaPago
from src.descuento.estrategia import EstrategiaDescuento


class ObservadorPedido(ABC):
    @abstractmethod
    def actualizar(self, pedido: "Pedido", evento: str) -> None:
        pass


class RegistradorPedido(ObservadorPedido):
    """Observador de ejemplo: lleva un registro de los eventos del pedido."""

    def __init__(self):
        self.eventos = []

    def actualizar(self, pedido: "Pedido", evento: str) -> None:
        self.eventos.append(evento)
        print(f"[Pedido] {evento} (total: {pedido.calcular_total():.2f})")


class Pedido:
    def __init__(self, subtotal: float, estrategia_pago: EstrategiaPago, descuento: EstrategiaDescuento = None):
        self.subtotal = subtotal
        self.estrategia_pago = estrategia_pago
        self.descuento = descuento
        self._observadores = []

    def agregar_observador(self, observador: ObservadorPedido) -> None:
        self._observadores.append(observador)

    def _notificar(self, evento: str) -> None:
        for observador in self._observadores:
            observador.actualizar(self, evento)

    def calcular_total(self) -> float:
        total = self.subtotal
        if self.descuento:
            total -= self.descuento.calcular(self.subtotal)
        return max(0.0, total)

    def confirmar_pedido(self) -> bool:
        total = self.calcular_total()
        resultado = self.estrategia_pago.procesar_pago(total)
        self._notificar("pedido confirmado" if resultado else "pago fallido")
        return resultado
