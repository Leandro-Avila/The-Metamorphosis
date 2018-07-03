import pygame, Gregor
import Variaveis as v
from pygame.locals import *


def tela_d():
    pygame.init()

    grade = pygame.transform.scale(v.gcenario.grade, (75, 230))
    guarda_roupa = pygame.transform.scale(v.gcenario.guarda_roupa, (275, 500))
    espelho = pygame.transform.scale(v.gcenario.espelho, (250, 300))
    cama = pygame.transform.scale(v.gcenario.cama, (400, 300))
    luminaria_a = pygame.transform.scale(v.gcenario.luminaria_a, (150, 150))
    prateleira = pygame.transform.scale(v.gcenario.prateleira, (250, 75))
    chave = pygame.transform.scale(v.gcenario.chave, (120, 60))
    alavanca_on = v.gcenario.alavanca_on
    alavanca_off = v.gcenario.alavanca_off
    porta = pygame.transform.scale(v.gcenario.porta, (180, 350))
    porta_aberta = pygame.transform.scale(v.gcenario.porta_aberta, (180, 350))
    base = pygame.__rect_constructor(-10, 738, 1376, 30)

    rectporta = porta.get_rect(topleft=(760, 350))
    rectgrade = grade.get_rect(topleft=(180, 0))
    rectAlavanca = alavanca_on.get_rect(topleft=(50, 115))
    rectcamal = pygame.__rect_constructor(420, 560, 2, 400)
    rectcamar = pygame.__rect_constructor(800, 560, 2, 400)
    rectcamat = pygame.__rect_constructor(430, 550, 360, 2)
    rectprateleirat = pygame.__rect_constructor(0, 220, 240, 2)
    rectprateleirab = pygame.__rect_constructor(0, 250, 240, 2)
    rectGuarda_roupal = pygame.__rect_constructor(1030, 230, 2, 500)
    rectGuarda_roupar = pygame.__rect_constructor(1260, 230, 2, 500)
    rectGuarda_roupat = pygame.__rect_constructor(1040, 210, 190, 2)
    rectchave = chave.get_rect(topleft=(1250, 650))
    rectGregor = v.gplayer.GregorEntrando[0].get_rect(topleft=(v.xGregor, v.yGregor))

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
    v.tela.blit(cama, (400, 450))
    v.tela.blit(luminaria_a, (v.largura/2, 50))
    v.tela.blit(espelho, (75, 375))
    v.tela.blit(guarda_roupa, (1000, 210))

    if collidekey:
        v.key = True
    elif not v.key:
        v.tela.blit(grade, (180, 0))
        v.tela.blit(chave, (1250, 650))
    elif v.key:
        collidegrade = False

    if basecollide or collidecamat or collideGuarda_roupat or collideprateleirat:
        v.yGregor -= 5

    if collidecamal or collideGuarda_roupal:
        v.xGregor -= 5

    if collidecamar or collideGuarda_roupar or collidegrade:
        v.xGregor += 5

    if collideprateleirab:
        v.yGregor += 5

    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (50, 115))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True
            v.tela_a = True

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (12, 157))

    if v.tela_d:
        v.tela.blit(porta_aberta, (830, 350))
        if collideporta and v.tela_a:
            v.key = False
            v.gregor_tela = 1
            v.alavanca_off = False
            v.tela_a = False
            v.maca = 0

    if not v.tela_d:
        v.tela.blit(porta, (830, 350))
