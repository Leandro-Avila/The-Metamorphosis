import pygame as pg
import Variaveis as v
from pygame.locals import *
from time import sleep


def main(language):
    screen = v.tela
    background = pg.transform.scale(pg.image.load('imagens/menu.jpg'), (v.largura, v.altura))
    credito = pg.transform.scale(pg.image.load('imagens/creditos.jpeg'), (v.largura, v.altura))
    pag_um = pg.transform.scale(pg.image.load('imagens/pag1.jpg'), (v.largura, v.altura))
    pag_dois = pg.transform.scale(pg.image.load('imagens/pag2.jpg'), (v.largura, v.altura))
    pag_tres = pg.transform.scale(pg.image.load('imagens/pag3.jpg'), (v.largura, v.altura))
    pag_quatro = pg.transform.scale(pg.image.load('imagens/pag4.jpg'), (v.largura, v.altura - 200))
    quit = pg.transform.scale(pg.image.load('imagens/end-' + language + '.png'), (200, 120))
    start = pg.transform.scale(pg.image.load('imagens/start-' + language + '.png'), (200, 120))
    credtis = pg.transform.scale(pg.image.load('imagens/credits-' + language + '.png'), (200, 120))
    screen.blit(background, (0, 0))
    screen.blit(start, (500, 290))
    screen.blit(credtis, (750, 290))
    screen.blit(quit, (1100, 600))
    personagem = 0
    rectstart = start.get_rect(topleft=(500, 290))
    rectcred = credtis.get_rect(topleft=(750, 290))
    rectquit = quit.get_rect(topleft=(1100, 600))
    play = False
    while personagem == 0:
        pos = pg.mouse.get_pos()
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
                if pg.mouse.get_pressed()[0] and rectcred.collidepoint(pos):
                    screen.blit(credito, (0, 0))
                    rectstart = start.get_rect(topleft=(50, 50))
                    screen.blit(start, (50, 50))
                    screen.blit(quit, (1100, 600))
                if play:
                    screen.blit(v.background.Sala, (0, 0))
                    v.tela.blit(v.player.Annie, (250, 200))
                    v.tela.blit(v.gplayer.Gregor, (850, 190))
                    rect_annie = v.player.Annie.get_rect(topleft=(250, 200))
                    rect_gregor = v.gplayer.Gregor.get_rect(topleft=(850, 190))
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
    screen.blit(pag_um, (0, 0))
    pg.display.update()
    sleep(2.5)
    screen.blit(pag_dois, (0, 0))
    pg.display.update()
    sleep(2.5)
    screen.blit(pag_tres, (0, 0))
    pg.display.update()
    sleep(2.5)
    screen.blit(pag_quatro, (0, 0))
    pg.display.update()
    sleep(2.5)
    return personagem

