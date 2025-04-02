class Autor:
    def __init__(self, nombre:str):
        self.nombre = nombre

    def __str__(self):      # Se cambia el comportamiento de el print con una instancia de Autor. 
        return self.nombre  # Ya no muestra la ubicación en memoria, muestra el atributo nombre.

class Libro:
    def __init__(self, titulo:str, autor:Autor):
        self.titulo = titulo
        self.autor = autor  # El libro "tiene un" autor

    def mostrar_info(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}")

# Crear un autor
autor = Autor("Gabriel García Márquez")

# Crear un libro con un autor
libro = Libro("Cien años de soledad", autor)

# Mostrar la información del libro
libro.mostrar_info()  # "Libro: Cien años de soledad, Autor: Gabriel García Márquez"

print(autor)
