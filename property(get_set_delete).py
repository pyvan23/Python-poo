class Persona:
    def __init__(self,nombre,edad):
        #Convencion Super Private
        self.__nombre = nombre
        #Convencion  Private
        self._edad = edad
        
    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self,new_name):
         self.__nombre = new_name
    
    @nombre.deleter
    def nombre(self):
         del self.__nombre 
    
    
pyvan = Persona('Pyvan',35)
print(pyvan.nombre)
nombre = pyvan.nombre
pyvan.nombre = 'ivan23'
nombre = pyvan.nombre
print(nombre)
del pyvan.nombre