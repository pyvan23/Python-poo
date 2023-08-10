#Clases abstractas (contratos que hacen que se deba implementar como dice la clase abstracta como si fueran interfaces en typeScript)
from abc import ABC, abstractmethod
class Persona(ABC):
    @abstractmethod
    def __init__(self, nombre, edad, sexo, actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractmethod
    def hacer_actividades(self):    
        pass
        
    def presentarse(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} de edad')
        
        
class Estudiante(Persona):
    
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
       
    def hacer_actividades(self):
        print(f'Estoy estudiando... {self.actividad}')
        
class Trabajador(Persona):
    
    def __init__(self, nombre, edad, sexo, actividad):
        super().__init__(nombre, edad, sexo, actividad)
       
    def hacer_actividades(self):
        print(f'Estoy Trabajando en ... {self.actividad}')

robert = Estudiante('Robert', 25, 'Masculino', 'Medicina')
pyvan = Trabajador('Ivan', 35, 'Masculino', 'Desarrollador')

robert.presentarse()
robert.hacer_actividades()
pyvan.presentarse()
pyvan.hacer_actividades()
