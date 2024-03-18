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


class Habitacion(pygame.sprite.Sprite):
    def __init__(self, recursos_escenario, tamaño, coordenadas, enemigos, trampas, tesoros = None):
        super().__init__()
        self.recursos_escenario = recursos_escenario
        self.coordenadas = coordenadas
        self.tamaño = tamaño
        self.enemigos = enemigos
        self.trampas = trampas
        self.tesoros = tesoros
    
    def draw(self, ventana_juego):
        escenario = crear_escenario(imagen = self.recursos_escenario, tamaño_escenario= self.tamaño, coordenadas_escenario= self.coordenadas, tamaño_bloques=[16, 16])

        escenario.draw(ventana_juego)


escenario_inicio = Habitacion(ruta_bloque, [10, 10], [80, 50], False, False, False)
        
