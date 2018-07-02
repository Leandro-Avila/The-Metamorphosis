import pygame, Gregor
import Variaveis as v
from pygame.locals import *


def tela_e():
    pygame.init()

    maca = pygame.transform.scale(v.gcenario.maca, (40, 40))
    g = pygame.transform.scale(v.gcenario.grade, (75, 230))
    moldura = pygame.transform.scale(v.gcenario.moldura, (180, 220))
    grade = pygame.transform.rotate(g, 270)
    guarda_roupa = pygame.transform.scale(v.gcenario.guarda_roupa, (275, 500))
    cama = pygame.transform.scale(v.gcenario.cama, (400, 300))
    luminaria_a = pygame.transform.scale(v.gcenario.luminaria_a, (150, 150))
    prateleira = pygame.transform.scale(v.gcenario.prateleira, (250, 75))
    chave = pygame.transform.scale(v.gcenario.chave, (120, 60))
    alavanca_on = v.gcenario.alavanca_on
    alavanca_off = v.gcenario.alavanca_off
    porta = pygame.transform.scale(v.gcenario.porta, (180, 350))
    porta_aberta = pygame.transform.scale(v.gcenario.porta_aberta, (180, 350))
    base = pygame.__rect_constructor(-10, 738, 1376, 30)

    rectgrade = grade.get_rect(topleft=(1140, 220))
    rectAlavanca = alavanca_on.get_rect(topleft=(1200, 600))
    rectcamal = pygame.__rect_constructor(170, 560, 2, 400)
    rectcamar = pygame.__rect_constructor(560, 560, 2, 400)
    rectcamat = pygame.__rect_constructor(180, 550, 360, 2)
    rectprateleirat = pygame.__rect_constructor(0, 220, 240, 2)
    rectprateleirab = pygame.__rect_constructor(0, 250, 240, 2)
    rectGuarda_roupal = pygame.__rect_constructor(920, 230, 2, 500)
    rectGuarda_roupar = pygame.__rect_constructor(1160, 230, 2, 500)
    rectGuarda_roupat = pygame.__rect_constructor(930, 220, 220, 2)
    rectchave = chave.get_rect(topleft=(50, 150))
    rectGregor = v.gplayer.GregorEntrando[0].get_rect(topleft=(v.xGregor, v.yGregor))
    rectporta = porta.get_rect(topleft=(700, 350))

    collideporta = rectporta.colliderect(rectGregor)
    collideprateleirat = rectprateleirat.colliderect(rectGregor)
    collideprateleirab = rectprateleirab.colliderect(rectGregor)
    collidekey = rectchave.colliderect(rectGregor)
    collidecamal = rectcamal.colliderect(rectGregor)
    collidecamar = rectcamar.colliderect(rectGregor)
    collidecamat = rectcamat.colliderect(rectGregor)
    collideGuarda_roupal = rectGuarda_roupal.colliderect(rectGregor)
    collideGuarda_roupar = rectGuarda_roupar.colliderect(rectGregor)
    collideGuarda_roupat = rectGuarda_roupat.colliderect(rectGregor)
    collidealavanca = rectAlavanca.colliderect(rectGregor)
    collidegrade = rectgrade.colliderect(rectGregor)
    basecollide = base.colliderect(rectGregor)

    v.tela.blit(prateleira, (0, 200))
    v.tela.blit(cama, (150, 450))
    v.tela.blit(luminaria_a, (v.largura/2, 50))
    v.tela.blit(guarda_roupa, (900, 210))
    v.tela.blit(moldura, (300, 250))
    v.tela.blit(maca, (v.maca, 250))

    if v.maca == 0:
        v.macaVel += 20
    if v.maca == 840:
        v.macaVel -= 20
    v.maca = v.maca + v.macaVel

    if collidekey:
        v.key = True
    elif not v.key:
        v.tela.blit(grade, (1140, 200))
        v.tela.blit(chave, (50, 150))
    elif v.key:
        collidegrade = False

    if basecollide or collidecamat or collideGuarda_roupat or collideprateleirat or collidegrade:
        v.yGregor -= 5

    if collidecamal or collideGuarda_roupal:
        v.xGregor -= 5

    if collidecamar or collideGuarda_roupar:
        v.xGregor += 5

    if collideprateleirab:
        v.yGregor += 5

    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (1200, 600))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True
            v.tela_b = True

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (1162, 642))

    if v.tela_e:
        v.tela.blit(porta_aberta, (700, 350))
        if collideporta and v.tela_b:
            v.gregor_tela = 2
            v.alavanca_off = False
            v.tela_b = False
            v.maca = 0
            v.xGregor = 50
            v.yGregor = 650

    if not v.tela_e:
        v.tela.blit(porta, (700, 350))
