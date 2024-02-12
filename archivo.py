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
            
if __name__ == '__main__':
    archivo = 'Data/data.json' # Variable que almacena la ubicación del archivo JSON
    verDatos(archivo)