from abc import ABC, abstractmethod


class InterfazInventario(ABC):
    """Interfaz que espera nuestro sistema de pedidos."""

    @abstractmethod
    def agregar_producto(self, producto: str, cantidad: int) -> None:
        pass

    @abstractmethod
    def obtener_stock(self, producto: str) -> int:
        pass

    @abstractmethod
    def reducir_stock(self, producto: str, cantidad: int) -> bool:
        pass


class SistemaInventarioExterno:
    """Adaptee: un sistema externo/legado con una interfaz distinta e incompatible."""

    def __init__(self):
        self._existencias = {}

    def registrar_existencia(self, codigo_producto: str, cantidad: int) -> None:
        self._existencias[codigo_producto] = self._existencias.get(codigo_producto, 0) + cantidad

    def consultar_existencia(self, codigo_producto: str) -> int:
        return self._existencias.get(codigo_producto, 0)

    def descontar_existencia(self, codigo_producto: str, cantidad: int) -> bool:
        actual = self._existencias.get(codigo_producto, 0)
        if cantidad <= 0 or cantidad > actual:
            return False
        self._existencias[codigo_producto] = actual - cantidad
        return True


class InventarioAdapter(InterfazInventario):
    """Adapta SistemaInventarioExterno a la interfaz InterfazInventario que espera la app."""

    def __init__(self, sistema_externo: SistemaInventarioExterno = None):
        self._sistema = sistema_externo or SistemaInventarioExterno()

    def agregar_producto(self, producto: str, cantidad: int) -> None:
        self._sistema.registrar_existencia(producto, cantidad)

    def obtener_stock(self, producto: str) -> int:
        return self._sistema.consultar_existencia(producto)

    def reducir_stock(self, producto: str, cantidad: int) -> bool:
        return self._sistema.descontar_existencia(producto, cantidad)
