import os
import platform
from datetime import datetime
import json
import pandas as pd
from IPython.display import display

### Funciones básicas de flujo ###
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
    5. Consultar un solo experimento por ID de una categoría.\n\
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
 
### Funciones de validación de datos ###
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

### Funciones para la "Base de Datos"
def leer_db():
    with open('db_experimentos.json', 'r') as f:
        db = json.load(f)
    return db

def guardar_registo_db(db):
    with open('db_experimentos.json', 'w') as f:
            json.dump(db, f)

# Funciones transversales experimentos            
def leer_experimentos_categoria(categoria:str):
    db = leer_db()
    for i in db[categoria].keys():
        print(f"\t\t\t*{i.title()}*")
        df = pd.DataFrame(db[categoria][i])
        df.set_index("id", inplace=True)
        print(df)
        print()
        
def leer_lista_experimentos(categoria:str, experimento:str):
    db = leer_db()
    df = pd.DataFrame(db[categoria][experimento])
    df.set_index("id", inplace=True)
    print(df)

######### CRUD experimentos FÍSICA #########
    
### Caudal ###
def crear_fisica_caudal(volumen:float, tiempo:float, fecha:str):
    global id_count
    
    # Cálculo
    print(f'Volumen: {volumen}\nTiempo: {tiempo}')    
    res = round(volumen / tiempo, 2)
    
    db = leer_db()
        
    if db['fisica']['caudal']['id'].__len__() == 0:
        db['fisica']['caudal']['id'].append(0)
        db['fisica']['caudal']['volumen'].append(volumen)
        db['fisica']['caudal']['tiempo'].append(tiempo)
        db['fisica']['caudal']['caudal'].append(res)
        db['fisica']['caudal']['fecha_experimento'].append(fecha)
        db['fisica']['caudal']['fecha_registro'].append(str(datetime.now().date()))
    else:
        db['fisica']['caudal']['id'].append(db['fisica']['caudal']['id'][-1] + 1)
        db['fisica']['caudal']['volumen'].append(volumen)
        db['fisica']['caudal']['tiempo'].append(tiempo)
        db['fisica']['caudal']['caudal'].append(res)
        db['fisica']['caudal']['fecha_experimento'].append(fecha)
        db['fisica']['caudal']['fecha_registro'].append(str(datetime.now().date()))
    
    guardar_registo_db(db)
    
    print()
    
    return f'El caudal del experimento es {res} L/s.\nExperimento registrado con exito!'

def leer_fisica_exp_idx(categoria:str, experimento:str, idx:int):
    db = leer_db()
    df = pd.DataFrame(db[categoria][experimento])
    df.set_index("id", inplace=True)
    print(f"\t*{categoria.title()}*")
    print(f"\t*{experimento.title()}*")
    print(df.loc[idx])