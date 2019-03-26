import pygame
import sys
import os
import subprocess
import ctypes
from .Cursor import Cursor
from .Boton import Boton
import random
from time import sleep
from pygame import Rect
from math import *
from Grafos_clases.Grafo import Grafo

pygame.init()


class GUI:

    def __init__(self, grafo):
        self.x = 0
        self.y = 0
        self.posible = False
        self.sentido = False
        self.obs = False
        self.conexion = False
        self.tan = False
        self.aux = []
        self.grafo = grafo
        self.cursor = Cursor()
        self.pintar()
        self.n = 0
        self.tang = 0

    def screen_size(self):
        self.n = 0
        size = (None, None)
        args = ["xrandr", "-q", "-d", ":0"]
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        for line in proc.stdout:
            if isinstance(line, bytes):
                line = line.decode("utf-8")
                if "Screen" in line:
                    size = (int(line.split()[7]), int(line.split()[9][:-1]))
        return size

    def screen_sizeW(self):
        self.n = 0
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        ancho, alto = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
        size = (ancho, alto)
        return size

    def pintar(self):
        if os.name is "posix":
            size = self.screen_size()
            ventana = pygame.display.set_mode(size)
        else:
            size = self.screen_sizeW()
            ventana = pygame.display.set_mode(size, pygame.RESIZABLE)
        pygame.display.set_caption("Grafo")
        fuente = pygame.font.SysFont("Arial Narrow", 30)
        fuenteb = pygame.font.SysFont("Arial Narrow", 25)
        fuentec = pygame.font.SysFont("Arial Narror", 20)
        if os.name == "posix":
            icon = pygame.image.load("../Imágenes/acueducto.png")
            imagen1 = pygame.image.load("../Imágenes/boton.png")
            imagen = pygame.image.load("../Imágenes/boton1.png")
            barrio = pygame.image.load("../Imágenes/Barrio.png")
            tanque = pygame.image.load("../Imágenes/tanque.png")
            fondo = pygame.image.load("../Imágenes/fondo.png")
            obstruc = pygame.image.load("../Imágenes/grieta.png")
            gota = pygame.image.load("../Imágenes/gota.png")
        else:
            icon = pygame.image.load("..\\Imágenes\\acueducto.png")
            imagen1 = pygame.image.load("..\\Imágenes\\boton.png")
            imagen = pygame.image.load("..\\Imágenes\\boton1.png")
            barrio = pygame.image.load("..\\Imágenes\\Barrio.png")
            tanque = pygame.image.load("..\\Imágenes\\tanque.png")
            fondo = pygame.image.load("..\\Imágenes\\fondo.png")
            obstruc = pygame.image.load("..\\Imágenes\\grieta.png")
            gota = pygame.image.load("..\\Imágenes\\gota.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)
        imagen = pygame.transform.scale(imagen, (160, 80))
        imagen1 = pygame.transform.scale(imagen1, (160, 80))
        barrio = pygame.transform.scale(barrio, (100, 100))
        tanque = pygame.transform.scale(tanque, (40, 60))
        fondo = pygame.transform.scale(fondo, size)
        boton = Boton(imagen, imagen1, 50, 50)
        boton1 = Boton(imagen, imagen1, 50, 100)
        boton2 = Boton(imagen, imagen1, 50, 150)
        boton3 = Boton(imagen, imagen1, 50, 200)
        boton4 = Boton(imagen, imagen1, 50, 250)
        boton5 = Boton(imagen, imagen1, 50, 300)
        agregar = fuenteb.render("    Agregar barrio", True, (0, 0, 0))
        obstruccion = fuenteb.render(" Crear obstrucción", True, (0, 0, 0))
        addarist = fuenteb.render("     Añadir tuberia", True, (0, 0, 0))
        sentido = fuenteb.render("  Cambiar sentido", True, (0, 0, 0))
        addTanque = fuenteb.render("   Añadir tanque", True, (0, 0, 0))
        desbordar = fuenteb.render(" Desbordar tanque", True, (0, 0, 0))
        obstruc = pygame.transform.scale(obstruc, (30, 40))
        obs = fuente.render("SELECCIONE TUBERIA A OBSTRUIR", True, (255, 0, 0))
        sent = fuente.render("SELECCIONE TUBERIA A LA CUAL LE CAMBIARÁ EL SENTIDO", True, (255, 0, 0))
        tanq = fuente.render("  SELECCIONE UN BARRIO DONDE SE CREARÁ UN TANQUE,", True, (255, 0, 0))
        tanq2 = fuente.render("(LA POSICION QUE SE SUGIERE EN PANTALLA ES OPCIONAL)", True, (255, 0, 0))
        conex = fuente.render("ELIJA LOS BARRIOS ORIGEN Y DESTINO PARA LA NUEVA TUBERIA", True, (255, 0, 0))
        gota = pygame.transform.scale(gota, (20, 20))
        capacidad = fuenteb.render("Capacidad máxima de los tanques: 500", True, (255, 255, 255))

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONUP and evento.button == 1:
                    if self.cursor.colliderect(boton.rect):
                        self.grafo = boton.agregar(self.grafo, gota)
                    elif self.cursor.colliderect(boton1.rect):
                        self.obs = True
                    elif self.obs:
                        for a in self.grafo.aristas:
                            if (a.line.x < pygame.mouse.get_pos()[0] < a.line.right and a.line.y
                                    < pygame.mouse.get_pos()[1] < a.line.bottom):
                                a.obs = True
                                break
                        self.obs = False
                    elif self.cursor.colliderect(boton2.rect):
                        self.conexion = True
                    elif self.conexion:
                        for nodo in self.grafo.nodos:
                            if (nodo.line.x < pygame.mouse.get_pos()[0] < nodo.line.right and nodo.line.y
                                    < pygame.mouse.get_pos()[1] < nodo.line.bottom):
                                self.aux.append(nodo)
                                if len(self.aux) == 2:
                                    self.grafo.add_arista(self.aux[0], self.aux[1], random.randint(1, 50),
                                                          (186, 186, 177), gota)
                                    self.aux = []
                                    self.conexion = False
                                break
                    elif self.cursor.colliderect(boton3.rect):
                        self.sentido = True
                    elif self.sentido:
                        for arist in self.grafo.aristas:
                            if (arist.line.x < pygame.mouse.get_pos()[0] < arist.line.right and arist.line.y
                                    < pygame.mouse.get_pos()[1] < arist.line.bottom):
                                temp = arist.origen
                                arist.origen = arist.destino
                                arist.destino = temp
                                arist.origen.adyacencias.append(arist.destino)
                                arist.destino.adyacencias.remove(arist.origen)
                                break
                        self.sentido = False
                    elif self.cursor.colliderect(boton4.rect):
                        self.tan = True
                    elif self.tan:
                        for nodo in self.grafo.nodos:
                            if (nodo.line.x < pygame.mouse.get_pos()[0] < nodo.line.right and nodo.line.y
                                    < pygame.mouse.get_pos()[1] < nodo.line.bottom):
                                nodo.tanque = True
                                break
                        self.tan = False
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            if self.conexion:
                ventana.blit(conex, (500, 20))
                pygame.display.update()
            if self.tan:
                ventana.blit(tanq, (500, 20))
                ventana.blit(tanq2, (500, 40))
                posibles = []
                for nodo in self.grafo.nodos:
                    self.posible = True
                    for node in self.grafo.nodos:
                        if nodo.tanque is not True:
                            for nd in node.adyacencias:
                                if node.tanque:
                                    if nd == nodo:
                                        self.posible = False
                                    elif self.posible is not False:
                                        self.posible = True
                    if self.posible:
                        posibles.append(nodo)
                for n in posibles:
                    if n.tanque is not True:
                        ventana.blit(tanque, (n.x + 55, n.y - 20))
                pygame.display.update()
            if self.obs:
                ventana.blit(obs, (550, 20))
                pygame.display.update()
            """if self.conexion:
                grafo = Grafo()
                for nodo in self.grafo.nodos:
                    grafo.add_nodo(nodo.iden, nodo.x, nodo.y, nodo.tanque)
                for no in grafo.nodos:
                    for n in grafo.nodos:
                        if n is not no:
                            grafo.add_arista(no, n, random.randint(1, 50), (255, 255, 255), gota)
                for j, ari in enumerate(grafo.aristas):
                    texto1 = fuente.render(str(grafo.aristas[j].peso), True, (0, 0, 0))
                    pygame.draw.line(ventana, (255, 0, 0), (ari.origen.line.centerx, ari.origen.line.centery),
                                     (ari.destino.line.centerx, ari.destino.line.centery), 33)
                    ari.line = (
                        pygame.draw.line(ventana, ari.color, (ari.origen.line.centerx, ari.origen.line.centery),
                                         (ari.destino.line.centerx, ari.destino.line.centery), 30))
                    ventana.blit(texto1, (ari.line.centerx, ari.line.centery))
                pygame.display.update()"""
            if self.sentido:
                ventana.blit(sent, (550, 20))
                pygame.display.update()
            ventana.blit(fondo, (0, 0))
            self.cursor.update()
            boton.update(ventana, self.cursor, agregar)
            boton1.update(ventana, self.cursor, obstruccion)
            boton2.update(ventana, self.cursor, addarist)
            boton3.update(ventana, self.cursor, sentido)
            boton4.update(ventana, self.cursor, addTanque)
            boton5.update(ventana, self.cursor, desbordar)
            ventana.blit(capacidad, (50, 10))

            for j, ari in enumerate(self.grafo.aristas):
                texto1 = fuente.render(str(self.grafo.aristas[j].peso), True, (0, 0, 0))
                pos1 = self.pos_peso(j, 0)
                pos = self.pos_peso(j, 1)
                ari.line = (pygame.draw.line(ventana, ari.color, (ari.origen.line.centerx, ari.origen.line.centery),
                                             (ari.destino.line.centerx, ari.destino.line.centery), 30))
                ventana.blit(texto1, (pos[0], pos[1]))
                if ari.obs:
                    ventana.blit(obstruc, (pos1[0], pos1[1]))
                if not ari.origen.tanque:
                    continue
                desx = ari.destino.line.centerx
                orix = ari.origen.line.centerx
                desy = ari.destino.line.centery
                oriy = ari.origen.line.centery
                rads = atan2(desy - oriy, desx - orix)
                dirx = 1
                diry = 1
                if desx - orix < 0:
                    dirx = -1
                if desy - oriy < 0:
                    diry = -1
                self.tang = tan(rads)
                if self.tang == 0:
                    self.tang = 0.5
                movex = dirx
                movey = tan(rads) * movex
                if abs(movey) < 1:
                    movey = diry
                    movex = movey / self.tang
                if abs(movex) < 1:
                    movex = dirx
                if abs(movey) < 0.1:
                    movey = diry
                    movex = 0.01
                sleep(0.002)
                ari.rect.centerx += movex
                ari.rect.centery += movey
                if dirx == -1:
                    if ari.rect.centerx < ari.destino.line.centerx:
                        ari.rect.centerx = ari.destino.line.centerx
                else:
                    if ari.rect.centerx > ari.destino.line.centerx:
                        ari.rect.centerx = ari.destino.line.centerx
                if diry == -1:
                    if ari.rect.centery < ari.destino.line.centery:
                        ari.rect.centery = ari.destino.line.centery
                else:
                    if ari.rect.centery > ari.destino.line.centery:
                        ari.rect.centery = ari.destino.line.centery
                rect1 = ari.rect
                rect2 = ari.destino.line
                if rect1.colliderect(rect2):
                    ari.rect = Rect(orix, oriy, 20, 20)
                if ari.obs or ari.origen.nivel <= 0:
                    continue
                ventana.blit(gota, ari.rect)
                ari.origen.nivel -= ari.peso/100
                if ari.destino.tanque:
                    ari.destino.nivel += ari.peso/100
            for nodo in self.grafo.nodos:
                if nodo.tanque:
                    if nodo.nivel < 0:
                        nodo.nivel = 0
                    if nodo.nivel > nodo.capacidad:
                        niv = fuentec.render(str(int(nodo.nivel)), True, (255, 0, 0))
                    else:
                        niv = fuentec.render(str(int(nodo.nivel)), True, (0, 0, 0))
                    ventana.blit(tanque, (nodo.x + 55, nodo.y - 20))
                    if nodo.nivel >= nodo.capacidad - 25:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y - 10, 28, 38))
                        if 500 < nodo.nivel <= 550:
                            pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 65, nodo.y + 20, 40, 10))
                        elif 550 < nodo.nivel <= 600:
                            pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 65, nodo.y + 20, 45, 10))
                        elif 600 < nodo.nivel <= 650:
                            pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 65, nodo.y + 20, 50, 10))
                        elif 650 < nodo.nivel:
                            pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 65, nodo.y + 20, 55, 10))
                    elif nodo.nivel >= nodo.capacidad - 50:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y - 8, 28, 36))
                    elif nodo.nivel >= nodo.capacidad - 75:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y - 6, 28, 34))
                    elif nodo.nivel >= nodo.capacidad - 100:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y - 4, 28, 32))
                    elif nodo.nivel >= nodo.capacidad - 125:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y - 2, 28, 30))
                    elif nodo.nivel >= nodo.capacidad - 150:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y, 28, 28))
                    elif nodo.nivel >= nodo.capacidad - 175:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 2, 28, 26))
                    elif nodo.nivel >= nodo.capacidad - 300:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 4, 28, 24))
                    elif nodo.nivel >= nodo.capacidad - 325:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 6, 28, 22))
                    elif nodo.nivel >= nodo.capacidad - 350:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 8, 28, 20))
                    elif nodo.nivel >= nodo.capacidad - 375:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 10, 28, 18))
                    elif nodo.nivel >= nodo.capacidad - 400:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 12, 28, 16))
                    elif nodo.nivel >= nodo.capacidad - 425:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 14, 28, 14))
                    elif nodo.nivel >= nodo.capacidad - 450:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 16, 28, 12))
                    elif nodo.nivel >= nodo.capacidad - 475:
                        pygame.draw.rect(ventana, (0, 0, 255), (nodo.x + 62, nodo.y + 18, 28, 10))

                    ventana.blit(niv, (nodo.x + 62, nodo.y - 15))
                nodo.line = ventana.blit(barrio, (nodo.x, nodo.y))

            pygame.display.update()

    def pos_peso(self, j, i):
        if self.grafo.aristas[j].origen.x < self.grafo.aristas[j].destino.x:
            posx = self.grafo.aristas[j].origen.x + \
                   ((self.grafo.aristas[j].destino.x - self.grafo.aristas[j].origen.x) / 2)
            tipo = 1
        else:
            posx = self.grafo.aristas[j].destino.x + \
                   ((self.grafo.aristas[j].origen.x - self.grafo.aristas[j].destino.x) / 2)
            tipo = 2
        if self.grafo.aristas[j].origen.y < self.grafo.aristas[j].destino.y:
            posy = self.grafo.aristas[j].origen.y + \
                   ((self.grafo.aristas[j].destino.y - self.grafo.aristas[j].origen.y) / 2)
            tipo2 = 1
        else:
            posy = self.grafo.aristas[j].destino.y + \
                   ((self.grafo.aristas[j].origen.y - self.grafo.aristas[j].destino.y) / 2)
            tipo2 = 2
        if i is 1:
            if (tipo is 1 and tipo2 is 1) or (tipo is 2 and tipo2 is 2):
                posx += 20
                posy += 60
            elif (tipo is 1 and tipo2 is 2) or (tipo is 2 and tipo2 is 1):
                posx += 35
                posy += 10
        else:
            if (tipo is 1 and tipo2 is 1) or (tipo is 2 and tipo2 is 2):
                posx += 40
                posy += 35
            elif (tipo is 1 and tipo2 is 2) or (tipo is 2 and tipo2 is 1):
                posx += 35
                posy += 30
        pos = [posx, posy]
        return pos
