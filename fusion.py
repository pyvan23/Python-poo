class Personaje:
    
    def __init__(self,nombre,poder):
        self.nombre = nombre
        self.poder = poder
        
    def __repr__(self) -> str:
        return f'{self.nombre} poder:{self.poder}'
    
    def __add__(self,otro_personaje):
        nuevo_nombre = self.nombre + "-" + otro_personaje.nombre
        nuevo_poder = (self.poder  + otro_personaje.poder)*2
        return Personaje(nuevo_nombre,nuevo_poder)
    
    
    
#goku = Personaje('Goku',10000)
#vegeta = Personaje('Vegeta',9999)
#vegeto = goku + vegeta
#print(vegeto)
opcion = ''
lista_de_fusiones = []
while True:
    print("======= Menú =======")
    print("1. Agregar fusión")
    print("2. Imprimir lista de fusiones")
    print("3. Eliminar personaje de la lista")
    print("0. Terminar")
    
    opcion = input("Selecciona una opción: ")

    if opcion == '1':
        nombre_primer_personaje = input('Cual es el nombre del primer personaje que quieres fusionar?')
        poder_primer_personaje = int(input('Cual es el poder del primer personaje que quieres fusionar?'))
        personaje1 = Personaje(nombre_primer_personaje, poder_primer_personaje)
        
        nombre_segundo_personaje = input('Cual es el nombre del segundo personaje que quieres fusionar?')
        poder_segundo_personaje = int(input('Cual es el poder del segundo personaje que quieres fusionar?'))
        personaje2 = Personaje(nombre_segundo_personaje, poder_segundo_personaje)
        
        fusion = personaje1 + personaje2
        lista_de_fusiones.append(fusion)
        print(f'Fusión agregada: {fusion}')

    elif opcion == '2':
        if True1:
            print("Lista de fusiones:")
            for index, fusion in enumerate(lista_de_fusiones, start=1):
                print(f"{index}. {fusion}")
        else:
            print("La lista de fusiones está vacía.")

    elif opcion == '3':
        if lista_de_fusiones:
            print("Selecciona el índice del personaje a eliminar:")
            for index, fusion in enumerate(lista_de_fusiones, start=1):
                print(f"{index}. {fusion}")
            try:
                indice_eliminar = int(input("Índice a eliminar: ")) - 1
                if 0 <= indice_eliminar < len(lista_de_fusiones):
                    fusion_eliminada = lista_de_fusiones.pop(indice_eliminar)
                    print(f"Se ha eliminado: {fusion_eliminada}")
                else:
                    print("Índice inválido.")
            except ValueError:
                print("Entrada inválida. Debes ingresar un número.")

        else:
            print("La lista de fusiones está vacía.")

    elif opcion == '0':
        print("Saliendo del programa...")
        break

    else:
        print("Opción inválida. Por favor, selecciona una opción válida.")