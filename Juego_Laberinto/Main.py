from colisiones import * 
from Sprites import *
from Castle_Objects import *
import pygame

pygame.init()

ANCHO_VENTANA, ALTO_VENTANA = 1300, 700

VENTANA_PRINCIPAL = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Las aventuras de Juan")

cartero = Personaje(nombre="Juan", objeto_spritesheets=sprites, coordenadas=(100, 240), velocidad=2, escenario_actual=escenario_inicio)

reloj = pygame.time.Clock()

juego_terminado = False
while juego_terminado != True:

    reloj.tick(50)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    VENTANA_PRINCIPAL.fill((83, 76, 206))

    #bloque.draw(VENTANA_PRINCIPAL)
    #escenario_inicio.draw(VENTANA_PRINCIPAL)
    escenario_inicio.escenario.draw(VENTANA_PRINCIPAL)
    escenario_de_reuiniones.escenario.draw(VENTANA_PRINCIPAL)
    escenario_de_descanso.escenario.draw(VENTANA_PRINCIPAL)
    escenario_principal.escenario.draw(VENTANA_PRINCIPAL)
    escenario_de_tropas.escenario.draw(VENTANA_PRINCIPAL)

    pasillos_mapa.draw(VENTANA_PRINCIPAL)

    print(cartero.direccion_movimiento)

    #cartero.draw(VENTANA_PRINCIPAL)
    cartero.update(VENTANA_PRINCIPAL)

    pygame.display.flip()
