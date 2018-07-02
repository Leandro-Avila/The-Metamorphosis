import pygame, Annie
import Variaveis as v
from pygame.locals import *


def tela_b():
    pygame.init()

    maca = pygame.transform.scale(v.cenario.maca, (40, 40))
    lareira = pygame.transform.scale(v.cenario.lareira, (400, 300))
    moldura = pygame.transform.scale(v.cenario.moldura, (180, 220))
    luminaria_a = pygame.transform.scale(v.cenario.luminaria_a, (150, 150))
    prateleira = pygame.transform.scale(v.cenario.prateleira, (250, 75))
    alavanca_on = v.cenario.alavanca_on
    alavanca_off = v.cenario.alavanca_off
    porta = pygame.transform.scale(v.cenario.porta, (180, 350))
    porta_aberta = pygame.transform.scale(v.cenario.porta_aberta, (180, 350))
    base = pygame.__rect_constructor(-10, 738, 1376, 30)

    rectAlavanca = alavanca_on.get_rect(topleft=(120, 150))
    rectprateleira = pygame.__rect_constructor(460, 310, 470, 30)
    rectprateleira_a = pygame.__rect_constructor(70, 185, 240, 30)
    rectprateleira_b = pygame.__rect_constructor(1110, 510, 240, 30)
    rectAnnie = pygame.__rect_constructor(v.xAnnie + 10, v.yAnnie + 146, 84, 70)
    rectporta = porta.get_rect(topleft=(30, 350))
    rectmaca = maca.get_rect(topleft=(v.maca, 250))

    collideporta = rectporta.colliderect(rectAnnie)
    collideprateleira = rectprateleira.colliderect(rectAnnie)
    collideprateleira_a = rectprateleira_a.colliderect(rectAnnie)
    collideprateleira_b = rectprateleira_b.colliderect(rectAnnie)
    collidealavanca = rectAlavanca.colliderect(rectAnnie)
    collidemaca = rectmaca.colliderect(rectAnnie)
    basecollide = base.colliderect(rectAnnie)

    v.tela.blit(prateleira, (450, 300))
    v.tela.blit(prateleira, (700, 300))
    v.tela.blit(prateleira, (60, 180))
    v.tela.blit(prateleira, (1100, 500))
    v.tela.blit(moldura, (300, 100))
    v.tela.blit(luminaria_a, (200, 300))
    v.tela.blit(luminaria_a, (1000, 300))
    v.tela.blit(lareira, (480, 410))
    v.tela.blit(maca, (v.maca, 250))

    if v.maca == 0:
        v.macaVel += 40
    if v.maca == 1320:
        v.macaVel -= 40
    v.maca = v.maca + v.macaVel

    if basecollide or collideprateleira or collideprateleira_a or collideprateleira_b:
        v.gravidade = 0
        if v.bPulo:
            v.gravidade = -37
    elif not (basecollide or collideprateleira or collideprateleira_a or collideprateleira_b) and not v.bPulo:
        v.gravidade = 37

    if collidemaca:
        v.xAnnie = v.largura / 2
        v.yAnnie = 580

    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (120, 100))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True
            v.tela_e = True

    if v.tela_b:
        v.tela.blit(porta_aberta, (30, 350))
        if collideporta and v.tela_e:
            v.annie_tela = 2
            v.maca = 0
            v.alavanca_off = False
            v.tela_e = False

    if not v.tela_b:
        v.tela.blit(porta, (30, 350))

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (82, 142))
