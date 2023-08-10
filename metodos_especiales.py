class Persona:
    def __init__(self,nombre,edad) -> None:
        self.nombre = nombre
        self.edad = edad
        
    def __str__(self) -> str:
        return f'Persona(nombre={self.nombre} edad={self.edad})'
    
    
    
goku = Persona('Goku','34')
print(goku)