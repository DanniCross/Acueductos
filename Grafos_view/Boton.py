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

    def agregar(self, grafo1):
        if self is not grafo1:
            grafo = grafo1
            iden = random.choice(string.ascii_letters)
            pas = False
            i = 0
            x = random.randint(250, 1300)
            y = random.randint(60, 670)
            if len(grafo.nodos) > 0:
                while i in range(len(grafo.nodos)):
                    if len(grafo.nodos) == 40:
                        print("No se pueden añadir más nodos")
                        break
                    else:
                        if iden != grafo.nodos[i].iden:
                            if pas is not True:
                                pas = True
                            if i == len(grafo.nodos) - 1:
                                while self.sobrepos(x, y, grafo):
                                    x = random.randint(250, 1300)
                                    y = random.randint(60, 670)
                        else:
                            iden = random.choice(string.ascii_letters)
                            i = -1
                            if pas is not False:
                                pas = False
                        i += 1
            else:
                grafo.add_nodo(iden, x, y, False)
            if pas is True:
                grafo.add_nodo(iden, x, y, False)
                n = random.randint(0, len(grafo.nodos) - 1)
                while pas:
                    if grafo.nodos[n].iden != iden:
                        pas = False
                    else:
                        n = random.randint(0, len(grafo.nodos) - 1)
                grafo.add_arista(grafo.buscar_nodo(iden), grafo.buscar_nodo(grafo.nodos[n].iden),
                                 random.randint(1, 50), (0, 0, 0))
            return grafo

    def sobrepos(self, x, y, grafo):
        if self is not grafo:
            for nd in grafo.nodos:
                if nd.x >= x - 100 and nd.y >= y - 100:
                    if nd.x <= x + 100 and nd.y <= y + 100:
                        return True
            return False
