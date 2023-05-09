class Person:
    def __init__(self) -> None:
         self._name = name 
         self._edad = edad
         self._telefono = telefono

# El decorador @Property le indica a Python que el metodo debe ser tratado como un atributo solo lectura
# De esta manera es la similitud a un Getter
@property
def name(self):

    return self._name

@property
def edad(self):

    return self._edad

@property
def telefono(self):

    return self._telefono


# Ahora para hacer una similitud a un Setter se implementa un decorador con el mismo nombre que el metodo de lectura

@name.setter
def name(self):

    return self._name

@edad.setter
def edad(self):

    return self._edad

@telefono.setter
def telefono(self):

    return self._telefono
