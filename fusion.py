class Personaje:
    
    def __init__(self,nombre,poder):
        self.nombre = nombre
        self.poder = poder
        
    def __repr__(self) -> str:
        return f'{self.nombre} poder:{self.poder}'
    
    def __add__(self,personaje):
        self.personaje = personaje
        
        return 
    
    
    
goku = Personaje('Goku',10000)
print(goku)