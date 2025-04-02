import os
import platform
from datetime import datetime
import json
import pandas as pd

### Funciones básicas de flujo ###
def limpiar_pantalla():
    op_sys = platform.system()
    if op_sys == 'Darwin':
        os.system('clear')
    else:
        os.system('cls')

def mostrar_menu():
    print()
    print("\t\t🔬 Experimentos App 🔬")
    print()

    print("MENÚ\n")
    print("\
    1. Registrar un experimento 🧪\n\
    2. Registrar varios experimentos 🔬\n\
    3. Consultar todos los experimentos 🔎\n\
    4. Consultar todos los experimentos de una categoría 🔎🧪\n\
    5. Consultar un solo experimento por ID de una categoría 🔎🧪🆔\n\
    6. Editar un experimento por ID 📝🧪🆔\n\
    7. Eliminar un experimento por ID ❌🆔\n\
    8. Generar informe de los experimentos de una categría ℹ️🧪\n\
    9.  Salir 🚪")
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
    b. Ley de Ohm.\n\
    c. Caída libre.")
    print()
    
def mostrar_experimentos_quimica():
    print("Experimentos de Química\n")
    print("\
    a. Cálculo del caudal.\n\
    b. Ley de Ohm (Voltaje).\n\
    c. Caída libre.")
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

### Funciones para la "Base de Datos" ###
def leer_db():
    with open('db_experimentos.json', 'r') as f:
        db = json.load(f)
    return db

def guardar_registo_db(db):
    with open('db_experimentos.json', 'w') as f:
            json.dump(db, f)

### Funciones transversales experimentos ###
def leer_experimentos_categorias(categoria:str):        # Muestra los experimentos de todas las categorías
    db = leer_db()
    for i in db[categoria].keys():
        print(f"\t\t\t*{i.title()}*")
        df = pd.DataFrame(db[categoria][i])
        df.set_index("id", inplace=True)
        print(df)
        print()
        
def leer_lista_experimentos_categoria(categoria:str, experimento:str):  # Experimentos de UNA SOLA categoría
    db = leer_db()
    df = pd.DataFrame(db[categoria][experimento])
    df.set_index("id", inplace=True)
    print(df)
        
def mostrar_ids_disponibles(categoria:str, experimento:str):
    db = leer_db()
    print(f"IDs disponibles: {', '.join([str(item) for item in db[categoria][experimento]["id"]])}")


######### CRUD experimentos FÍSICA #########
    
### Caudal ###
def crear_fisica_caudal(volumen:float, tiempo:float, fecha:str):
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

def leer_experimentos():
    db = leer_db()
    
    keys = list(db.keys())
    values = [list(i.keys()) for i in list(db.values())]

    for v in values[0]:
        print(f"\t\tCategoría {keys[0].title()} - Experimento {" ".join(v.split("_")).title()}")
        print(pd.DataFrame(db[keys[0]][v]).set_index("id"))
        print()

    for v in values[1]:
        print(f"\t\tCategoría {keys[1].title()} - Experimento {" ".join(v.split("_")).title()}")
        print(pd.DataFrame(db[keys[1]][v]).set_index("id"))
        print()

    for v in values[2]:
        print(f"\t\tCategoría {keys[2].title()} - Experimento {" ".join(v.split("_")).title()}")
        print(pd.DataFrame(db[keys[2]][v]).set_index("id"))
        print()

def leer_fisica_caudal_exp_idx(categoria:str, experimento:str, idx:int):
    db = leer_db()
    df = pd.DataFrame(db[categoria][experimento])
    df.set_index("id", inplace=True)
    print(f"\t*{categoria.title()}*")
    print(f"\t*{experimento.title()}*")
    print(df.loc[idx])

