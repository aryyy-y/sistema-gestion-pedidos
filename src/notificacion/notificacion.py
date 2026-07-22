from abc import ABC, abstractmethod


class CanalEnvio(ABC):
    """Implementación del Bridge: define CÓMO se envía el mensaje."""

    @abstractmethod
    def enviar_mensaje(self, mensaje: str, destinatario: str) -> bool:
        pass


class CanalEmail(CanalEnvio):
    def enviar_mensaje(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando Email a {destinatario}: {mensaje}")
        return True


class CanalSMS(CanalEnvio):
    def enviar_mensaje(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando SMS a {destinatario}: {mensaje}")
        return True


class Notificacion(ABC):
    """Abstracción del Bridge: define QUÉ tipo de notificación es, delega el envío al canal."""

    def __init__(self, canal: CanalEnvio):
        self.canal = canal

    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        pass


class NotificacionNormal(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        return self.canal.enviar_mensaje(mensaje, destinatario)


class NotificacionUrgente(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        return self.canal.enviar_mensaje(f"[URGENTE] {mensaje}", destinatario)
