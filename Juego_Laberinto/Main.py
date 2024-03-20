from colisiones import * 
from Sprites import *
from Castle_Objects import *
import pygame

pygame.init()

ANCHO_VENTANA, ALTO_VENTANA = 1300, 700

VENTANA_PRINCIPAL = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Las aventuras de Juan")

rectas_escenarios = {
                        #top, bottom, left, right
    "escenario_inicio": [125, 310, 80, 310],
    "escenario_reuiniones": [75, 265, 530, 750],
    "escenario_descanso": [470, 650, 85, 300],
    "escenario_principal": [470, 675, 505, 795],
    "escenario_tropas": [205, 565, 963, 1225]
}

rectas_pasillos = {
    "inicio-reuiniones": [109, 232, 295, 545],
    "inicio-descanso": [310, 470, 165, 220],
    "descanso-principal": [542, 585, 295, 505],
    "principal-reuiniiones": [265, 470, 625, 680],
    "principal-tropas": [360, 402, 675, 965]
}

cartero = Personaje(nombre="Juan", objeto_spritesheets=sprites, coordenadas=(580, 240), velocidad=2, escenario_actual=escenario_inicio, limites_rectangulo=rectas_escenarios["escenario_reuiniones"])

reloj = pygame.time.Clock()


juego_terminado = False
while juego_terminado != True:

    reloj.tick(50)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            juego_terminado = True

    VENTANA_PRINCIPAL.fill((0, 0, 0)) #(83, 76, 206)

    #bloque.draw(VENTANA_PRINCIPAL)
    #escenario_inicio.draw(VENTANA_PRINCIPAL)
    escenario_inicio.escenario.draw(VENTANA_PRINCIPAL)
    escenario_de_reuiniones.escenario.draw(VENTANA_PRINCIPAL)
    escenario_de_descanso.escenario.draw(VENTANA_PRINCIPAL)
    escenario_principal.escenario.draw(VENTANA_PRINCIPAL)
    escenario_de_tropas.escenario.draw(VENTANA_PRINCIPAL)

    colision_pasillos = pygame.sprite.spritecollide(cartero, pasillos_mapa, False)

    if colision_pasillos:
        cartero.limites_rectangulo = [75, 675, colision_pasillos[0].rect.left, colision_pasillos[0].rect.right]

    print(cartero.rect.right)
    pasillos_mapa.draw(VENTANA_PRINCIPAL)

    cartero.update(VENTANA_PRINCIPAL)

    pygame.display.flip()
