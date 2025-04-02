class Singleton:
    # Atributo que almacenará la única instancia
    __instancia = None
    # _instancia = None  Se puede acceder directamente desde una instancia.
    
    def __new__(cls):
        # Si no existe la instancia, la creamos
        if cls.__instancia is None:
            cls.__instancia = super().__new__(cls)
        # Si existe, devolvemos la única instancia
        return cls.__instancia


# Uso del Singleton
obj1 = Singleton()
obj2 = Singleton()

print(obj1 is obj2)  # Output: True, ambas son la misma instancia
print(obj1)     # Mismo espacio en memoria
print(obj2)     # Mismo espacio en memoria

# print(obj1.__instancia)  # Error
# print(obj1._Singleton__instancia)  Deja consultar el atributo. Esto se conoce como mangling (cambiar el name del atributo para dificultar su acceso)
# print(obj1._instancia)  Con un solo _ deja consultar el atributo. Solo es una convención para
                        # sugeririr no acceder a este atributo desde fuera de la clase, sino hacerlo por medio de un método.
                        
# Prompt: Me puedes explicar el patrón de diseño Singleton en el desarrollo de software con python?