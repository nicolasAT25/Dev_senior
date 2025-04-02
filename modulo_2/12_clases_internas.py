class Vehiculo:
    def __init__(self, marca, modelo, año, color, tipo):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.tipo = tipo
        
    def mostrar_informacion(self):
        print(f"Vehículo: {self.marca} {self.modelo}, Año: {self.año}, Color: {self.color}, Tipo: {self.tipo}")
    
    # Clase interna Motor
    class Motor:
        def __init__(self, tipo, potencia, cilindrada, combustible):
            self.tipo = tipo
            self.potencia = potencia
            self.cilindrada = cilindrada
            self.combustible = combustible
            
        def mostrar_motor(self):
            print(f"Motor: {self.tipo}, Potencia: {self.potencia} HP, Cilindrada: {self.cilindrada}L, Combustible: {self.combustible}")

# Crear una instancia de la clase Vehiculo
mi_vehiculo = Vehiculo("Toyota", "Camry", 2022, "Negro", "Sedán")

# Crear una instancia de la clase Motor desde la clase interna de Vehiculo
mi_motor = mi_vehiculo.Motor("Gasolina", 200, 2.5, "Gasolina")

# Llamar a los métodos
mi_vehiculo.mostrar_informacion()  # Imprime: Vehículo: Toyota Camry, Año: 2022, Color: Negro, Tipo: Sedán
mi_motor.mostrar_motor()  # Imprime: Motor: Gasolina, Potencia: 200 HP, Cilindrada: 2.5L, Combustible: Gasolina