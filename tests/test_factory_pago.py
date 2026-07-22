import pytest
from src.pago.factory import FactoryPago
from src.pago.pago import PagoTarjeta, PagoEfectivo, PagoTransferencia


def test_factory_crea_pago_tarjeta():
    pago = FactoryPago.crear_metodo_pago("tarjeta", numero_tarjeta="1111222233334444")
    assert isinstance(pago, PagoTarjeta)


def test_factory_crea_pago_efectivo():
    pago = FactoryPago.crear_metodo_pago("efectivo")
    assert isinstance(pago, PagoEfectivo)


def test_factory_crea_pago_transferencia():
    pago = FactoryPago.crear_metodo_pago("transferencia", cuenta_destino="123456789")
    assert isinstance(pago, PagoTransferencia)


def test_factory_tipo_no_soportado_lanza_error():
    with pytest.raises(ValueError):
        FactoryPago.crear_metodo_pago("criptomoneda")
