from abc import ABC, abstractmethod

class VerificadorOrtografico(ABC):
    @abstractmethod
    def verificar_palabra(self,palabra):
        pass
    
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass
class Diccionario(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar palabras si esta en el diccionario
        pass
class ServicioOnline(VerificadorOrtografico):
    def verificar_palabra(self, palabra):
        #logica para verificar el servicio web
        pass
    
#depende de la implemenacion concreta de diccionario, depende de una interfaz osea de la clase abstaracta
class CorrectorOrtografico:
    def __init__(self,verificador) -> None:
        self.verificador = verificador
        
    def corregir_texto(self,texto):
        #usamos el verificador para corregir texto
        pass
    
correctr = CorrectorOrtografico(Diccionario())