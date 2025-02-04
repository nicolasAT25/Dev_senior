import os
import platform
from datetime import datetime
import json


id_count = 1

def limpiar_pantalla():
    op_sys = platform.system()
    if op_sys == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def mostrar_menu():
    print()
    print("\t\tExperimentos App")
    print()

    print("MENÚ\n")
    print("\
    1. Registrar un experimento.\n\
    2. Registrar varios experimentos.\n\
    3. Consultar todos los experimentos.\n\
    4. Consultar todos los experimentos de una categoría.\n\
    5. Consultar un solo experimento de una categoría.\n\
    6. Editar un experimento.\n\
    7. Eliminar un experimento.\n\
    8. Generar informe de los experimentos de una categría.\n\
    9. Generar informe de todos los experimentos.\n\
    10. Salir.")
    print()
    
def mostrar_categorias():
    print()
    print("CATEGORÍAS\n")
    print("\
    a. Física.\n\
    b. Química.\n\
    c. Biología.")
    print()
    
def mostrar_experimentos_fisica():
    print("Experimentos de Física\n")
    print("\
    a. Cálculo del caudal.\n\
    b. Área de un círculo.")
    print()
    
def validar_num_positivo(num:float):
    try:
        res = float(num)
    except Exception as e:
        print(e)
    if num < 0:
        raise 'El número debe ser positivo.'
    
        
def validar_fecha(fecha:str):
    try:
        fecha_formato = datetime.strptime(fecha, "%Y-%m-%d").date()
    except Exception as e:
        raise f'La fecha ingresada no es válida. {e}'
    
    if fecha_formato > datetime.now().date():
        raise 'La fecha ingresada es mayor a la fecha actual.'
    
    return str(fecha)
    
def crear_fisica_caudal(volumen:float, tiempo:float, fecha:str):
    global id_count
    
    # Cálculo
    print(f'Volumen: {volumen}\nTiempo: {tiempo}')    
    res = round(volumen / tiempo, 2)
    
    with open('db_experimentos.json', 'r') as f:
        db = json.load(f)
    
        db['fisica']['caudal']['id'] = id_count
        db['fisica']['caudal']['volumen'] = volumen
        db['fisica']['caudal']['tiempo'] = tiempo
        db['fisica']['caudal']['fecha_experimento'] = fecha
        db['fisica']['caudal']['fecha_registro'] = str(datetime.now().date())
        
        with open('db_experimentos.json', 'w') as f:
            json.dump(db, f)
    
    id_count =+ 1
    
    return f'El caudal del experimento es {res} L/s.\nExperimento registrado con exito!'