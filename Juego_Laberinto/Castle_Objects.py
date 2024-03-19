from Sprites import *
import pygame


pygame.init()

class Bloque(pygame.sprite.Sprite):
    def __init__(self, imagen, coordenadas):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.rect = self.image.get_rect()

        self.rect.x = coordenadas[0]
        self.rect.y = coordenadas[1]

    def draw(self, ventana_juego):
        ventana_juego.blit(self.image, self.rect)

ruta_bloque = "assets_villa/bloques_escenario/tile18.png"

def crear_escenario(imagen, tamaño_escenario, coordenadas_escenario, tamaño_bloques):

    cuadrados_escenario = pygame.sprite.Group()

    coordenada_y_bloque = coordenadas_escenario[1]

    for filas in range(tamaño_escenario[1]):
        coordenada_x_bloque = coordenadas_escenario[0]
        
        for columnas in range(tamaño_escenario[0]):
            cuadrados_escenario.add(Bloque(imagen, [coordenada_x_bloque, coordenada_y_bloque]))

            coordenada_x_bloque += tamaño_bloques[0]

        coordenada_y_bloque += tamaño_bloques[1]

    return cuadrados_escenario

def detectar_colision():
    pass


bloques_escenario_2 = crear_escenario(imagen = ruta_bloque, tamaño_escenario= [10, 10], coordenadas_escenario= [330, 78], tamaño_bloques=[16, 16])
bloques_escenario_3 = crear_escenario(imagen = ruta_bloque, tamaño_escenario= [10, 10], coordenadas_escenario= [80, 330], tamaño_bloques=[16, 16])
bloques_escenario_4 = crear_escenario(imagen = ruta_bloque, tamaño_escenario= [15, 10], coordenadas_escenario= [330, 330], tamaño_bloques=[16, 16])
#bloques_escenario_5 = crear_escenario(imagen = ruta_bloque, tamaño_escenario= [10, 10], coordenadas_escenario= [100, 200], tamaño_bloques=[16, 16])
#bloques_escenario_6 = crear_escenario(imagen = ruta_bloque, tamaño_escenario= [10, 10], coordenadas_escenario= [100, 200], tamaño_bloques=[16, 16])

class Escenario(pygame.sprite.Sprite):
    def __init__(self, nombre_escenario, imagen, coordenadas, tamaño_escenario):
        super().__init__()
        self.nombre_escenario = nombre_escenario
        self.image = pygame.transform.scale(imagen, (tamaño_escenario))
        self.rect = self.image.get_rect()

        self.rect.x = coordenadas[0]
        self.rect.y = coordenadas[1]

    def draw(self, ventana_juego):
        ventana_juego.blit(self.image, self.rect)

class Habitacion(pygame.sprite.Sprite):
    def __init__(self, nombre_habitacion, tamaño_habitacion, coordenadas, enemigos, trampas, tesoros = None):
        super().__init__()
        self.coordenadas = coordenadas
        self.escenario = Escenario(nombre_habitacion, recortar_imagen(pygame.image.load("assets_villa/dungeon_tiles.png"), 10, 10, 105, 105), self.coordenadas, tamaño_habitacion)
        self.rect = self.escenario.rect
        self.enemigos = enemigos
        self.trampas = trampas
        self.tesoros = tesoros
    
    def draw(self, ventana_juego):
        
        self.escenario.draw(ventana_juego)

#escenarios que representaran el mapa del juego
        
escenarios_mapa = pygame.sprite.Group()

escenario_inicio = Habitacion("colonia", (300, 250), [20, 60], False, False, False)
escenario_de_reuiniones = Habitacion("reuiniones", (290, 250), [470, 10], False, False, False)
escenario_de_descanso = Habitacion("descanso", (300, 250), [20, 400], False, False, False)
escenario_principal = Habitacion("principal", (420, 275), [400, 400], False, False, False)
escenario_de_tropas = Habitacion("tropas", (400, 600), [860, 10], False, False, False)


escenarios_mapa.add(escenario_inicio)
escenarios_mapa.add(escenario_de_reuiniones)
escenarios_mapa.add(escenario_de_descanso)
escenarios_mapa.add(escenario_principal)
escenarios_mapa.add(escenario_de_tropas)


pasillos_mapa = pygame.sprite.Group()

#los pasillos por donde el jugador podra pasar para llegar a los demás lugares
pasillos_mapa.add(Escenario("pasillo-colonia-reuiniones", recortar_imagen(pygame.image.load("assets_villa/dungeon_tiles.png"), 40, 40, 20, 25), (170, 290), (50, 175)))
pasillos_mapa.add(Escenario("pasillo-colonia-descanso", recortar_imagen(pygame.image.load("assets_villa/dungeon_tiles.png"), 40, 40, 20, 25), (297, 180), (250, 50)))
pasillos_mapa.add(Escenario("pasillo-colonia-principal", recortar_imagen(pygame.image.load("assets_villa/dungeon_tiles.png"), 40, 40, 20, 25), (297, 530), (212, 50)))
pasillos_mapa.add(Escenario("pasillo-principal-reuiniones", recortar_imagen(pygame.image.load("assets_villa/dungeon_tiles.png"), 40, 40, 20, 25), (627, 240), (50, 232)))
pasillos_mapa.add(Escenario("pasillo-colonia-tropas", recortar_imagen(pygame.image.load("assets_villa/dungeon_tiles.png"), 40, 40, 20, 25), (677, 350), (287, 50)))


