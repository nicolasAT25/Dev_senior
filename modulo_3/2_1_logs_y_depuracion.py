import logging
from dataclasses import dataclass, field

# Handler que guarda la config y va a guardar los eventos en un archivo.
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='eventos.log',
                    filemode='a'    # con 'w' se guarda solo la última ejecución, con 'a' guarda todas.
                    )

# Crear un nuevo manejador y sus características para la consola.
console_handler = logging.StreamHandler()   # Objeto para crear el nuevo handler.
console_handler.setLevel(level=logging.DEBUG
                    )
console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console_handler.setFormatter(console_formatter)

logging.getLogger().addHandler(console_handler)

# Me ahorra crear el constructor de la clase. Solo indico los tipos de los atributos.
@dataclass
class Producto:
    nombre: str
    precio: float
    cantidad: int
    
    def comprar(self, cantidad: int):
        if cantidad > self.cantidad:
            logging.error(f"ERROR: No hay suficiente stock de '{self.nombre}'.\nStock disponible: {self.cantidad}")
            raise ValueError(f"No hay suficiente stock de '{self.nombre}'.\nSolo quedan {self.cantidad} unidades.")
        else:
            self.cantidad -= cantidad
            logging.info(f"Compra exitosa: {cantidad} unidades de '{self.nombre}'\nStock restante {self.cantidad} unidades.")
            return self.precio * cantidad
        
@dataclass
class Tienda:
    productos: list[Producto] = field(default_factory=list)
    
    def agregar_producto(self, producto:Producto):
        self.productos.append(producto)
        logging.debug(f"Producto agregado: {producto.nombre} - Precio: {producto.precio} - Stock: {producto.cantidad}")

    def realizar_compra(self, nombre_producto:str, cantidad:int):
        producto = next((p for p in self.productos if p.nombre == nombre_producto), None) # El None evita un error si no se encuentra el producto
        if producto:
            try:
                total = producto.comprar(cantidad)
            except ValueError as e:
                logging.error(f"Error en la compra: {e}")
            else:
                logging.info(f"Compra realizada: {cantidad} unidades de '{nombre_producto}', por un total de ${total}")
                return total
            
        else:
            logging.warning(f"Producto no registrado en stock '{nombre_producto}'")
            

# Método principal (único) que activa todo el software.
if __name__ == "__main__":  
    tienda = Tienda()
    
    inventario_portatil = Producto(nombre="Laptop", precio=1000, cantidad=5)
    inventario_teclado = Producto(nombre="Teclado mecánico", precio=50, cantidad=20)
    tienda.agregar_producto(inventario_portatil)
    tienda.agregar_producto(inventario_teclado)
    
    # Casos de prueba
    tienda.realizar_compra("Laptop", 1)
    tienda.realizar_compra("Teclado mecánico", 2)
    tienda.realizar_compra("Mouse", 6)
    tienda.realizar_compra(42, "siete")
    tienda.realizar_compra("laptop", 1)
    tienda.realizar_compra("Teclado mecánico", 30)