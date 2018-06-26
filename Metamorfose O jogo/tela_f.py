import pygame, Gregor
import Variaveis as v
from pygame.locals import *


def tela_f():
    pygame.init()

    maca = pygame.transform.scale(v.gcenario.maca, (40, 40))
    moldura = pygame.transform.scale(v.gcenario.moldura, (180, 220))
    guarda_roupa = pygame.transform.scale(v.gcenario.guarda_roupa, (275, 500))
    cama = pygame.transform.scale(v.gcenario.cama, (400, 300))
    luminaria_a = pygame.transform.scale(v.gcenario.luminaria_a, (150, 150))
    alavanca_on = v.gcenario.alavanca_on
    alavanca_off = v.gcenario.alavanca_off
    porta = pygame.transform.scale(v.gcenario.porta, (180, 350))
    porta_aberta = pygame.transform.scale(v.gcenario.porta_aberta, (180, 350))
    base = pygame.__rect_constructor(-10, 738, 1376, 30)

    rectAlavanca = alavanca_on.get_rect(topleft=(1200, 600))
    rectcamal = pygame.__rect_constructor(170, 560, 2, 400)
    rectcamar = pygame.__rect_constructor(560, 560, 2, 400)
    rectcamat = pygame.__rect_constructor(180, 550, 360, 2)
    rectGuarda_roupal = pygame.__rect_constructor(550, 230, 2, 500)
    rectGuarda_roupar = pygame.__rect_constructor(820, 230, 2, 500)
    pygame.draw.rect(v.tela,(255,0,0), rectGuarda_roupar, 2)
    pygame.draw.rect(v.tela,(255,0,0), rectGuarda_roupal, 2)
    rectGuarda_roupat = pygame.__rect_constructor(570, 220, 220, 2)
    pygame.draw.rect(v.tela,(255,0,0), rectGuarda_roupat, 2)
    rectGregor = v.gplayer.GregorEntrando[0].get_rect(topleft=(v.xGregor, v.yGregor))

    collidecamal = rectcamal.colliderect(rectGregor)
    collidecamar = rectcamar.colliderect(rectGregor)
    collidecamat = rectcamat.colliderect(rectGregor)
    collideGuarda_roupal = rectGuarda_roupal.colliderect(rectGregor)
    collideGuarda_roupar = rectGuarda_roupar.colliderect(rectGregor)
    collideGuarda_roupat = rectGuarda_roupat.colliderect(rectGregor)
    collidealavanca = rectAlavanca.colliderect(rectGregor)
    basecollide = base.colliderect(rectGregor)

    v.tela.blit(cama, (150, 450))
    v.tela.blit(luminaria_a, (v.largura/2, 50))
    v.tela.blit(guarda_roupa, (550, 210))
    v.tela.blit(moldura, (200, 250))
    v.tela.blit(maca, (v.maca, 250))
    v.tela.blit(maca, (850, v.maca_y))
    v.tela.blit(maca, (1100, v.maca_y))

    if v.maca == 0:
        v.macaVel += 10
    if v.maca == 420:
        v.macaVel -= 10
    v.maca = v.maca + v.macaVel
    if v.maca_y == 0:
        v.macaVely += 20
    if v.maca_y == 680:
        v.macaVely -= 20
    v.maca_y = v.maca_y + v.macaVely

    if basecollide or collidecamat or collideGuarda_roupat:
        v.yGregor -= 5

    if collidecamal or collideGuarda_roupal:
        v.xGregor -= 5

    if collidecamar or collideGuarda_roupar:
        v.xGregor += 5

    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (1200, 600))
        v.tela.blit(porta, (900, 350))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (1162, 642))
        v.tela.blit(porta_aberta, (900, 350))