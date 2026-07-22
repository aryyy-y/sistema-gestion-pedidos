from src.inventario.inventario import Inventario, NotificadorStockBajo


def test_agregar_y_obtener_stock():
    inv = Inventario()
    inv.agregar_producto("camiseta", 10)
    assert inv.obtener_stock("camiseta") == 10


def test_reducir_stock_exitoso():
    inv = Inventario()
    inv.agregar_producto("camiseta", 10)
    assert inv.reducir_stock("camiseta", 4) is True
    assert inv.obtener_stock("camiseta") == 6


def test_reducir_stock_insuficiente_falla():
    inv = Inventario()
    inv.agregar_producto("camiseta", 3)
    assert inv.reducir_stock("camiseta", 5) is False
    assert inv.obtener_stock("camiseta") == 3


def test_observador_es_notificado_en_stock_bajo(capsys):
    inv = Inventario()
    inv.agregar_observador(NotificadorStockBajo(umbral=5))
    inv.agregar_producto("camiseta", 10)
    inv.reducir_stock("camiseta", 6)
    salida = capsys.readouterr().out
    assert "Stock bajo" in salida
