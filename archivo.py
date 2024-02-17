#Programa que lee e interactua con un archivo JSON

import json

def verDatos(archivo):
    with open(archivo,'r', encoding='utf-8') as datos: # Se abre el archivo JSON en modo de lecutra y en codificación utf-8
        plantilla = json.load(datos) 
        #print(plantilla)

        for jugador in plantilla["jugadores"]:
            #print(jugador)
            print('')
            print('Nombre: ', jugador["nombre"])
            print('Apellido: ', jugador["apellido"])
            print('Edad: ', jugador["edad"])
            print('Su paso por el fútbol: ', jugador["equipos"])
            print('')
            
def agregarJugador(archivo):
    # Solicita al usuario que ingrese la información del nuevo jugador
    nombre = input("Ingresa el nombre del jugador: ")
    apellido = input("Ingresa el apellido del jugador: ")
    edad = int(input("Ingresa la edad del jugador: "))
    
    equipos = []
    while True:
        equipo = input("Ingresa un equipo en el que ha estado el jugador (teclea 'salir' para terminar): ")
        if equipo.lower() == 'salir':
            break
        equipos.append(equipo)

    nuevo_jugador = {
        "nombre": nombre,
        "apellido": apellido,
        "edad": edad,
        "equipos": equipos
    }

    # Abre el archivo JSON y carga los datos
    with open(archivo, 'r', encoding='utf-8') as datos:
        plantilla = json.load(datos)

    # Agrega el nuevo jugador a la lista de jugadores
    plantilla["jugadores"].append(nuevo_jugador)

    # Escribe los datos actualizados en el archivo JSON
    with open(archivo, 'w', encoding='utf-8') as datos:
        json.dump(plantilla, datos, ensure_ascii=False, indent=4)

def menu():
    while True:
        print("\nElija una de las siguientes opciones: ")
        print("1. Ver datos de los jugadores")
        print("2. Agregar un nuevo jugador")
        print("x. Salir")
        opcion = input("¿Que opción desea ejecutar?: ")

        if opcion == '1':
            verDatos(archivo)
        elif opcion == '2':
            agregarJugador(archivo)
        elif opcion.lower() == 'x':
            break
        else:
            print("La opción no es valida, intente de nuevo...")


if __name__ == '__main__':
    archivo = 'Data/data.json' # Variable que almacena la ubicación del archivo JSON
    menu()