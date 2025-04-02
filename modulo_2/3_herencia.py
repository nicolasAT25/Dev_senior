# class Animal:
#     def __init__(self, nombre:str, edad:int):
#         self.nombre = nombre
#         self.edad = edad

#     def hablar(self):
#         print("El animal hace un sonido.")

# class Perro(Animal):
#     def __init__(self, nombre:str, edad:int, raza:str):
#         super().__init__(nombre, edad)
#         self.raza = raza

#     def hablar(self):
#         print(f"{self.nombre} dice guau!!!")

# mi_perro = Perro("Rex", 5, "labrador")
# mi_perro.hablar()

class Animal:
    def __init__(self, nombre:str, edad:int):
        self.nombre = nombre
        self.edad = edad
        
    def hablar(self):
        print("El animal hace un sonido.")
        
    def informacion(self):
        print(f"El animal se llama {self.nombre} y tiene {self.edad} años de edad")
        
class Gato(Animal):
    def __init__(self, nombre:str, edad:int, raza:str):
        super().__init__(nombre, edad)
        self.raza = raza

    def hablar(self):
        print(f"{self.nombre} maúlla.")

    def ronronear(self):
        print(f"{self.nombre} está ronroneando.")
            
    def informacion(self):
        print(f"El animal se llama {self.nombre}, tiene {self.edad} años de edad y es de raza {self.raza}") # Se utilizan los atributos de la clase padre.
        
gato = Gato("Zoe", 9, "Siames")

gato.informacion()
gato.hablar()
gato.ronronear()
super(Gato, gato).hablar()  # Primera forma de llamar el método de la clase padre.
Animal.hablar(gato) # Segunda forma de llamar el método de la clase padre.