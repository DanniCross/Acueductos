from Grafos_view.GUI import GUI
from Grafos_clases.Grafo import Grafo
from Grafos_view.JSON import JSON


def main():
    grafo = Grafo()
    json = JSON()
    grafo = json.Leer(grafo)
    GUI(grafo)


main()
