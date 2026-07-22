from abc import ABC, abstractmethod
from typing import Dict, List


class ObservadorInventario(ABC):
    @abstractmethod
    def actualizar(self, producto: str, stock_actual: int) -> None:
        pass


class NotificadorStockBajo(ObservadorInventario):
    def __init__(self, umbral: int = 5):
        self.umbral = umbral

    def actualizar(self, producto: str, stock_actual: int) -> None:
        if stock_actual <= self.umbral:
            print(f"⚠️  Stock bajo de '{producto}': quedan {stock_actual} unidades")


class Inventario:
    def __init__(self):
        self._stock: Dict[str, int] = {}
        self._observadores: List[ObservadorInventario] = []

    def agregar_observador(self, observador: ObservadorInventario) -> None:
        self._observadores.append(observador)

    def agregar_producto(self, producto: str, cantidad: int) -> None:
        self._stock[producto] = self._stock.get(producto, 0) + cantidad

    def obtener_stock(self, producto: str) -> int:
        return self._stock.get(producto, 0)

    def reducir_stock(self, producto: str, cantidad: int) -> bool:
        disponible = self._stock.get(producto, 0)
        if cantidad <= 0 or cantidad > disponible:
            return False
        self._stock[producto] = disponible - cantidad
        self._notificar(producto, self._stock[producto])
        return True

    def _notificar(self, producto: str, stock_actual: int) -> None:
        for observador in self._observadores:
            observador.actualizar(producto, stock_actual)
