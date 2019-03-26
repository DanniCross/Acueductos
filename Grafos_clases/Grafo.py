from .Nodo import Nodo
from .Arista import Arista


class Grafo:

    def __init__(self):
        self.aristas = []
        self.nodos = []

    def add_nodo(self, iden, x, y, tanque):
        nodo = Nodo(iden, x, y, tanque)
        if nodo in self.nodos:
            return
        self.nodos.append(nodo)

    def add_arista(self, origen, destino, peso, color, imagen):
        arista = Arista(origen, destino, peso, color, imagen)
        auxar = Arista(destino, origen, peso, color, imagen)
        if arista in self.aristas or auxar in self.aristas:
            return
        self.aristas.append(arista)
        origen.adyacencias.append(destino)
        destino.adyacencias.append(origen)

    def buscar_nodo(self, iden):
        for nodo in self.nodos:
            if nodo.iden == iden:
                return nodo

    def imprimir(self, grafo):
        if self == grafo:
            grafo = self
        for nodo in grafo.nodos:
            print(nodo.iden, end=" ")
        print()
        for arista in grafo.aristas:
            print(arista.origen.iden, "-----", arista.destino.iden, " : ", arista.peso)
