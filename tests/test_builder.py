import pytest
from src.pedido.builder import PedidoBuilder
from src.pago.pago import PagoEfectivo
from src.descuento.estrategia import DescuentoPorcentaje


def test_builder_construye_pedido_simple():
    pedido = (
        PedidoBuilder()
        .con_subtotal(100.0)
        .con_pago(PagoEfectivo())
        .construir()
    )
    assert pedido.subtotal == 100.0
    assert pedido.calcular_total() == 100.0


def test_builder_construye_pedido_con_descuento():
    pedido = (
        PedidoBuilder()
        .con_subtotal(200.0)
        .con_pago(PagoEfectivo())
        .con_descuento(DescuentoPorcentaje(10.0))
        .construir()
    )
    assert pedido.calcular_total() == 180.0


def test_builder_sin_pago_lanza_error():
    with pytest.raises(ValueError):
        PedidoBuilder().con_subtotal(50.0).construir()
