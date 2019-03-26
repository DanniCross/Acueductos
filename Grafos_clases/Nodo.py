from pygame import Rect


class Nodo:

    def __init__(self, iden, x, y, tanque):
        self.adyacencias = []
        self.iden = iden
        self.x = x
        self.y = y
        self.line = Rect(x, y, 100, 100)
        self.tanque = tanque
        if self.tanque:
            self.capacidad = 500
            self.nivel = 500
