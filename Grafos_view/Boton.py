import pygame


class Boton(pygame.sprite.Sprite):

    def __init__(self, imagen, imagen1, x, y):
        super(Boton, Boton).__init__(self)
        pygame.transform.scale(imagen, (5, 10), imagen)
        pygame.transform.scale(imagen1, (5, 10), imagen1)
        self.normal = imagen
        self.seleccion = imagen1
        self.actual = self.normal
        self.rect = self.actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

    def update(self, ventana, cursor):
        if cursor.colliderect(self.rect):
            self.actual = self.seleccion
        else:
            self.actual = self.normal
        ventana.blit(self.actual, self.rect)
