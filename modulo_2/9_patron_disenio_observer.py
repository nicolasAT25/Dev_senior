# Clase Clima (Sujeto)
class Clima:
    def __init__(self):
        self.observadores = []  # Lista de observadores
        self.temperatura = None
        
    def agregar_observador(self, observador):
        self.observadores.append(observador)
        
    def eliminar_observador(self, observador):
        self.observadores.remove(observador)
        
    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar(self.temperatura)
            
    def cambiar_temperatura(self, nueva_temperatura):
        self.temperatura = nueva_temperatura
        self.notificar_observadores()
        
# Definimos la clase Observador (Ciudad)
class Ciudad:
    def __init__(self, nombre):
        self.nombre = nombre
        
    def actualizar(self, temperatura):
        print(f"La ciudad {self.nombre} ha recibido la actualización de temperatura: {temperatura}°C")
        
# Uso del patrón Observador (Sujeto)
clima = Clima()

# Creamos observadores
ciudad1 = Ciudad("Madrid")
ciudad2 = Ciudad("Barcelona")

# Registramos las ciudades como observadores
clima.agregar_observador(ciudad1)
clima.agregar_observador(ciudad2)

# Cambiamos la temperatura, y las ciudades son notificadas
clima.cambiar_temperatura(22)

# Cambiamos nuevamente la temperatura, las ciudades también se actualizan
clima.cambiar_temperatura(28)