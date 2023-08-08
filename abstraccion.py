from abc import ABC, abstractclassmethod

class Persona(ABC):
    @abstractclassmethod
    def __init__(self,nombre,edad,sexo,actividad):
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.actividad = actividad
        
    @abstractclassmethod
    def trabajar(self):    
            pass
        
    def presentarse(self):
        print(f'Hola me llamo {self.nombre} y tengo {self.edad} de edad')
        
        
class Estudiante(Persona):
   def __init__(self,nombre,edad,sexo,actividad):
       super().__init__(self,nombre,edad,sexo,actividad)