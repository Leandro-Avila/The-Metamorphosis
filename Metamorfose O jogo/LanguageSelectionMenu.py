import pygame as pg
import Menu, os
import decompress as d
import Variaveis as v
from pygame.locals import *


def main():
    pg.mixer.music.load('sons/moon-light.mp3')
    pg.mixer.music.play(0)
    screen = v.tela
    d.decompress('imagens/menu')
    background = pg.transform.scale(pg.image.load('imagens/menu.jpg'), (v.largura, v.altura))
    screen.blit(background, (0, 0))
    myfont = pg.font.SysFont("monospace", 15)
    label = myfont.render("Select the language / Selecione o idioma", 1, (255, 255, 0))
    screen.blit(label, (500, 275))
    escolha = 0
    while escolha == 0:
        eua = pg.transform.scale(pg.image.load('imagens/eua.png'), (50, 40))
        screen.blit(eua, (600, 300))
        br = pg.transform.scale(pg.image.load('imagens/bandeira_nacional.png'), (50, 40))
        screen.blit(br, (700, 300))
        recteua = eua.get_rect(topleft=(600, 300))
        rectbr = br.get_rect(topleft=(700, 300))
        for evento in pg.event.get():
            pos = pg.mouse.get_pos()
            if evento.type == QUIT:
                os.remove('imagens/menu.jpg')
                os.remove('imagens/sala.jpg')
                os.remove('imagens/menu.jpg')
                pg.quit()
            elif evento.type == KEYDOWN:
                if evento.key == K_ESCAPE:
                    os.remove('imagens/menu.jpg')
                    os.remove('imagens/sala.jpg')
                    os.remove('imagens/menu.jpg')
                    pg.quit()
            elif evento.type == pg.MOUSEBUTTONDOWN:
                if pg.mouse.get_pressed()[0] and recteua.collidepoint(pos):
                    escolha = 1
                elif pg.mouse.get_pressed()[0] and rectbr.collidepoint(pos):
                    escolha = 2
        pg.display.update()
    if escolha == 1:
        return Menu.main("en")
    if escolha == 2:
        return Menu.main("br")