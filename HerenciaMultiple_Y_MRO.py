class Animal:
    def __init__(self) :
        pass
    def comer(self):
        return f'comiendo....'
    
class Mamifero(Animal):
    
     def amamantar(self):
        return f'amamantar....'
    
class Ave(Animal):
    
    def volar(self):
       return f'volando...'
        
class Murcielago(Mamifero,Ave):
  pass
        
        
murcielago = Murcielago()
print(murcielago.amamantar())
print(murcielago.volar())
print(murcielago.comer())

print(Murcielago.mro())