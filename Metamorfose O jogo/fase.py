import pygame, Annie
import Variaveis as v
from tela_a import tela_a
from tela_b import tela_b
from tela_c import tela_c
from tela_d import tela_d
from tela_e import tela_e
from tela_f import tela_f
from time import sleep

pag_cinco = pygame.transform.scale(pygame.image.load('imagens/pag5.jpg'), (v.largura, v.altura))
pag_seis = pygame.transform.scale(pygame.image.load('imagens/pag6.jpg'), (v.largura, v.altura))
pag_sete = pygame.transform.scale(pygame.image.load('imagens/pag7.jpg'), (v.largura, v.altura))
pag_oito = pygame.transform.scale(pygame.image.load('imagens/pag8.jpg'), (v.largura, v.altura))

pygame.init()


def faseAnnie():
    v.tela.blit(v.background.Sala, (0, 0))
    if v.annie_tela == 0:
        tela_a()
    elif v.annie_tela == 1:
        tela_b()
    elif v.annie_tela == 2:
        tela_c()
    elif v.annie_tela == 3:
        v.tela.blit(pag_cinco, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.tela.blit(pag_seis, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.tela.blit(pag_sete, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.tela.blit(pag_oito, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.rodando = False

    if v.annie_tela != 3:
        if v.spritemov >= 98:
            v.spritemov = 0
        if v.direita:
            v.tela.blit(v.player.AnnieDireita[v.spritemov//14], (v.xAnnie, v.yAnnie))
            v.spritemov += 7
        elif v.esquerda:
            v.tela.blit(v.player.AnnieEsquerda[v.spritemov//14], (v.xAnnie, v.yAnnie))
            v.spritemov += 7
        elif v.ePulo:
            v.tela.blit(v.player.AnniePulandoE[v.sPulo//2], (v.xAnnie, v.yAnnie))
            if v.sPulo < 8:
                v.sPulo += 2
        elif v.dPulo:
            v.tela.blit(v.player.AnniePulando[v.sPulo//2], (v.xAnnie, v.yAnnie))
            if v.sPulo < 8:
                v.sPulo += 2
        else:
            v.tela.blit(v.player.AnnieEntrando[0], (v.xAnnie, v.yAnnie))
    pygame.display.update()


def faseGregor():
    v.tela.blit(v.gbackground.Quarto, (0, 0))
    if v.gregor_tela == 0:
        tela_d()
    elif v.gregor_tela == 1:
        tela_e()
    elif v.gregor_tela == 2:
        tela_f()
    elif v.gregor_tela == 3:
        v.tela.blit(pag_cinco, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.tela.blit(pag_seis, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.tela.blit(pag_sete, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.tela.blit(pag_oito, (0, 0))
        pygame.display.update()
        sleep(2.5)
        v.rodando = False

    if v.gregor_tela != 3:
        if v.spriteg >= 128:
            v.spriteg = 0
        if v.gdireita:
            v.tela.blit(v.gplayer.GregorDireita[v.spriteg//16], (v.xGregor, v.yGregor))
            v.spriteg += 8
        elif v.gesquerda:
            v.tela.blit(v.gplayer.GregorEsquerda[v.spriteg//16], (v.xGregor, v.yGregor))
            v.spriteg += 8
        elif v.cima:
            v.tela.blit(v.gplayer.GregorCima[v.spriteg//16], (v.xGregor, v.yGregor))
            v.spriteg += 8
        elif v.baixo:
            v.tela.blit(v.gplayer.GregorBaixo[v.spriteg//16], (v.xGregor, v.yGregor))
            v.spriteg += 8
        else:
            if v.yGregor == 518:
                v.tela.blit(v.gplayer.GregorEntrando[0], (v.xGregor, v.yGregor))
            else:
                v.tela.blit(v.gplayer.GregorCima[1], (v.xGregor, v.yGregor))
    pygame.display.update()