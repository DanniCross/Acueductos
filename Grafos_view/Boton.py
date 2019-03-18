import pygame
import random
import string


class Boton(pygame.sprite.Sprite):

    def __init__(self, imagen, imagen1, x, y):
        super(Boton, Boton).__init__(self)
        self.normal = imagen
        self.seleccion = imagen1
        self.actual = self.normal
        self.rect = self.actual.get_rect()
        self.rect.left, self.rect.top = (x, y)
        self.x = x
        self.y = y

    def update(self, ventana, cursor, agregar):
        if cursor.colliderect(self.rect):
            self.actual = self.seleccion
        else:
            self.actual = self.normal
        ventana.blit(self.actual, self.rect)
        ventana.blit(agregar, (65, 83))

    def agregar(self, grafo):
        grafo = grafo
        pas = True
        id = random.choice(string.ascii_letters)
        x = random.randint(200, 600)
        y = random.randint(50, 400)
        for nodo in grafo.nodos:
            while pas:
                if nodo.x == x or x == nodo.x + 80 or x == nodo.x - 80:
                    if nodo.y != y and y != nodo.y + 80 and y != nodo.y - 80:
                        pas = False
                        continue
                    else:
                        y = random.randint(200, 600)
                else:
                    pas = False
        grafo.add_nodo(id, x, y)
        if len(grafo.nodos) > 1:
            i = random.randrange(0, len(grafo.nodos))
            if grafo.nodos[i].iden != id:
                grafo.add_arista(grafo.buscar_nodo(id), grafo.buscar_nodo(grafo.nodos[i].iden),
                                 random.randint(1, 50), (0, 0, 0))
        return grafo
