from src.pago.pago import EstrategiaPago, PagoTarjeta, PagoEfectivo, PagoTransferencia


class FactoryPago:
    @staticmethod
    def crear_metodo_pago(tipo: str, **kwargs) -> EstrategiaPago:
        tipo = tipo.lower()
        if tipo == "tarjeta":
            return PagoTarjeta(numero_tarjeta=kwargs.get("numero_tarjeta", "0000000000000000"))
        elif tipo == "efectivo":
            return PagoEfectivo()
        elif tipo == "transferencia":
            return PagoTransferencia(cuenta_destino=kwargs.get("cuenta_destino", "000000000"))
        else:
            raise ValueError(f"Método de pago no soportado: {tipo}")
