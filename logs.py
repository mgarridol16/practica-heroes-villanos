import logging
import os
from datetime import datetime



class Log:

    def __init__(self):
            #creo la carpeta si no existe
        if not os.path.exists("log"):
            os.mkdir("log")
        fecha = datetime.now().strftime("%Y%m%d")
        self.ruta = f"log/{fecha}-personajes.log"

        logging.basicConfig(
            filename=self.ruta,
            level=logging.INFO,
            format="[%(asctime)s] [%(levelname)s] %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
            encoding="utf-8"
        )
        self.logger = logging.getLogger()

    def escribir(self, tipo, mensaje):
        tipo_limpio = tipo.upper()

        # Delegamos en los métodos propios de la librería logging
        if tipo_limpio == "WARNING":
            self.logger.warning(mensaje)
        elif tipo_limpio == "ERROR":
            self.logger.error(mensaje)
        else:
            self.logger.info(mensaje)