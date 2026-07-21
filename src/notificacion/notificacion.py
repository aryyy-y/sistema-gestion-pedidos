from abc import ABC, abstractmethod

class Notificacion(ABC):
    @abstractmethod
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        pass

class NotificacionEmail(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando Email a {destinatario}: {mensaje}")
        return True

class NotificacionSMS(Notificacion):
    def enviar(self, mensaje: str, destinatario: str) -> bool:
        print(f"Enviando SMS a {destinatario}: {mensaje}")
        return True