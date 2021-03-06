import json
import os
import pygame


class JSON:

    def Leer(self, grafo):
        gota = pygame.image.load("../Imágenes/gota.png")
        gota = pygame.transform.scale(gota, (20, 20))
        if self != grafo:
            pass
        grafo = grafo
        if os.name is "posix":
            fil = "../grafo.json"
        else:
            fil = "..\\grafo.json"
        with open(fil) as file:
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
                                     arista['peso'], (186, 186, 177), gota)
        return grafo
