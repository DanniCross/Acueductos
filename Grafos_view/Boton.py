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
        grafo = grafo1
        id = random.choice(string.ascii_letters)
        pas = False
        pas2 = False
        i = 0
        j = 0
        x = random.randint(250, 700)
        y = random.randint(20, 600)
        if len(grafo.nodos) > 0:
            while i in range(len(grafo.nodos)):
                print(i, pas, id)
                if id != grafo.nodos[i].iden:
                    print(id)
                    if pas is not True:
                        pas = True
                    if i == len(grafo.nodos) - 2:
                        while j < len(grafo.nodos):
                            if x != grafo.nodos[j].x and x != grafo.nodos[j].x + 50 and x != grafo.nodos[j].x - 50:
                                if y != grafo.nodos[j].y and y != grafo.nodos[j].y + 50 and y != grafo.nodos[j].y - 50:
                                    if pas2 is not True:
                                        pas2 = True
                                    print(j)
                                else:
                                    y = random.randint(20, 600)
                                    j = -1
                                    if pas2 is not False:
                                        pas2 = False
                                        print(j)
                            else:
                                if pas2 is not True:
                                    pas2 = True
                                print(j)
                            j += 1
                else:
                    id = random.choice(string.ascii_letters)
                    i = -1
                    if pas is not False:
                        pas = False
                i += 1
        else:
            grafo.add_nodo(id, x, y)
        if pas is True and pas2 is True:
            grafo.add_nodo(id, x, y)
        return grafo
