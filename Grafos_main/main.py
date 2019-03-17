from Grafos_clases.Grafo import Grafo
from Grafos_view.GUI import GUI
from Grafos_clases.Recorridos import Recorridos


def main():

    grafo1 = Grafo()
    recorrido = Recorridos(grafo1)
    grafo1.add_nodo("A", 500, 100)
    grafo1.add_nodo("B", 400, 300)
    grafo1.add_nodo("C", 600, 300)
    grafo1.add_nodo("D", 500, 400)
    grafo1.add_nodo("E", 350, 150)

    grafo1.add_arista(grafo1.buscar_nodo("A"), grafo1.buscar_nodo("E"), 3, (0, 0, 0))
    grafo1.add_arista(grafo1.buscar_nodo("D"), grafo1.buscar_nodo("B"), 1, (0, 0, 0))
    grafo1.add_arista(grafo1.buscar_nodo("B"), grafo1.buscar_nodo("A"), 7, (0, 0, 0))
    grafo1.add_arista(grafo1.buscar_nodo("C"), grafo1.buscar_nodo("D"), 10, (0, 0, 0))

    grafo2 = recorrido.kruskal()
    grafo1.imprimir(grafo1)
    GUI(grafo1)


main()
