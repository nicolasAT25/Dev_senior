class Vehiculo:
    def __init__(self, marca:str):
        self.marca = marca
        
    def mostrar_info(self):
        print(f"Vehículo de la marca {self.marca}")
        
class Coche(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)
    
    def mostrar_info(self):
        print(f"Coche de la marca {self.marca}")
        
class Moto(Vehiculo):
    def __init__(self, marca):
        super().__init__(marca)
        
    def mostrar_info(self):
        print(f"Moto de la marca {self.marca}")
        
vehiculos = [Coche("Ferrari"), Moto("Yamaha")]

for vehiculo in vehiculos:
    vehiculo.mostrar_info()     # Se ve como el mismo método se comporta diferente.
    
super(Coche, Coche("Audi")).mostrar_info()  # Invocando el método de la clase padre.