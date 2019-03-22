import pygame
import sys
import os
import subprocess
import ctypes
from .Cursor import Cursor
from .Boton import Boton

pygame.init()


class GUI:

    def __init__(self, grafo):
        self.grafo = grafo
        self.cursor = Cursor()
        self.pintar()
        self.n = 0

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
        if os.name == "posix":
            icon = pygame.image.load("../Imágenes/acueducto.png")
            imagen1 = pygame.image.load("../Imágenes/boton.png")
            imagen = pygame.image.load("../Imágenes/boton1.png")
            barrio = pygame.image.load("../Imágenes/Barrio.png")
            tanque = pygame.image.load("../Imágenes/tanque.png")
            fondo = pygame.image.load("../Imágenes/fondo.png")
        else:
            icon = pygame.image.load("..\\Imágenes\\acueducto.png")
            imagen1 = pygame.image.load("..\\Imágenes\\boton.png")
            imagen = pygame.image.load("..\\Imágenes\\boton1.png")
            barrio = pygame.image.load("..\\Imágenes\\Barrio.png")
            tanque = pygame.image.load("..\\Imágenes\\tanque.png")
            fondo = pygame.image.load("..\\Imágenes\\fondo.png")
        icon = pygame.transform.scale(icon, (32, 32))
        pygame.display.set_icon(icon)
        imagen = pygame.transform.scale(imagen, (160, 80))
        imagen1 = pygame.transform.scale(imagen1, (160, 80))
        barrio = pygame.transform.scale(barrio, (100, 100))
        tanque = pygame.transform.scale(tanque, (30, 50))
        fondo = pygame.transform.scale(fondo, size)
        boton = Boton(imagen, imagen1, 50, 50)
        boton1 = Boton(imagen, imagen1, 50, 100)
        agregar = fuenteb.render("    Agregar barrio", True, (0, 0, 0))
        obstruccion = fuenteb.render(" Crear obstrucción", True, (0, 0, 0))

        while True:
            for evento in pygame.event.get():
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.cursor.colliderect(boton.rect):
                        self.grafo = boton.agregar(self.grafo)
                    elif self.cursor.colliderect(boton1.rect):
                        nota = fuenteb.render("SELECCIONE TUBERIA A OBSTRUIR.", True, (0, 255, 0))
                        ventana.blit(nota, (500, 500))
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            ventana.blit(fondo, (0, 0))
            self.cursor.update()
            boton.update(ventana, self.cursor, agregar)
            boton1.update(ventana, self.cursor, obstruccion)
            if self.grafo is None:
                print("No hay grafo")
                pygame.quit()
                sys.exit()
            else:
                for j in range(0, len(self.grafo.aristas)):
                    texto1 = fuente.render(str(self.grafo.aristas[j].peso), True, (0, 0, 0))
                    pygame.draw.line(ventana, self.grafo.aristas[j].color,
                                     (self.grafo.aristas[j].origen.x, self.grafo.aristas[j].origen.y),
                                     (self.grafo.aristas[j].destino.x, self.grafo.aristas[j].destino.y), 20)
                    ventana.blit(texto1, self.pos_peso(j))
                for i in range(len(self.grafo.nodos)):
                    if self.grafo.nodos[i].tanque is True:
                        ventana.blit(tanque, (self.grafo.nodos[i].x + 30, self.grafo.nodos[i].y-55))

                    ventana.blit(barrio, (self.grafo.nodos[i].x-45, self.grafo.nodos[i].y-55))
            pygame.display.update()

    def pos_peso(self, j):
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
        if (tipo is 1 and tipo2 is 1) or (tipo is 2 and tipo2 is 2):
            posx += -30
            posy += 20
        elif (tipo is 1 and tipo2 is 2) or (tipo is 2 and tipo2 is 1):
            posx += -30
            posy += -30
        pos = (posx, posy)
        return pos
