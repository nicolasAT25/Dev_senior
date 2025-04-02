'''
logger: lo activo para generar los mensajes.
handlres: 
format: timestamp.
level: de los loggins o eventos.

Los logs se pueden mandar a archivos .log para hacer mantenimiento al software.
Refactorizar es implementar una nueva librería que hace más sencillo el código.
'''

'''
NIVELES DE LOGGIN
- Debug
- Info
- Warning
- Error
- Critical
'''

import logging

# Los loggins aparecerán en consola
logging.basicConfig(level=logging.DEBUG,    # mostrar desde debug que es el primer nivel hacia abajo
                    format='%(asctime)s - %(levelname)s - %(message)s',                    
                    ) 

# Estos mensajes se deben comentar y no es tan escalable y mantenible.
logging.debug("Este es un mensaje de debug")
logging.info("Este es un mensaje informativo")
logging.warning("Este es un mensaje de advertencia")
logging.error("Este es un mensaje de ERROR")
logging.critical("Este es un mensaje SERIO que puede detener el software...")