from src.entorno.fabrica import FabricaDesarrollo, FabricaProduccion, obtener_fabrica
from src.pago.pago import PagoEfectivo, PagoTransferencia
from src.notificacion.notificacion import CanalEmail, CanalSMS


def test_fabrica_desarrollo_crea_familia_correcta():
    fabrica = FabricaDesarrollo()
    assert isinstance(fabrica.crear_metodo_pago(), PagoEfectivo)
    assert isinstance(fabrica.crear_canal_notificacion(), CanalEmail)


def test_fabrica_produccion_crea_familia_correcta():
    fabrica = FabricaProduccion()
    assert isinstance(fabrica.crear_metodo_pago(), PagoTransferencia)
    assert isinstance(fabrica.crear_canal_notificacion(), CanalSMS)


def test_obtener_fabrica_segun_entorno():
    assert isinstance(obtener_fabrica("produccion"), FabricaProduccion)
    assert isinstance(obtener_fabrica("desarrollo"), FabricaDesarrollo)
    assert isinstance(obtener_fabrica("cualquier_otra_cosa"), FabricaDesarrollo)
