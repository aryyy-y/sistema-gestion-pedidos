from abc import ABC, abstractmethod


class EstrategiaPago(ABC):
    @abstractmethod
    def procesar_pago(self, monto: float) -> bool:
        pass


class PagoTarjeta(EstrategiaPago):
    def __init__(self, numero_tarjeta: str):
        self.numero_tarjeta = numero_tarjeta

    def procesar_pago(self, monto: float) -> bool:
        print(f"Cobrando ${monto:.2f} a la tarjeta terminada en {self.numero_tarjeta[-4:]}")
        return monto > 0


class PagoEfectivo(EstrategiaPago):
    def procesar_pago(self, monto: float) -> bool:
        print(f"Recibiendo ${monto:.2f} en efectivo")
        return monto > 0


class PagoTransferencia(EstrategiaPago):
    def __init__(self, cuenta_destino: str):
        self.cuenta_destino = cuenta_destino

    def procesar_pago(self, monto: float) -> bool:
        print(f"Transfiriendo ${monto:.2f} a la cuenta {self.cuenta_destino}")
        return monto > 0
