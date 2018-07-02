import pygame, Annie, LanguageSelectionMenu, _thread, os, server, client
import Variaveis as v
import fase as f
from pygame.locals import *

pygame.init()

menu = LanguageSelectionMenu.main()


if menu == 1:
    _thread.start_new_thread(client.client_thread, ())
    while v.rodando:
        v.yAnnie = v.yAnnie + v.gravidade
        v.xAnnie += v.velX
        key = pygame.key.get_pressed()
        if not v.bPulo:
            if key[pygame.K_SPACE]:
                v.sPulo = 0
                v.spritemov = 0
                if v.direita:
                    v.dPulo = True
                    v.bPulo = True
                    v.direita = False
                    v.esquerda = False
                elif v.esquerda:
                    v.ePulo = True
                    v.bPulo = True
                    v.direita = False
                    v.esquerda = False
                else:
                    v.bPulo = True
                    v.dPulo = True
        else:
            if -37 <= v.gravidade <= 5:
                v.gravidade = v.gravidade - v.pulo
            else:
                if v.ePulo:
                    v.esquerda = True
                elif v.dPulo:
                    v.direita = True
                v.ePulo = False
                v.dPulo = False
                v.bPulo = False
                v.sPulo = 8
        for evento in pygame.event.get():
            if evento.type == QUIT:
                v.rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    v.rodando = False
                elif evento.key == K_x:
                    v.alavanca = True
                elif evento.key == K_LEFT and v.xAnnie > 0:
                    v.esquerda = True
                    v.direita = False
                    v.velX -= 10
                elif evento.key == K_RIGHT and v.xAnnie < 1336:
                    v.direita = True
                    v.esquerda = False
                    v.velX += 10
            if evento.type == KEYUP:
                if evento.key == K_LEFT:
                    v.direita = False
                    v.esquerda = False
                    v.spritemov = 0
                    v.velX = 0
                elif evento.key == K_x:
                    v.alavanca = False
                elif evento.key == K_RIGHT:
                    v.direita = False
                    v.esquerda = False
                    v.spritemov = 0
                    v.velX = 0
        v.clock.tick(v.FPS)
        f.faseAnnie()
if menu == 2:
    _thread.start_new_thread(server.server, ())
    while v.rodando:
        v.xGregor += v.gvelX
        v.yGregor += v.gvelY
        for evento in pygame.event.get():
            if evento.type == QUIT:
                v.rodando = False
            if evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    v.rodando = False
                elif evento.key == K_x:
                    v.alavanca = True
                elif evento.key == K_LEFT:
                    if v.yGregor == 518:
                        v.gdireita = False
                        v.gesquerda = True
                        v.cima = False
                        v.baixo = False
                    else:
                        v.gdireita = False
                        v.gesquerda = False
                        v.cima = True
                        v.baixo = False
                    v.gvelX -= 5
                elif evento.key == K_RIGHT:
                    if v.yGregor == 518:
                        v.gdireita = True
                        v.gesquerda = False
                        v.cima = False
                        v.baixo = False
                    else:
                        v.gdireita = False
                        v.gesquerda = False
                        v.cima = True
                        v.baixo = False
                    v.gvelX += 5
                elif evento.key == K_UP:
                    v.gdireita = False
                    v.gesquerda = False
                    v.cima = True
                    v.baixo = False
                    v.gvelY -= 5
                elif evento.key == K_DOWN:
                    v.gdireita = False
                    v.gesquerda = False
                    v.cima = False
                    v.baixo = True
                    v.gvelY += 5
            if evento.type == KEYUP:
                if evento.key == K_LEFT:
                    v.gesquerda = False
                    v.cima = False
                    v.gvelX = 0
                elif evento.key == K_RIGHT:
                    v.gdireita = False
                    v.cima = False
                    v.gvelX = 0
                elif evento.key == K_UP:
                    v.cima = False
                    v.gvelY = 0
                elif evento.key == K_DOWN:
                    v.baixo = False
                    v.gvelY = 0
                elif evento.key == K_x:
                    v.alavanca = False
        v.clock.tick(v.FPS)
        f.faseGregor()
os.remove('imagens/menu.jpg')
os.remove('imagens/sala.jpg')
os.remove('imagens/quarto.jpg')
pygame.quit()