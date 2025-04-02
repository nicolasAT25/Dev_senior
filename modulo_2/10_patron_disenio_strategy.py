"""
Permite cambiar el comportamiento en tiempo de ejecución.
"""

from abc import ABC, abstractmethod

# 1. Estrategia abstracta
class MetodoPago(ABC):
    
    @abstractmethod
    def pagar(self):
        pass
    
# 2. Estrategias concretas
class PagoTarjeta(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con tarjeta de crédito.")

class PagoPaypal(MetodoPago):
    def pagar(self, monto):
        print(f"Pagando ${monto} con Paypal.")

# 3. Contexto
class Pedido:
    def __init__(self, monto, metodo_pago:MetodoPago):
        self.monto = monto
        self.metodo_pago = metodo_pago
        
    def realizar_pago(self):
        self.metodo_pago.pagar(self.monto)
        
    def cambiar_metodo_pago(self, nuevo_metodo_pago:MetodoPago):
        self.metodo_pago = nuevo_metodo_pago
        print("Método de pago cambiado.")
        
# Uso del patrón de diseño Strategy con cambio dinámico de estrategia.

# Crear métodos de pago
pago_con_tarjeta = PagoTarjeta()
pago_con_paypal = PagoPaypal()

# Crear pedido con un método de pago inicial
pedido = Pedido(100, pago_con_tarjeta)

# Realizar el pago con el primer método de pago
pedido.realizar_pago()

# Cambiar el método de pago en tiempo de ejecución
pedido.cambiar_metodo_pago(pago_con_paypal)

# Realizar el pago con el NUEVO método de pago
pedido.realizar_pago()