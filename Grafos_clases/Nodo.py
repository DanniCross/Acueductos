class Nodo:

    def __init__(self, iden, x, y, tanque):
        self.adyacencias = []
        self.iden = iden
        self.x = x
        self.y = y
        self.tanque = tanque
        if self.tanque is True:
            self.capacidad = 50
