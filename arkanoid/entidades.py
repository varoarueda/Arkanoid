from pygame import sprite
import pygame as pg
from pygame.sprite import Sprite
from arkanoid import ALTO, ANCHO 


class Raqueta(Sprite): # Hereda de sprite
    disfraces = "electric00.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraces}") # otra sintaxis para .format. Hay que ponerle self. porque es una variable de clase, si estuviera dentro del init, seria una variable local y no haria falta el .self
        self.rect = self.image.get_rect(**kwargs) # método get_rect permite acceder al midbottom en class Partida 

    def update(self):
        if pg.key.get_pressed()[pg.K_LEFT]:
            self.rect.x -= 5

        if self.rect.left <= 0:
            self.rect.left = 0

        if pg.key.get_pressed()[pg.K_RIGHT]:
            self.rect.x += 5

        if self.rect.right >= ANCHO:
            self.rect.right = ANCHO


class Bola(Sprite):
    disfraces = "ball1.png"
    def __init__(self, **kwargs):
        self.image = pg.image.load(f"resources/images/{self.disfraces}")
        self.rect = self.image.get_rect(**kwargs) # Atributo rectángulo
        self.delta_x = 5 # Variación en x
        self.delta_y = 5
        self.viva = True 
        self.position = kwargs

    def update(self):
        self.rect.x += self.delta_x # Mueve la bola desde la cordenada x + la variación asiganda (delta_x = 5)
        if self.rect.x <= 0 or self.rect.right >= ANCHO:
            self.delta_x *= -1

        self.rect.y += self.delta_y 
        if self.rect.y <= 0:
            self.delta_y *= -1

        if self.rect.bottom >= ALTO:
            self.viva = False
            self.rect.center = self.image.get(**self.position_inicial)

    def comprobar_colision(self, otro):
        if self.rect.right >= otro.rect.left and self.rect.left <= otro.rect.right and \
           self.rect.bottom >= otro.rect.top and self.rect.top <= otro.rect.bottom:
           self.delta_y *= -1
            
    


       

