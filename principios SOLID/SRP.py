class TanqueDeCombustible:
    def __init__(self) -> None:
        self.combustible = 100
        
    def agregar_combustible(self,cantidad):
        self.combustible += cantidad 
    
    def obtener_combustible(self):
        return self.combustible
    
    def usar_combustible(self,cantidad):
        self.combustible -= cantidad
        
         
class Auto:
    def __init__(self,tanque) -> None:
        self.posicion = 0
        self.tanque = tanque
        
    def mover(self,distancia):
        if self.tanque.obtener_combustible() >= distancia / 2:
            self.posicion += distancia
            self.tanque.usar_combustible(distancia / 2)
            print('El auto esta en movimiento')
        else:
            print('No hay suficiente combustible')
            
    def obtener_posicion(self):
        return self.posicion
          
            
            
tanque_nafta = TanqueDeCombustible()
clio = Auto(tanque_nafta)

print(clio)
print(clio.obtener_posicion())
clio.mover(20)
print(clio.obtener_posicion())
clio.mover(150)
print(clio.obtener_posicion())
clio.mover(120)
print(clio.obtener_posicion())