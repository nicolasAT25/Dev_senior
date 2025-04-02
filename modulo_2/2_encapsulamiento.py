# Proteger algunos de los atributos de la clase.

import os

class Perro:
    # Método constructor
    def __init__(self, nombre:str):
        self.__nombre = nombre  # Son 2 underscore para hacerlos de tipo private.
        
    def get(self):              # Para obtener atributos private se debe hacer desde un método.
        return self.__nombre
        
    def set(self, nuevo_nombre:str):    # Para cambiar atributos private se debe hacer desde un método.
        self.__nombre = nuevo_nombre
        return self.__nombre
    
perro_1 = Perro("Max")
perro_2 = Perro(7)

# print(perro_1.get())
# print(perro_1.set("Tanjiro"))
# print(type(perro_1.get()))
# print("----------------------------")
# print(perro_2.get())
# print(type(perro_2.get()))

################################################################################################

class Coche:
    def __init__(self, marca:str, modelo:str, anio:int):
        self.__marca = marca
        self.__modelo = modelo
        self.__anio = anio
        
    ### Getters ###
    def get_marca(self):
        return self.__marca
        
    def get_modelo(self):
        return self.__modelo
        
    def get_anio(self):
        return self.__anio
    
    ### Setters ###
    def set_anio(self, nuevo_anio:int):
        if nuevo_anio > self.__anio:
            anio_anterior = self.__anio
            self.__anio = nuevo_anio
            return f"El año del coche cambió de {anio_anterior} a {nuevo_anio}."
        else:
            print(f"El nuevo año debe ser mayor al año actual. Año actual ({self.__anio}), año ingresado ({nuevo_anio}).")
    
    ### Otros métodos ###    
    def saludar(self):
        print(f"Hola, soy un {self.__marca} {self.__modelo} del año {self.__anio}.")

coche_1 = Coche("Volkswagen", "Polo", 2012)

os.system("clear")

print(coche_1.get_marca())
print(coche_1.get_modelo())
print(coche_1.get_anio())
print("----------------------")
coche_1.saludar()
# coche_1.set_anio(2010)
print(coche_1.set_anio(2018))   # Se añade el print cuando hay un return. En este caso es un str.
coche_1.saludar()