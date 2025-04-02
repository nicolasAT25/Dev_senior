# Librerías
from datetime import datetime
import json

# Funciones básicas
from utils import limpiar_pantalla, mostrar_menu, mostrar_categorias

# Funciones de validación
from utils import validar_num_positivo, validar_fecha

# Funciones generales
from utils import leer_experimentos_categorias, mostrar_ids_disponibles, eliminar_exp_id, leer_experimentos

# Funciones Física
from utils import mostrar_experimentos_fisica, crear_fisica_caudal, leer_fisica_caudal_exp_idx, actualizar_fisica_caudal_exp_idx, leer_lista_experimentos_categoria
from utils import crear_fisica_voltaje, leer_fisica_voltaje_exp_idx, actualizar_voltaje_caudal_exp_idx

# Funciones Química
from utils import mostrar_experimentos_quimica

# mostrar_menu()

# sel = int(input("Selecciona la opción que deseas ejecutar: "))
# limpiar_pantalla()

while True:
    mostrar_menu()

    sel = int(input("Selecciona la opción que deseas ejecutar: "))
    
    if sel == 1:
        mostrar_categorias()
        categoria = input('Selecciona la categría del experimento a registrar: ')
        limpiar_pantalla()
        
        if categoria == 'Física' or categoria == 'a':
            mostrar_experimentos_fisica()
            exp = input('Selecciona el experimento: ')
            limpiar_pantalla()
            
            if exp == 'a':  # Caudal
                volumen = float(input('Ingresa el volumen en litros: '))
                validar_num_positivo(volumen)
                limpiar_pantalla()
                
                tiempo = float(input('Ingresa el tiempo en segundos: '))
                validar_num_positivo(tiempo)
                limpiar_pantalla()
                
                fecha = input("Ingresa la fecha en que se realizó el experimento (YYYY-mm-dd): ")
                fecha = validar_fecha(fecha)
                
                print(crear_fisica_caudal(volumen=volumen, tiempo=tiempo, fecha=fecha))
                
            elif exp == 'b':    # Ley de Ohm (volataje)
                corriente = float(input('Ingresa la corriente eléctrica en amperios: '))
                validar_num_positivo(corriente)
                limpiar_pantalla()
                
                resistencia = float(input('Ingresa la resistencia en ohmios: '))
                validar_num_positivo(resistencia)
                limpiar_pantalla()
                
                fecha = input("Ingresa la fecha en que se realizó el experimento (YYYY-mm-dd): ")
                fecha = validar_fecha(fecha)
                
                print(crear_fisica_voltaje(corriente=corriente, resistencia=resistencia, fecha=fecha))
                
        elif categoria == 'Química' or categoria == 'b':
            mostrar_experimentos_quimica()
            exp = input('Selecciona el experimento: ')
            limpiar_pantalla()

    elif sel == 2:
        num_experimentos = int(input("Ingresa el número de experimentos a registrar: "))
        limpiar_pantalla()
        
        mostrar_categorias()
        categoria = input('Selecciona la categría del experimento a registrar: ')
        limpiar_pantalla()
        if categoria == 'Física' or categoria == 'a':
            mostrar_experimentos_fisica()
            exp = input('Selecciona el experimento: ')
            limpiar_pantalla()
            
            if exp == 'a':  # Caudal
                for i in range(num_experimentos):
                    print(f"Experimento {i+1} de {num_experimentos}.")
                    print()
                    volumen = float(input('Ingresa el volumen en litros: '))
                    validar_num_positivo(volumen)
                    limpiar_pantalla()
                    
                    print()
                    tiempo = float(input('Ingresa el tiempo en segundos: '))
                    validar_num_positivo(tiempo)
                    limpiar_pantalla()
                    
                    fecha = input("Ingresa la fecha en que se realizó el experimento (YYYY-mm-dd): ")
                    fecha = validar_fecha(fecha)
                    
                    print(crear_fisica_caudal(volumen=volumen, tiempo=tiempo, fecha=fecha))
                    print()

    elif sel == 3:
        limpiar_pantalla()
        print()
        leer_experimentos()

    elif sel == 4:
        mostrar_categorias()
        categoria_temp = input('Selecciona la categría de la cual quieres consutar los experimentos: ')
        limpiar_pantalla()
        
        if categoria_temp == "a" or categoria_temp == "Física".lower():
            categoria = "fisica"
            leer_experimentos_categorias(categoria)
                
    elif sel == 5:
        mostrar_categorias()
        categoria_temp = input('Selecciona la categría de la cual quieres consutar un experimento por ID: ')
        limpiar_pantalla()
        
        if categoria_temp == "a" or categoria_temp == "Física".lower():
            categoria = "fisica"
            mostrar_experimentos_fisica()
        experimento_temp = input("Selecciona el experimento del cual quieres consultar por ID: ")
        limpiar_pantalla()
        
        if experimento_temp == "a" or experimento_temp == "Cálculo del caudal".lower():
            experimento = "caudal"
            mostrar_ids_disponibles(categoria, experimento)    
            idx = int(input('Ingresa al ID: '))
            limpiar_pantalla()
            leer_fisica_caudal_exp_idx(categoria, experimento, idx)
            
        if experimento_temp == "b" or experimento_temp == "Ley de Ohm".lower():
            experimento = "voltaje"
            mostrar_ids_disponibles(categoria, experimento)    
            idx = int(input('Ingresa al ID: '))
            limpiar_pantalla()
            leer_fisica_voltaje_exp_idx(categoria, experimento, idx)
                
    elif sel == 6:
        mostrar_categorias()
        categoria_temp = input('Selecciona la categría del experimento que deseas modificar por ID: ')
        limpiar_pantalla()
        
        if categoria_temp == "a" or categoria_temp == "Física".lower():
            categoria = "fisica"
            mostrar_experimentos_fisica()
        experimento_temp = input("Selecciona el experimento del cual quieres consultar por ID: ")
        limpiar_pantalla()
        
        if experimento_temp == "a" or experimento_temp == "Cálculo del caudal".lower():
            experimento = "caudal"
            leer_lista_experimentos_categoria(categoria, experimento) 

            idx = int(input('Ingresa al ID: '))
            limpiar_pantalla()

            nuevo_volumen = float(input('Ingresa el nuevo volumen en litros: '))
            validar_num_positivo(nuevo_volumen)
            limpiar_pantalla()

            nuevo_tiempo = float(input('Ingresa el nuevo tiempo en segundos: '))
            validar_num_positivo(nuevo_volumen)
            limpiar_pantalla()

            nueva_fecha = input("Ingresa la nueva fecha en que se realizó el experimento (YYYY-mm-dd): ")
            nueva_fecha = validar_fecha(nueva_fecha)

            limpiar_pantalla()
            print(actualizar_fisica_caudal_exp_idx(categoria, experimento, idx, nuevo_volumen, nuevo_tiempo, nueva_fecha))
        
        elif experimento_temp == "b" or experimento_temp == "Ley de Ohm".lower():
            experimento = "voltaje"
            leer_lista_experimentos_categoria(categoria, experimento) 

            idx = int(input('Ingresa al ID: '))
            limpiar_pantalla()

            nueva_corriente = float(input('Ingresa la nueva corriente en amperios: '))
            validar_num_positivo(nueva_corriente)
            limpiar_pantalla()

            nueva_resistencia = float(input('Ingresa la nueva resistencia en ohmios: '))
            validar_num_positivo(nueva_resistencia)
            limpiar_pantalla()

            nueva_fecha = input("Ingresa la nueva fecha en que se realizó el experimento (YYYY-mm-dd): ")
            nueva_fecha = validar_fecha(nueva_fecha)

            limpiar_pantalla()
            print(actualizar_voltaje_caudal_exp_idx(categoria, experimento, idx, nueva_corriente, nueva_resistencia, nueva_fecha))

    elif sel == 7:
        mostrar_categorias()
        categoria_temp = input('Selecciona la categría del experimento que deseas eliminar por ID: ')
        limpiar_pantalla()
        
        if categoria_temp == "a" or categoria_temp == "Física".lower():
            categoria = "fisica"
            mostrar_experimentos_fisica()
        experimento_temp = input("Selecciona el experimento del cual quieres eliminar por ID: ")
        limpiar_pantalla()
        
        if experimento_temp == "a" or experimento_temp == "Cálculo del caudal".lower():
            experimento = "caudal"
            leer_lista_experimentos_categoria(categoria, experimento) 
            print()

            idx = int(input('Ingresa el ID del experimento que deseas eliminar: '))
            limpiar_pantalla()
            
            print(eliminar_exp_id(categoria, experimento, idx))
    
    elif sel == 9:
        print("\n👋 Saliendo de 🔬 Experimentos App 🔬...")
        print()
        break
    
    else:
        print("\n❌ ¡Opción inválida! Elija una opción del 1 al 10.")