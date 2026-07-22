from abc import ABC, abstractmethod
from src.pago.pago import EstrategiaPago, PagoEfectivo, PagoTransferencia
from src.notificacion.notificacion import CanalEnvio, CanalEmail, CanalSMS


class FabricaEntorno(ABC):
    """Abstract Factory: crea familias de objetos relacionados y consistentes según el entorno."""

    @abstractmethod
    def crear_metodo_pago(self) -> EstrategiaPago:
        pass

    @abstractmethod
    def crear_canal_notificacion(self) -> CanalEnvio:
        pass


class FabricaDesarrollo(FabricaEntorno):
    def crear_metodo_pago(self) -> EstrategiaPago:
        return PagoEfectivo()

    def crear_canal_notificacion(self) -> CanalEnvio:
        return CanalEmail()


class FabricaProduccion(FabricaEntorno):
    def crear_metodo_pago(self) -> EstrategiaPago:
        return PagoTransferencia(cuenta_destino="CTA-PROD-0001")

    def crear_canal_notificacion(self) -> CanalEnvio:
        return CanalSMS()


def obtener_fabrica(entorno: str) -> FabricaEntorno:
    entorno = entorno.lower()
    if entorno in ("produccion", "production", "prod"):
        return FabricaProduccion()
    return FabricaDesarrollo()
