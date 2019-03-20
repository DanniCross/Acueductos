import json


class JSON:

    def Leer(self, grafo):
        if self != grafo:
            pass
        grafo = grafo
        with open('/run/media/josec/Jose Cruz/Documentos/Pycharm Projects/Grafos/grafo.json') as file:
            data = json.load(file)
            for graf in data['Grafo']:
                for nodo in graf['Nodo']:
                    if nodo['tanque'] == 0:
                        t = False
                    else:
                        t = True
                    grafo.add_nodo(nodo['id'], nodo['x'], nodo['y'], t)
                for arista in graf['Arista']:
                    grafo.add_arista(grafo.buscar_nodo(arista['origen']), grafo.buscar_nodo(arista['destino']),
                                     arista['peso'], (0, 0, 0))
        return grafo
