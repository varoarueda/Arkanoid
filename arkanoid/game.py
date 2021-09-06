# game es el director de la pelicula, organiza las diferentes pantallas del juego
import pygame as pg
from arkanoid import ALTO, ANCHO #arkanoid es el módulo
from arkanoid.escenas import Portada, Partida, Records # importamos las escenas para que este archivo las reconozca

pg.init()

class Game():
    def __init__(self):
        pantalla = pg.display.set_mode((ANCHO, ALTO)) # Crea pantalla con medidas
        self.escenas = [Portada(pantalla), Partida(pantalla), Records(pantalla)] # Necesita una lista de escenas. Intancias de las escenas (ipmportar para que las reconozca, instanciarlas y meterles la pantalla)

    def launch(self): # Método empezar el juego
        i = 0
        while True: # Bucle para llamar a todas las escenas de la lista self.escenas e ir lanzándolas
            self.escenas[i].bucle_principal() # Llamando a la escena, con el .blucle_principal, asegura que todas las escenas que itera lo tenga (porque lo necesita cada escena)
            i += 1
            if i == len(self.escenas): # Condición para que el bucle sea infinito e itere seguido por las escenas. Cuando llega al final de la lista, vuelve a empezar. Solo va a salir si en la escena llamamos a "sys exit()""
                i = 0

        pg.quit()


