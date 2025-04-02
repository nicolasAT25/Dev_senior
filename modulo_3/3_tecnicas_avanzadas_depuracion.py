'''
Técnicas avanzadas de depuración con IDE VS Code.

Estándar PEP 8
DYR (don't repeat yourself)
KISS (keep it simple stupid)
'''

"""class Empleado:
    
    def __init__(self, nombre:str, ventas:float):
        self.nombre = nombre
        self.ventas = ventas
        
    def calcular_comision(self):
        '''
        Calcula la comisión que recibe el empleado con base en las ventas realizadas.
        '''
        if self.ventas > 5000:
            return self.ventas * 0.10
        
        return self.ventas * 0.05
    
empleados = [
    Empleado("Ana", 6000),
    Empleado("Luis", 3000),
    Empleado("Andrés", 10000),
    Empleado("Pedro", 0),
    Empleado("Pedro", -2000),
]

print(Empleado.calcular_comision)
for empleado in empleados:
    print(f"La comisión del empleado {empleado.nombre} es: {empleado.calcular_comision()}")"""
    
    
class Reserva:
    def __init__(self, cliente, fecha):
        self.cliente = cliente
        self.fecha = fecha if fecha is not None else "Fecha no asignada."
        
reservas = [
    Reserva("Nicolás"),
    Reserva("Lorena", "30-03-2025"),
]

for reserva in reservas:
    if reserva.fecha == "Fecha no asignada.":
        print(f"ERROR. Fecha de reserva no asignada para el cliente {reserva.cliente}")
    else:
        print(f"Reserva a nombre del cliente {reserva.cliente} para la fecha {reserva.fecha}")