from src.notificacion.notificacion import NotificacionEmail, NotificacionSMS

def test_enviar_notificacion_email():
    email = NotificacionEmail()
    resultado = email.enviar("Su pedido está listo", "cliente@test.com")
    assert resultado is True

def test_enviar_notificacion_sms():
    sms = NotificacionSMS()
    resultado = sms.enviar("Su código de verificación es 1234", "555-1234")
    assert resultado is True
    