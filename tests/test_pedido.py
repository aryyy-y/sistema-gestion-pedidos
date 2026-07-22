from src.pedido.pedido import Pedido, RegistradorPedido
from src.pago.pago import PagoEfectivo
from src.descuento.estrategia import DescuentoFijo


def test_calcular_total_sin_descuento():
    pedido = Pedido(subtotal=100.0, estrategia_pago=PagoEfectivo())
    assert pedido.calcular_total() == 100.0


def test_calcular_total_con_descuento():
    pedido = Pedido(subtotal=100.0, estrategia_pago=PagoEfectivo(), descuento=DescuentoFijo(30.0))
    assert pedido.calcular_total() == 70.0


def test_calcular_total_no_es_negativo():
    pedido = Pedido(subtotal=20.0, estrategia_pago=PagoEfectivo(), descuento=DescuentoFijo(50.0))
    assert pedido.calcular_total() == 0.0


def test_confirmar_pedido_exitoso():
    pedido = Pedido(subtotal=50.0, estrategia_pago=PagoEfectivo())
    assert pedido.confirmar_pedido() is True


def test_observador_es_notificado_al_confirmar_pedido():
    pedido = Pedido(subtotal=50.0, estrategia_pago=PagoEfectivo())
    registrador = RegistradorPedido()
    pedido.agregar_observador(registrador)
    pedido.confirmar_pedido()
    assert "pedido confirmado" in registrador.eventos
