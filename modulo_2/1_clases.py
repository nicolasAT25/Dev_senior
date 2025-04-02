class Persona:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
        
    def presentarse(self):
        print(f"Hola, mi nombres es {self.nombre} y tengo {self.edad} años.")
        
persona_1 = Persona("Nicolás Aranguren", 32)
persona_1.presentarse()

class Libro:
    def __init__(self, libro:str, autor:str, paginas:int):
        self.libro = libro
        self.autor = autor
        self.paginas = paginas
        
    def detalle_libro(self):
        print(f"El libro {self.libro} fue escrito por el autor {self.autor} y tiene {self.paginas} páginas.")
        
libro_1 = Libro("Cien años de solidad", "Gabriel García Márquez", 130)
libro_1.detalle_libro()