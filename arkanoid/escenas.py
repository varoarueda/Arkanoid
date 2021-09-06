import pygame as pg
from . import FPS, ANCHO, ALTO # from . = from arkanoid (módulo)
from.entidades import Bola, Raqueta


class Escena():
    def __init__(self, pantalla): # Le paso la pantalla creada en game class Game (la misma ventana va a ser común a todas las escenas)
        self.pantalla = pantalla # Transformar pantalla en atibuto de la class Escena
        self.reloj = pg.time.Clock()

    def bucle_principal(self): # Lo dejo vacío y ya se definirá dentro de cada escena
        pass

class Portada(Escena): # Hereda de Escena
    def __init__(self, pantalla):
        super().__init__(pantalla) # super(). Hereda el init de la clase padre "class Escena". Siempre quiero el self.pantalla y el self.reloj de class Escena en class Portada
        self.logo = pg.image.load("resources/images/arkanoid_name.png") # Crea atributo logo y carga la imagen. La imagen se carga fuera del bucle.
        fuente = pg.font.Font("resources/fonts/CabinSketch-Bold.ttf", 40) # Crea la fuente, importando la fuente que quiera
        self.textito = fuente.render("Pulsa <SPC> para comentar", True, (0,0,0)) # Crea la imagen del texto (pygame render)
        self.anchoTexto = self.textito.get_width() # get.width da el ancho de textito

    def bucle_principal(self): # Creado como siempre
        game_over = False
        while not game_over:
            for evento in pg.event.get(): # Captura eventos
                if evento.type == pg.QUIT:
                    exit() # Antes era game_over = True. Se cambia para diferenciarlo del game_over = True de evento KEYDOWN y no acabe ahí el bucle y game de paso a la siguiente escena

                if evento.type == pg.KEYDOWN: # Captura eventos
                    if evento.key == pg.K_SPACE: # Presionar "espacio" y game.py tiene que dar paso a la siguiente escena, entonces finaliza el bucle
                        game_over = True # Acaba el bucle

            self.pantalla.fill((225, 225, 0)) # Relleno fondo surface
            self.pantalla.blit(self.logo, (140, 140)) # Pinta el logo en surface
            self.pantalla.blit(self.textito, ((ANCHO - self.anchoTexto) // 2, 640)) # pinta el texto en surface y le da cordenadas para centrarlo
            pg.display.flip() # renderiza en pantalla

class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla) # Vuelve a traer pantalla y reloj de class Escena
        self.fondo = pg.image.load("resources/images/background.jpg")
        self.player = Raqueta(midbottom =(ANCHO // 2, ALTO -15 ))
        self.bola = Bola(center = (ANCHO // 2, ALTO // 2 - 100))
        

    def bucle_principal(self):
        self.vidas = 3
        game_over = False
        while self.vidas > 0:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    exit()

            self.player.update()

            self.bola.update()

            self.bola.comprobar_colision(self.player)

            if not self.bola.viva:
                self.vidas -= 1
                self.bola.viva = True # Para reiniciar

            self.pantalla.blit(self.fondo, (0, 0)) 
            self.pantalla.blit(self.player.image, self.player.rect)
            self.pantalla.blit(self.bola.image, self.bola.rect)
            pg.display.flip()



class Records(Escena):
    pass


        



