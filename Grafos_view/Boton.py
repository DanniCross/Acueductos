import pygame


class Boton(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super(Boton, Boton).__init__()
        self.x = x
        self.y = y

    def agregar(self, cursor):
        for evento in pygame.event.get():
            if evento == cursor.colliderect(pygame.Rect):
                pass
