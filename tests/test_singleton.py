from src.config.configuracion import ConfiguracionSistema

def test_singleton_retorna_misma_instancia():
    a = ConfiguracionSistema()
    b = ConfiguracionSistema()
    assert a is b

def test_singleton_mismos_valores():
    a = ConfiguracionSistema()
    b = ConfiguracionSistema()
    assert a.entorno == b.entorno