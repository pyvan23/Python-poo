#herencia simple
class Persona:
    def __init__(self,nombre ,edad):
        self.nombre = nombre
        self.edad = edad
        
    def imprimirPersona(self):
        print(f'Soy {self.nombre} y tengo {self.edad} de edad.')
        
        
class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre,edad)
        self.grado = grado
    def inprimirGrado(self):
        return f'Es el alumno {self.nombre} con {self.edad} de edad y es del grado {self.grado} '
    
    
    
    
estudiante = Estudiante('Pyvan',23,3)
print(estudiante.inprimirGrado())

