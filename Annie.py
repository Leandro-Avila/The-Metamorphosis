import pygame
import decompress as d

class Annie:
    def __init__(self):
        self.pngAnnie = pygame.image.load('imagens/Annie.png')
        self.Annie = pygame.image.load('imagens/AnnieV1.1.png')
        self.AnnieDireita = []
        self.AnnieEsquerda = []
        self.AnniePulando = []
        self.AnniePulandoE = []
        self.AnnieEntrando = []
        self.AnnieSaindo = []

        self.AnnieDireita.append(self.pngAnnie.subsurface(134, 0, 134, 236))
        self.AnnieDireita.append(self.pngAnnie.subsurface(268, 0, 134, 236))
        self.AnnieDireita.append(self.pngAnnie.subsurface(402, 0, 134, 236))
        self.AnnieDireita.append(self.pngAnnie.subsurface(536, 0, 134, 236))
        self.AnnieDireita.append(self.pngAnnie.subsurface(670, 0, 134, 236))
        self.AnnieDireita.append(self.pngAnnie.subsurface(804, 0, 134, 236))
        self.AnnieDireita.append(self.pngAnnie.subsurface(938, 0, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(138, 259, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(276, 259, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(414, 259, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(552, 259, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(690, 259, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(828, 259, 134, 236))
        self.AnnieEsquerda.append(self.pngAnnie.subsurface(958, 259, 114, 216))
        self.AnniePulando.append(self.pngAnnie.subsurface(4, 505, 134, 226))
        self.AnniePulando.append(self.pngAnnie.subsurface(142, 505, 134, 226))
        self.AnniePulando.append(self.pngAnnie.subsurface(280, 505, 134, 226))
        self.AnniePulando.append(self.pngAnnie.subsurface(418, 505, 134, 226))
        self.AnniePulando.append(self.pngAnnie.subsurface(556, 505, 134, 223))
        self.AnniePulandoE.append(self.pngAnnie.subsurface(0, 728, 134, 216))
        self.AnniePulandoE.append(self.pngAnnie.subsurface(120, 728, 120, 216))
        self.AnniePulandoE.append(self.pngAnnie.subsurface(262, 728, 128, 216))
        self.AnniePulandoE.append(self.pngAnnie.subsurface(402, 728, 134, 216))
        self.AnniePulandoE.append(self.pngAnnie.subsurface(536, 728, 140, 216))
        self.AnnieEntrando.append(self.pngAnnie.subsurface(0, 0, 134, 236))
        self.AnnieSaindo.append(self.pngAnnie.subsurface(0, 236, 134, 236))


class Bg():
    def __init__(self):
        d.decompress('imagens/sala')
        self.ImagemSala = pygame.image.load('imagens/sala.jpg')
        self.Sala = pygame.transform.scale(self.ImagemSala, (1366, 768))
        self.rectSala = self.Sala.get_rect()


class Cenario():
    def __init__(self):
        self.cama = pygame.image.load('imagens/cama.png')
        self.espelho = pygame.image.load('imagens/espelho.png')
        self.guarda_roupa = pygame.image.load('imagens/guarda-roupa.png')
        self.lareira = pygame.image.load('imagens/lareira.png')
        self.luminaria_a = pygame.image.load('imagens/luminaria_1.png')
        self.luminaria_b = pygame.image.load('imagens/luminaria_2.png')
        self.luminaria_off = pygame.image.load('imagens/luminaria_off.png')
        self.moldura = pygame.image.load('imagens/moldura.png')
        self.poltrona = pygame.image.load('imagens/poltrona.png')
        self.sofa = pygame.image.load('imagens/sofa.png')
        self.vaso = pygame.image.load('imagens/vaso.png')
        self.alavanca_on = pygame.image.load('imagens/alavanca2.png')
        self.alavanca_off = pygame.image.load('imagens/alavanca1.png')
        self.cadeira = pygame.image.load('imagens/cadeira.png')
        self.chave = pygame.image.load('imagens/chave.png')
        self.mesa = pygame.image.load('imagens/mesa.png')
        self.prateleira = pygame.image.load('imagens/prateleira.png')
        self.porta = pygame.image.load('imagens/porta.png')
        self.porta_aberta = pygame.image.load('imagens/porta_aberta.png')
        self.grade = pygame.image.load('imagens/grade.png')
        self.maca = pygame.image.load('imagens/maca.png')
        self.piano = pygame.image.load('imagens/piano.png')
