import pygame
import sys
from .Cursor import Cursor
from .Boton import Boton

pygame.init()


class GUI:

    def __init__(self, grafo):
        self.grafo = grafo
        self.cursor = Cursor()
        self.pintar()

    def pintar(self):
        ventana = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Grafo")
        fuente = pygame.font.SysFont("Comic Sans MS", 30)
        color = (0, 255, 255)
        imagen = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/Grafos/Imágenes/boton.png")
        imagen1 = pygame.image.load("/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/Grafos/Imágenes/boton1.png")
        boton = Boton(imagen, imagen1, 200, 50)

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ventana.fill((255, 255, 255))
            self.cursor.update()
            boton.update(ventana, self.cursor)
            if self.grafo is None:
                print("No hay grafo")
                pygame.quit()
                sys.exit()
            else:
                for j in range(0, len(self.grafo.aristas)):
                    if self.grafo.aristas[j].origen.x < self.grafo.aristas[j].destino.x:
                        posx = self.grafo.aristas[j].origen.x + \
                               ((self.grafo.aristas[j].destino.x - self.grafo.aristas[j].origen.x)/2)
                    else:
                        posx = self.grafo.aristas[j].destino.x + \
                               ((self.grafo.aristas[j].origen.x - self.grafo.aristas[j].destino.x)/2)
                    if self.grafo.aristas[j].origen.y < self.grafo.aristas[j].destino.y:
                        posy = self.grafo.aristas[j].origen.y + \
                               ((self.grafo.aristas[j].destino.y - self.grafo.aristas[j].origen.y)/2)
                    else:
                        posy = self.grafo.aristas[j].destino.y + \
                               ((self.grafo.aristas[j].origen.y - self.grafo.aristas[j].destino.y)/2)
                    texto1 = fuente.render(str(self.grafo.aristas[j].peso), True, (0, 0, 0))
                    ventana.blit(texto1, (posx, posy))
                    pygame.draw.line(ventana, self.grafo.aristas[j].color,
                                     (self.grafo.aristas[j].origen.x, self.grafo.aristas[j].origen.y),
                                     (self.grafo.aristas[j].destino.x, self.grafo.aristas[j].destino.y), 2)
                for i in range(len(self.grafo.nodos)):
                    pygame.draw.circle(ventana, color, (self.grafo.nodos[i].x, self.grafo.nodos[i].y), 25, 0)
                    texto = fuente.render(self.grafo.nodos[i].iden, True, (0, 0, 0))
                    ventana.blit(texto, (self.grafo.nodos[i].x - 7, self.grafo.nodos[i].y - 8))
            pygame.display.update()
