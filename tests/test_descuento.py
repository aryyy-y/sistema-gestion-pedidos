from src.descuento.estrategia import DescuentoFijo, DescuentoPorcentaje

def test_descuento_fijo():
    descuento = DescuentoFijo(50.0)
    assert descuento.calcular(200.0) == 50.0

def test_descuento_porcentaje():
    descuento = DescuentoPorcentaje(10.0)
    assert descuento.calcular(200.0) == 20.0