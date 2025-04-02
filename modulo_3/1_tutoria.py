'''def validar_numero():
    while True:
        try:
            numero = float(input("Ingrese un número: "))
        except ValueError as e:
            print(f"El valor ingresado no es un número entero. ERROR: {e}\n")
            print("Intente de de nuevo....")
        else:
            print(f"El número ingresado es {numero}")
            break
        finally:
            print("\n👋🏼 Saliendo del sistema!")

validar_numero()'''

'''
datos = {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"}

def mostrar_values():
    while True:
        try:
            key = input("Ingrese la 'llave' para consultar su valor: ")
            value = datos[key]  # Parece que en el try hay que tener el "valor" que se va a evaluar en except y a utilizar en el resto
        except KeyError as e:
            print(f"\nLa 'llave' no existe...\nLas llaves disponibles son: {', '.join(datos.keys())}\nERROR:{e}")
        else:
            print(f"El valor de la llave '{key}' es: {value}")
            break
        finally:
            print("\n👋🏼 Saliendo del sistema!\n")

mostrar_values()
'''


dbz = ["Goku", "Vegeta", "Gohan"]

def consultar_idx():
    while True:
        try:
            idx = int(input("Ingrese el índice a consultar de la lista: "))
            value = dbz[idx]
        except IndexError as e:
            print(f"\nEl índice se encuentra fuera del rango de la lista\nEl rango de la lista es: 0-{len(dbz)-1}\nERROR:{e}")
        except ValueError as e:
            print(f"\nEl índice no corresponde a un entero.\nIntente de nuevo...")
        else:
            print(f"El valor del índice '{idx}' es: {value}")
            break
        finally:
            print("\n👋🏼 Saliendo del sistema!\n")
            
consultar_idx()
