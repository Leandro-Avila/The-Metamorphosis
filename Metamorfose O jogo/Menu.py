import pygame as pg
import Variaveis as v
from pygame.locals import *
import os

def main(language):
    screen = v.tela
    background = pg.transform.scale(pg.image.load('imagens/menu.jpg'), (v.largura, v.altura))
    quit = pg.transform.scale(pg.image.load('imagens/end-' + language + '.png'), (200, 120))
    start = pg.transform.scale(pg.image.load('imagens/start-' + language + '.png'), (200, 120))
    credtis = pg.transform.scale(pg.image.load('imagens/credits-' + language + '.png'), (200, 120))
    screen.blit(background, (0, 0))
    screen.blit(start, (450, 290))
    screen.blit(credtis, (750, 290))
    screen.blit(quit, (1100, 600))
    personagem = 0
    play = False
    while personagem == 0:
        pos = pg.mouse.get_pos()
        rectstart = start.get_rect(topleft=(450, 290))
        rectcred = credtis.get_rect(topleft=(750, 290))
        rectquit = quit.get_rect(topleft=(1100, 600))
        for evento in pg.event.get():
            if evento.type == QUIT:
                pg.quit()
            elif evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    os.remove('imagens/menu.jpg')
                    os.remove('imagens/sala.jpg')
                    os.remove('imagens/quarto.jpg')
                    pg.quit()
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0] and rectstart.collidepoint(pos):
                    play = True
                if play:
                    screen.blit(v.background.Sala, (0, 0))
                    v.tela.blit(v.player.Annie, (350, 200))
                    v.tela.blit(v.gplayer.Gregor, (750, 190))
                    rect_annie = v.player.Annie.get_rect(topleft=(350, 200))
                    rect_gregor = v.gplayer.Gregor.get_rect(topleft=(750, 190))
                    if rect_annie.collidepoint(pos) and pg.mouse.get_pressed()[0]:
                            personagem = 1
                    elif rect_gregor.collidepoint(pos) and pg.mouse.get_pressed()[0]:
                            personagem = 2
                elif pg.mouse.get_pressed()[0] and rectquit.collidepoint(pos):
                    os.remove('imagens/menu.jpg')
                    os.remove('imagens/sala.jpg')
                    os.remove('imagens/quarto.jpg')
                    pg.quit()
        pg.display.update()
    return personagem

