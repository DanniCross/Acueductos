from pygame import Rect


class Arista:

    def __init__(self, origen, destino, peso, color, imagen):
        self.origen = origen
        self.destino = destino
        self.peso = peso
        self.color = color
        self.rect = Rect(origen.line.centerx, origen.line.centery, 20, 20)
        self.obs = False
        self.line = None
        self.imagen = imagen
