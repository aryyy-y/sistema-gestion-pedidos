from src.inventario.inventario import InventarioAdapter, SistemaInventarioExterno


def test_agregar_y_obtener_stock():
    inv = InventarioAdapter()
    inv.agregar_producto("camiseta", 10)
    assert inv.obtener_stock("camiseta") == 10


def test_reducir_stock_exitoso():
    inv = InventarioAdapter()
    inv.agregar_producto("camiseta", 10)
    assert inv.reducir_stock("camiseta", 4) is True
    assert inv.obtener_stock("camiseta") == 6


def test_reducir_stock_insuficiente_falla():
    inv = InventarioAdapter()
    inv.agregar_producto("camiseta", 3)
    assert inv.reducir_stock("camiseta", 5) is False
    assert inv.obtener_stock("camiseta") == 3


def test_adapter_usa_sistema_externo_inyectado():
    sistema_externo = SistemaInventarioExterno()
    sistema_externo.registrar_existencia("pantalon", 20)
    inv = InventarioAdapter(sistema_externo)
    assert inv.obtener_stock("pantalon") == 20
