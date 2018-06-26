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
    rectprateleira = pygame.__rect_constructor(360, 310, 470, 30)
    rectprateleira_a = pygame.__rect_constructor(0, 170, 240, 30)
    rectprateleira_b = pygame.__rect_constructor(1110, 170, 240, 30)
    rectpiano = pygame.__rect_constructor(900, 560, 500, 30)
    pygame.draw.rect(v.tela,(255,0,0,), rectprateleira, 2)
    rectAnnie = pygame.__rect_constructor(v.xAnnie, v.yAnnie + 146, 114, 70)
    pygame.draw.rect(v.tela, (255,0,0), rectAnnie, 2)
    pygame.draw.rect(v.tela, (255,0,0), rectAlavanca, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectprateleira, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectprateleira_a, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectprateleira_b, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectpiano, 2)


    collideprateleira = rectprateleira.colliderect(rectAnnie)
    collideprateleira_a = rectprateleira_a.colliderect(rectAnnie)
    collideprateleira_b = rectprateleira_b.colliderect(rectAnnie)
    collidealavanca = rectAlavanca.colliderect(rectAnnie)
    basecollide = base.colliderect(rectAnnie)
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
    v.tela.blit(grade, (180, -10))
    v.tela.blit(grade, (1086, -10))
    v.tela.blit(chave, (560, 260))
    v.tela.blit(chave, (1175, 140))

    if v.maca == 0:
        v.macaVel += 30
    if v.maca == 630:
        v.macaVel -= 30
    v.maca = v.maca + v.macaVel

    if v.maca_a == 660:
        v.macaVel_a += 30
    if v.maca_a == 1290:
        v.macaVel_a -= 30
    v.maca_a = v.maca_a + v.macaVel_a

    if basecollide or collideprateleira or collideprateleira_a or collideprateleira_b or collidepiano:
        v.gravidade = 0
        if v.bPulo:
            v.gravidade = -37
        elif not (basecollide or collideprateleira or collideprateleira_a or collideprateleira_b or collidepiano):
            if not v.bPulo:
                v.gravidade = 37
            
    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (80, 100))
        v.tela.blit(porta, (30, 350))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (42, 142))
        v.tela.blit(porta_aberta, (30, 350))