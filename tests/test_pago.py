from src.pago.pago import PagoTarjeta, PagoEfectivo, PagoTransferencia


def test_pago_tarjeta_exitoso():
    pago = PagoTarjeta("1234567812345678")
    assert pago.procesar_pago(100.0) is True


def test_pago_efectivo_exitoso():
    pago = PagoEfectivo()
    assert pago.procesar_pago(50.0) is True


def test_pago_transferencia_exitoso():
    pago = PagoTransferencia("00112233445")
    assert pago.procesar_pago(75.0) is True


def test_pago_monto_invalido_falla():
    pago = PagoEfectivo()
    assert pago.procesar_pago(0) is False
