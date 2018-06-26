import pygame, Annie
import Variaveis as v
from pygame.locals import *


def tela_a():
    pygame.init()

    guarda_roupa = pygame.transform.scale(v.cenario.guarda_roupa, (275, 500))
    cama = pygame.transform.scale(v.cenario.cama, (400, 300))
    luminaria_a = pygame.transform.scale(v.cenario.luminaria_a, (150, 150))
    prateleira = pygame.transform.scale(v.cenario.prateleira, (250, 75))
    alavanca_on = v.cenario.alavanca_on
    alavanca_off = v.cenario.alavanca_off
    porta = pygame.transform.scale(v.cenario.porta, (180, 350))
    porta_aberta = pygame.transform.scale(v.cenario.porta_aberta, (180, 350))
    base = pygame.__rect_constructor(-10, 738, 1376, 30)

    rectAlavanca = alavanca_on.get_rect(topleft=(120, 150))
    rectcama = pygame.__rect_constructor(990, 600, 350, 50)
    rectprateleira = pygame.__rect_constructor(570, 340, 200, 30)
    rectGuarda_roupa = pygame.__rect_constructor(50, 260, 275, 30)
    rectAnnie = pygame.__rect_constructor(v.xAnnie, v.yAnnie + 156, 120, 55)

    collideGuarda_roupa = rectGuarda_roupa.colliderect(rectAnnie)
    collideprateleira = rectprateleira.colliderect(rectAnnie)
    collidecama = rectcama.colliderect(rectAnnie)
    collidealavanca = rectAlavanca.colliderect(rectAnnie)
    basecollide = base.colliderect(rectAnnie)

    v.tela.blit(prateleira, (550, 330))
    v.tela.blit(cama, (950, 450))
    v.tela.blit(luminaria_a, (200, 300))
    v.tela.blit(luminaria_a, (1000, 300))
    pygame.draw.rect(v.tela, (255, 0, 0), rectAlavanca, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectcama, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectprateleira, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectGuarda_roupa, 2)
    pygame.draw.rect(v.tela, (255, 0, 0), rectAnnie, 2)

    if basecollide or collidecama or collideprateleira or collideGuarda_roupa:
        v.gravidade = 0
        if v.bPulo:
            v.gravidade = -37
    elif not (basecollide or collidecama or collideprateleira or collideGuarda_roupa) and not v.bPulo:
        v.gravidade = 37

    if not v.alavanca_off:
        v.tela.blit(alavanca_on, (120, 150))
        v.tela.blit(porta, (760, 350))

    if collidealavanca:
        if v.alavanca:
            v.alavanca_off = True
            v.tela_d = True

    if v.alavanca_off:
        v.tela.blit(alavanca_off, (82, 192))

    if v.tela_a:
        v.tela.blit(porta_aberta, (760, 350))

    v.tela.blit(guarda_roupa, (50, 210))