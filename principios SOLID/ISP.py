from abc import ABC, abstractmethod

class Trabajador:
    @abstractmethod
    def trabajar(self):
        print('persona trabajando...')
class Comedor:
    @abstractmethod
    def comer(self):
        print('persona comiendo ...')
class Durmiente:
    
    @abstractmethod
    def dormir(self):
       pass
        
class Humano(Trabajador,Durmiente,Comedor):
    def dormir(self):
        print('persona durmiendo...')
    def comer(self):
        print('persona comiendo...')
    def trabajar(self):
        print('persona trabajando...')
    
class Robot(Trabajador):
    def trabajar(self):
        print('robot trabajando...')


robot = Robot()
robot.trabajar()
persona = Humano()
persona.trabajar()