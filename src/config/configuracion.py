import os
from typing import Optional

class ConfiguracionSistema:
    _instancia: Optional["ConfiguracionSistema"] = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super(ConfiguracionSistema, cls).__new__(cls)
            cls._instancia._inicializar()
        return cls._instancia

    def _inicializar(self):
        # Carga de variables de entorno o valores por defecto
        self.entorno = os.getenv("ENTORNO", "desarrollo")
        self.impuesto_default = float(os.getenv("IMPUESTO_DEFAULT", "0.16"))
        self.moneda = "MXN"

    def obtener_info(self) -> dict:
        return {
            "entorno": self.entorno,
            "impuesto_default": self.impuesto_default,
            "moneda": self.moneda
        }
    