def actualizar_fisica_caudal_exp_idx(categoria:str, experimento:str, idx:int, nuevo_volumen:float, nuevo_tiempo:float, nueva_fecha:str):
    # leer_lista_experimentos_categoria(categoria, experimento)

    print(f'Volumen: {nuevo_volumen}\nTiempo: {nuevo_tiempo}') 
    nueva_res = round(nuevo_volumen / nuevo_tiempo, 2)

    db = leer_db()

    posicion = db[categoria][experimento]['id'].index(idx)

    db[categoria][experimento]['volumen'][posicion] = nuevo_volumen
    db[categoria][experimento]['tiempo'][posicion] = nuevo_tiempo
    db[categoria][experimento]['caudal'][posicion] = nueva_res
    db[categoria][experimento]['fecha_experimento'][posicion] = nueva_fecha
    db[categoria][experimento]['fecha_registro'][posicion] = str(datetime.now().date()) # Se sobreescribe la fecha de registro.

    guardar_registo_db(db)
    
    print()
    
    return f'El nuevo caudal del experimento es {nueva_res} L/s.\nExperimento modificado con exito!'

def eliminar_exp_id(categoria:str, experimento:str, idx:int):

    db = leer_db()

    posicion = db[categoria][experimento]['id'].index(idx)

    db[categoria][experimento]['id'].pop(posicion)
    db[categoria][experimento]['volumen'].pop(posicion)
    db[categoria][experimento]['tiempo'].pop(posicion)
    db[categoria][experimento]['caudal'].pop(posicion)
    db[categoria][experimento]['fecha_experimento'].pop(posicion)
    db[categoria][experimento]['fecha_registro'].pop(posicion)

    guardar_registo_db(db)
    
    print()
    
    return f'El experimento "{experimento}" con ID {idx} de la categoría "{categoria}" se a eliminado con éxito.'

### Voltaje ###
def crear_fisica_voltaje(corriente:float, resistencia:float, fecha:str):
    # Cálculo
    print(f'Corriente: {corriente}\nResistencia: {resistencia}')    
    res = round(corriente * resistencia, 2)
    
    db = leer_db()
        
    if db['fisica']['voltaje']['id'].__len__() == 0:
        db['fisica']['voltaje']['id'].append(0)
        db['fisica']['voltaje']['corriente'].append(corriente)
        db['fisica']['voltaje']['resistencia'].append(resistencia)
        db['fisica']['voltaje']['voltaje'].append(res)
        db['fisica']['voltaje']['fecha_experimento'].append(fecha)
        db['fisica']['voltaje']['fecha_registro'].append(str(datetime.now().date()))
    else:
        db['fisica']['voltaje']['id'].append(db['fisica']['voltaje']['id'][-1] + 1)
        db['fisica']['voltaje']['corriente'].append(corriente)
        db['fisica']['voltaje']['resistencia'].append(resistencia)
        db['fisica']['voltaje']['voltaje'].append(res)
        db['fisica']['voltaje']['fecha_experimento'].append(fecha)
        db['fisica']['voltaje']['fecha_registro'].append(str(datetime.now().date()))
    
    guardar_registo_db(db)
    
    print()
    
    return f'El voltaje del experimento es {res} V.\nExperimento registrado con exito!'

def leer_fisica_voltaje_exp_idx(categoria:str, experimento:str, idx:int):
    db = leer_db()
    df = pd.DataFrame(db[categoria][experimento])
    df.set_index("id", inplace=True)
    print(f"\t*{categoria.title()}*")
    print(f"\t*{experimento.title()}*")
    print(df.loc[idx])
    
def actualizar_voltaje_caudal_exp_idx(categoria:str, experimento:str, idx:int, nueva_corriente:float, nueva_resistencia:float, nueva_fecha:str):
    # leer_lista_experimentos_categoria(categoria, experimento)

    print(f'Corriente: {nueva_corriente}\Resistencia: {nueva_resistencia}') 
    nueva_res = round(nueva_corriente * nueva_resistencia, 2)

    db = leer_db()

    posicion = db[categoria][experimento]['id'].index(idx)

    db[categoria][experimento]['corriente'][posicion] = nueva_corriente
    db[categoria][experimento]['resistencia'][posicion] = nueva_resistencia
    db[categoria][experimento]['voltaje'][posicion] = nueva_res
    db[categoria][experimento]['fecha_experimento'][posicion] = nueva_fecha
    db[categoria][experimento]['fecha_registro'][posicion] = str(datetime.now().date()) # Se sobreescribe la fecha de registro.

    guardar_registo_db(db)
    
    print()
    
    return f'El nuevo voltaje del experimento es {nueva_res} V.\nExperimento modificado con exito!'