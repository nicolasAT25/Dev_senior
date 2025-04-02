'''class ErrorPersonalizado(Exception):
    def __init__(self, mensaje):
        super().__init__(mensaje)
        
try:
    raise ErrorPersonalizado("Esto es un ejemplo de error personalizado.")
except ErrorPersonalizado as e:
    print(f"Se caprutó un error: {e}")'''
    
    
'''
NIVELES DE LOGGIN
- Debug
- Info
- Warning
- Error
- Critical
'''
    
'''import logging

logging.basicConfig(
    # level=logging.ERROR,
    level=logging.INFO, # Si lo dejo desde el level ERROR no se ejecuta el else
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("Errores.log"),
        logging.StreamHandler()
    ]
)

try:
    # 1/0
    1/2
except ZeroDivisionError as e:
    logging.error(f"Error capturado: {e}")
else:
    logging.info("La división fue todo un éxito!")'''
    
    
# Sistema con varias peticiones en paralelo
'''import asyncio

async def tarea():
    
    try:
        await asyncio.sleep(1)
        raise ValueError("Error en tarea asíncrona.")
    except ValueError as e:
        print(f"Error capturado en async: {e}")
        
asyncio.run(tarea())'''

import psycopg
import logging

logging.basicConfig(
    # level=logging.ERROR,
    level=logging.INFO, # Si lo dejo desde el level ERROR no se ejecuta el else
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("Errores_db.log"),
        logging.StreamHandler()
    ]
)

try:
    conn = psycopg.connect(host= "localhost", dbname="cualquiera", user="nicolasat", password="1234")
except psycopg.OperationalError as e:
    # print(f"Error de conexión contra la DB: {e}")
    logging.error(f"Error de conexión contra la DB: {e}")