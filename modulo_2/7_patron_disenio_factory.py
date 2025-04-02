from abc import ABC, abstractmethod

# # Interfaz común para los vehículos
# class Vehiculo(ABC):
#     @abstractmethod
#     def moverse(self):
#         pass

# class Coche(Vehiculo):
#     def moverse(self):
#         return "El coche está conduciendo"

# class Bicicleta(Vehiculo):
#     def moverse(self):
#         return "La bicicleta está pedaleando"

# class VehiculoFactory:
#     def crear_vehiculo(self, tipo: str) -> Vehiculo:
#         if tipo == "coche":
#             return Coche()
#         elif tipo == "bicicleta":
#             return Bicicleta()
#         else:
#             raise ValueError(f"Tipo de vehículo {tipo} no reconocido.")

# # Creamos una fábrica de vehículos
# fabrica = VehiculoFactory()

# # Usamos la fábrica para crear un coche
# vehiculo1 = fabrica.crear_vehiculo("coche")
# print(vehiculo1.moverse())  # "El coche está conduciendo"

# # Usamos la fábrica para crear una bicicleta
# vehiculo2 = fabrica.crear_vehiculo("bicicleta")
# print(vehiculo2.moverse())  # "La bicicleta está pedaleando"


print("------------------------------------------")

# Clase base/padre para los productos
class Producto(ABC):
    @abstractmethod
    def mostrar_info(self):
        pass

# Clases hijas
class Smartphone(Producto):
    def mostrar_info(self):
        return "Este es un Smartphone."

class Tablet(Producto):
    def mostrar_info(self):
        return "Este es una Tablet."

class Laptop(Producto):
    def mostrar_info(self):
        return "Este es una Laptop."

# Fábrica
class ProductoFactory:
    @staticmethod
    def crear_producto(tipo):
        if tipo == "smartphone":
            return Smartphone()
        elif tipo == "tablet":
            return Tablet()
        elif tipo == "laptop":
            return Laptop()
        else:
            raise ValueError("Tipo de producto no reconocido")
        
def cliente():
    tipo_producto = input("¿Qué producto deseas? (smartphone/tablet/laptop): ").lower()
    
    producto = ProductoFactory.crear_producto(tipo_producto)
    
    print(producto.mostrar_info())

# Ejecutamos la función cliente
cliente()



# Prompt: Me puedes explicar el patrón de diseño Factory en el desarrollo de software con python?
