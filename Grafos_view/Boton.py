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
        ventana.blit(agregar, (self.x, self.y + 32))

    def agregar(self, grafo1, imagen):
        if self is not grafo1:
            grafo = grafo1
            iden = random.choice(string.ascii_letters)
            pas = False
            i = 0
            x = random.randint(250, 1300)
            y = random.randint(60, 670)
            n = random.randint(0, len(grafo.nodos) - 1)
            t = random.randint(2, 10)
            while pas:
                if grafo.nodos[n].iden != iden:
                    pas = False
                else:
                    n = random.randint(0, len(grafo.nodos) - 1)
            if len(grafo.nodos) > 0:
                while i in range(len(grafo.nodos)):
                    if len(grafo.nodos) == 32:
                        print("No se pueden añadir más nodos")
                        break
                    else:
                        if iden != grafo.nodos[i].iden:
                            if pas is not True:
                                pas = True
                            if i == len(grafo.nodos) - 1:
                                while self.sobrepos(x, y, grafo):
                                    x = random.randint(250, 950)
                                    y = random.randint(60, 650)
                        else:
                            iden = random.choice(string.ascii_letters)
                            i = -1
                            if pas is not False:
                                pas = False
                        i += 1
            else:
                if t % 2 == 0:
                    tanque = True
                else:
                    tanque = False
                grafo.add_nodo(iden, x, y, tanque)
            if pas is True:
                if t % 2 == 0:
                    tanque = True
                else:
                    tanque = False
                grafo.add_nodo(iden, x, y, tanque)
                actual = grafo.buscar_nodo(iden)
                for nodo in grafo.nodos:
                    print("hola")
                    if ((actual.x == nodo.x + 100 or actual.x == nodo.x - 100)
                            and (actual.y == nodo.y + 100 or actual.y == nodo.y - 100)):
                        print("hola2")
                        grafo.add_arista(grafo.buscar_nodo(iden), grafo.buscar_nodo(grafo.nodos[n].iden),
                                         random.randint(1, 50), (186, 186, 177), imagen)
                        print(actual.x, actual.y)
                        print(nodo.x, nodo.y)
                        break

            return grafo

    def sobrepos(self, x, y, grafo):
        if self is not grafo:
            for nd in grafo.nodos:
                if nd.x >= x - 100 and nd.y >= y - 100:
                    if nd.x <= x + 100 and nd.y <= y + 100:
                        return True
            return False
