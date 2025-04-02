"""
Necesitamos 2 clases
- Persona: nombre y cedula
- Cliente: numero de cuenta, balance y clave
Un metodo __str__, depositar, retirar, historial de ambos.

Codigo para elegir deposito, retiro o salir.
"""

from os import system
from abc import ABC, abstractmethod
from datetime import datetime

class Persona(ABC):
    def __init__(self, nombre_apellido, cedula):
        self.nombre = nombre_apellido
        self.cedula = cedula
        
    @abstractmethod
    def __str__(self):
        pass
     
"""
Contrato que cualquier objeto que la implemente debe tener el metodo actualizar
"""   
class Observador(ABC):
    
    @abstractmethod
    def __init__(self):
        pass
    
    @abstractmethod
    def actualizar(self, mensaje):
        raise NotImplementedError ("Las subclases deben de implementar este metodo")
    
# De momento notificador es la unica que implementa el contrato. Pero se puede agregar más
class Notificador(Observador): #ConcreteObserver o ObservadorConcreto
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []
    
    def actualizar(self, mensaje):
        print(mensaje)

class Cliente(Persona):
    
    def __init__(self, nombre_apellido, cedula, numero_cuenta, balance, clave):
        super().__init__(nombre_apellido, cedula)
        self.cuenta = numero_cuenta
        self.balance = balance
        self.clave = clave
        self.observadores = []
        self.historial_depositos = []
        self.historial_retiros = []
        
    def __str__(self):
        limpiar()
        return f'\nNombre: {self.nombre}\nCedula: {self.cedula}\nNumero de Cuenta: {self.cuenta}\nBalance: ${self.balance}\n'
    
    def agregar_observador(self, observador):
        self.observadores.append(observador)
        
    def eliminar_observador(self, observador):
        self.observadores.remove(observador)
        
    def notificar_observadores(self, mensaje):
        for observador in self.observadores:
            observador.actualizar(mensaje)
        #print(mensaje)
    
    def depositar(self):
        limpiar()
        monto_depositar = int(input('¿Cuánto dinero desea depositar?: '))
        if monto_depositar > 0: 
            self.balance += monto_depositar
            self.notificar_observadores(f'Deposito de ${monto_depositar} realizado con éxito\n') # -> NOTIFICADOR
            self.historial_depositos.append(monto_depositar) 
        else: 
            print('ERROR. Monto máximo por deposito alcanzado\n')
            
    def retirar(self):
        limpiar()
        while True:
            print(f'Dinero actual: {self.balance}\n')
            monto_retirar = int(input('¿Cuánto dinero desea retirar?: '))
            clave = input('Digite su clave: ')
            if not self.validar_clave(clave):
                print('Acceso denegado. Clave incorrecta')
                self.notificar_observadores(f"\nAcceso denegado. Clave incorrecta.")
                break
            elif monto_retirar <= self.balance and monto_retirar > 0: # Ni numero negativo ni mayor al balance
                self.balance -= monto_retirar
                print(f'\nRetiro con exito.\nBalance: ${self.balance}\n') # -> NOTIFICADOR
                self.notificar_observadores(f'Retiro con exito\nDinero actual: ${monto_retirar}\n') # -> NOTIFICADOR
                self.historial_retiros.append(monto_retirar)
                break
            else: 
                print(f'ERROR. Imposible retirar ${monto_retirar} porque no existe ese dinero en la cuenta\n')    
                break
            
    def mostrar_historial(self):
        limpiar()
        
        if len(self.historial_depositos) == 0:
            print('No se han realizado depositos')
        else:
            print('Historial de depositos:')
            for monto in self.historial_depositos:
                print(monto)
            
            
        if len(self.historial_retiros) == 0:
            print('No se han realizado retiros')
        else:
            print('Historial de retiros:')
            for monto in self.historial_retiros:
                print(monto)
            
    def validar_clave(self, clave):
    
        if clave == self.clave:
            return True
        else:
            return False
    
def limpiar():
    try:
        system('cls')
    except Exception as e:
        print(f"ERROR. No fue posible limpiar pantalla cajero ({e})")
    else:
        system("clear")
            
def crear_cliente():
    nombre = input('Ingrese su nombre y apellido: ')
    cedula = int(input('Ingrese su cedula: '))
    numero_cuenta = int(input('Ingrese su numero de cuenta: '))
    balance = float(input('Ingrese su balance: '))
    
    while True:
        clave = input('Ingrese una clave de 4 digitos para el cajero: ')
        longitud_clave = len(clave)
        if longitud_clave == 4 and clave.isnumeric():
            break
        else:
            print('\nERROR. La clave debe ser de 4 digitos.\n')
            continue
    return Cliente(nombre, cedula, numero_cuenta, balance, clave)            

def cajero(cliente):
    
    notificador = Notificador("Notificador 1")
    cliente.agregar_observador(notificador)
    
    while True:
        
        print('\nCajero DevSenior\n')
        print("1. Depositar")
        print("2. Retirar")
        print("3. Estado de cuenta")
        print("4. Historial de transacciones")
        print("5. Salir")
        
        opcion = int(input("\n¿Cuál tramite desea realizar?: "))
        
        if opcion > 0 and opcion < 6:
            if opcion == 1:
                cliente.depositar()
            elif opcion == 2:
                cliente.retirar()
            elif opcion == 3:
                print(cliente)
            elif opcion == 4:
                cliente.mostrar_historial()
            elif opcion == 5:
                print('\nHasta luego. Gracias por usar nuestros servicios :)')
                break
        else:
            print('ERROR. Digite una opción valida.\n')
    
cliente1 = crear_cliente()
cajero(cliente1)