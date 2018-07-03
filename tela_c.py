import pygame, Annie
import Variaveis as v
from pygame.locals import *


def tela_c():
    pygame.init()

    maca = pygame.transform.scale(v.cenario.maca, (40, 40))
    piano = pygame.transform.scale(v.cenario.piano, (500, 400))
    grade = pygame.transform.scale(v.cenario.grade, (75, 230))
    moldura = pygame.transform.scale(v.cenario.moldura, (180, 220))
    chave = pygame.transform.scale(v.cenario.chave, (120, 60))
    luminaria_a = pygame.transform.scale(v.cenario.luminaria_a, (150, 150))
    prateleira = pygame.transform.scale(v.cenario.prateleira, (250, 75))
    alavanca_on = v.cenario.alavanca_on
    alavanca_off = v.cenario.alavanca_off
    porta = pygame.transform.scale(v.cenario.porta, (180, 350))
    porta_aberta = pygame.transform.scale(v.cenario.porta_aberta, (180, 350))
    base = pygame.__rect_constructor(-10, 738, 1376, 30)

    rectAlavanca = alavanca_on.get_rect(topleft=(120, 150))
    rectprateleira = pygame.__rect_constructor(360, 310, 460, 30)
    rectprateleira_a = pygame.__rect_constructor(0, 170, 240, 30)
    rectprateleira_b = pygame.__rect_constructor(1100, 170, 240, 30)
    rectpiano = pygame.__rect_constructor(980, 560, 500, 30)
    rectAnnie = pygame.__rect_constructor(v.xAnnie + 10, v.yAnnie + 146, 74, 70)
    rectmaca = maca.get_rect(topleft=(v.maca, 250))
    rectmaca_a = maca.get_rect(topleft=(v.maca_a, 250))
    rectgrade = grade.get_rect(topleft=(180, -10))
    rectgrade_a = grade.get_rect(topleft=(1086, -10))
    rectkey = chave.get_rect(topleft=(560, 260))
    rectkey_a = chave.get_rect(topleft=(1175, 140))
    rectporta = porta.get_rect(topleft=(30, 350))

    collideporta = rectporta.colliderect(rectAnnie)
    collidegrade = rectgrade.colliderect(rectAnnie)
    collidegrade_a = rectgrade_a.colliderect(rectAnnie)
    collidekey = rectkey.colliderect(rectAnnie)
    collidekey_a = rectkey_a.colliderect(rectAnnie)
    collideprateleira = rectprateleira.colliderect(rectAnnie)
    collideprateleira_a = rectprateleira_a.colliderect(rectAnnie)
    collideprateleira_b = rectprateleira_b.colliderect(rectAnnie)
    collidealavanca = rectAlavanca.colliderect(rectAnnie)
    basecollide = base.colliderect(rectAnnie)
    collidemaca = rectmaca.colliderect(rectAnnie)
    collidemaca_a = rectmaca_a.colliderect(rectAnnie)
    collidepiano = rectpiano.colliderect(rectAnnie)

    v.tela.blit(prateleira, (350, 300))
    v.tela.blit(prateleira, (600, 300))
    v.tela.blit(prateleira, (0, 180))
    v.tela.blit(prateleira, (1100, 180))
    v.tela.blit(moldura, (500, 400))
    v.tela.blit(luminaria_a, (200, 300))
    v.tela.blit(luminaria_a, (1000, 300))
    v.tela.blit(maca, (v.maca, 250))
    v.tela.blit(maca, (v.maca_a, 250))
    v.tela.blit(piano, (900, 400))

    if v.maca == 0:
        v.macaVel += 15
    if v.maca == 630:
        v.macaVel -= 15
    v.maca = v.maca + v.macaVel

    if v.maca_a == 660:
        v.macaVel_a += 15
    if v.maca_a == 1290:
        v.macaVel_a -= 15
    v.maca_a = v.maca_a + v.macaVel_a

    if collidekey:
        v.key = True
    elif not v.key:
        v.tela.blit(grade, (1086, -10))
        v.tela.blit(chave, (560, 260))
    elif v.key:
        collidegrade_a = False

    if collidegrade_a:
        v.xAnnie -= 10

    if collidekey_a:
        v.key_a = True
    elif not v.key_a:
        v.tela.blit(grade, (180, -10))
        v.tela.blit(chave, (1175, 140))
    elif v.key_a:
        collidegrade = False

    if collidegrade:
        v.xAnnie += 10

    if basecollide or collideprateleira or collideprateleira_a or collideprateleira_b or collidepiano:
        v.gravidade = 0
        if v.bPulo:
            v.gravidade = -37
    elif not (basecollide or collideprateleira or collideprateleira_a or collideprateleira_b or collidepiano) and not v.bPulo:
            v.gravidade = 37

    if collidemaca or collidemaca_a:
        v.xAnnie = v.largura / 2
        v.yAnnie = 580
            
    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (80, 100))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True
            v.tela_f = True

    if v.tela_c:
        v.tela.blit(porta_aberta, (30, 350))
        if collideporta and v.tela_f:
            v.annie_tela = 3
            v.alavanca_off = False
            v.tela_f = False

    if not v.tela_c:
        v.tela.blit(porta, (30, 350))

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (42, 142))
