from src.notificacion.notificacion import NotificacionNormal, NotificacionUrgente, CanalEmail, CanalSMS


def test_enviar_notificacion_email():
    notificacion = NotificacionNormal(CanalEmail())
    assert notificacion.enviar("Tu pedido fue confirmado", "cliente@correo.com") is True


def test_enviar_notificacion_sms():
    notificacion = NotificacionNormal(CanalSMS())
    assert notificacion.enviar("Tu pedido fue confirmado", "5512345678") is True


def test_notificacion_urgente_marca_el_mensaje(capsys):
    notificacion = NotificacionUrgente(CanalEmail())
    notificacion.enviar("Stock agotado", "admin@correo.com")
    salida = capsys.readouterr().out
    assert "[URGENTE]" in salida


def test_misma_notificacion_con_distintos_canales():
    urgente_sms = NotificacionUrgente(CanalSMS())
    assert urgente_sms.enviar("Aviso", "5500000000") is True
