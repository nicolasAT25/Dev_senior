# Librerías
from datetime import datetime
import json

# Funciones básicas
from utils import limpiar_pantalla, mostrar_menu, mostrar_categorias

#Funciones de validación
from utils import validar_num_positivo, validar_fecha

# Funciones Física
from utils import mostrar_experimentos_fisica, crear_fisica_caudal

mostrar_menu()

sel = int(input("Selecciona la opción que deseas ejecutar: "))
limpiar_pantalla()

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