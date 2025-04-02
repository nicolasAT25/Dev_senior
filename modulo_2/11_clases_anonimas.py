# Estructura

"""
Clase = type('Clase', 'clase base', {
    atributos: ... ,
    funciones: ...
})
"""

# def saludar(self):
#     print(f"Hola, mi nombre es {self.nombre}!")
    
# # type para crear una clase anónima
# Persona = type('Persona', (object,), {
#     'nombre': 'Juan',   # Atributos
#     'saludar': saludar  # Funciones / se habla de funciones con clases anónimas
# })

# # Instancia de la clase anónima
# objeto_persona = Persona()

# # Invocación de la clase anónima
# objeto_persona.saludar()

# ------------------------------------------------------

# def crear_formulario(campos: list):
#     Formulario = type('Formulario', (object,), {
#         'nombre': campos[0],
#         'edad': campos[1],
#         'email':campos[2]
#     })
    
#     return Formulario

# formulario_1 = crear_formulario(['Goku', 25, 'gokukakaroto@vegeta.com'])
# print(formulario_1.nombre)
# print(formulario_1.edad)
# print(formulario_1.email)

def crear_formulario(campos: list):
    atributos = {campo: '' for campo in campos}
    Formulario = type('Formulario', (object,), atributos)
    
    return Formulario

formulario_1 = crear_formulario(['nombre', 'edad', 'email'])
formulario_1.nombre = 'Goku'
formulario_1.edad = 25
formulario_1.email = 'gokukakaroto@vegeta.com'

print(formulario_1.nombre)