from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class Vendedor(ABC):
    """_summary_
    
    Implementación de la clase abstracta para definir la clase "Vendedor"

    nombre: str
    ventas: float
    """
    nombre: str
    ventas: float
    
    @abstractmethod
    def calcular_comision(self) -> float:
        pass
    
@dataclass
class VendedorBase(Vendedor):
    """_summary_
    
    Implementación concreta de un vendedor con una comisión por venta del 10%

    Args:
        Vendedor (_type_): _description_
    """
    def calcular_comision(self) -> float:
        return self.ventas * 0.10
    
@dataclass
class VendedorPremium(Vendedor):
    """_summary_
    
    Implementación concreta de un vendedor con una comisión por venta del 15%

    Args:
        Vendedor (_type_): _description_
    """
    def calcular_comision(self) -> float:
        return self.ventas * 0.15