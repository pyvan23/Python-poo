class Estudiante:
# metodo constructor se ejecuta siempre que se crea el objeto
    def __init__(self,nombre,grado,edad):
        self.nombre = nombre 
        self.grado = grado
        self.edad = edad
        
    def llamar (self):
        print(f"El alumno: {self.nombre} Estudiando " )
        
terminar = False
        
while not terminar:
    nombre = input("Cual es el nombre del estudiante?")
    grado = input("A qué grado pertenece?")
    edad = input("Edad?")
    
    estudiante1 = Estudiante(nombre, grado, edad)
    estudiante1.llamar()
    
    terminar = input("Oprima cualquier tecla para terminar o 'q' para salir: ") == 'q'
