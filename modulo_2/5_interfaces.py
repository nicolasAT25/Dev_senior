"""
Clase que define métodos que **DEBEN** ser implementados  por las clases hijas,
sin proporcionar una implementación concreta de esos métodos. La librería ABC 
permite crear clases abstractas y permite usar la librería abstractmethod.
"""

from abc import ABC, abstractmethod

# Interfaz
class Vehiculo(ABC):    
    
    @abstractmethod
    def mover(self):
        pass
    
class Carro(Vehiculo):
    def mover(self):
        print("El carro se está conduciendo por carretera.")
    # def cambiar(self):
    #     print("El carro se está conduciendo por carretera.")  Genera error si solo implementamos este método y no el de mover.
        
class Bicicleta(Vehiculo):
    def mover(self):
        print("La bicicleta tiene dos ruedas.")
        
vehiculos = [Carro(), Bicicleta()]

for v in vehiculos:
    v.mover()