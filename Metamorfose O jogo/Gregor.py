import pygame
import decompress as d


class Gregor:
    def __init__(self):
        self.pngGregor = pygame.image.load('imagens/Gregor.png')
        self.Gregor = pygame.image.load('imagens/GregorV1.png')
        self.GregorDireita = []
        self.GregorEsquerda = []
        self.GregorCima = []
        self.GregorBaixo = []
        self.GregorEntrando = []
        self.GregorSaindo = []

        self.GregorDireita.append(self.pngGregor.subsurface(134, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(263, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(402, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(546, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(690, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(834, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(968, 0, 134, 217))
        self.GregorDireita.append(self.pngGregor.subsurface(1107, 0, 99, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(134, 232, 124, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(256, 232, 134, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(394, 232, 134, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(532, 232, 134, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(685, 232, 134, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(828, 232, 134, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(973, 232, 134, 217))
        self.GregorEsquerda.append(self.pngGregor.subsurface(1102, 232, 104, 217))
        self.GregorCima.append(self.pngGregor.subsurface(0, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(134, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(268, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(402, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(541, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(675, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(819, 432, 134, 217))
        self.GregorCima.append(self.pngGregor.subsurface(968, 432, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(0, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(134, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(268, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(402, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(541, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(675, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(819, 649, 134, 217))
        self.GregorBaixo.append(self.pngGregor.subsurface(968, 649, 134, 217))
        self.GregorEntrando.append(self.pngGregor.subsurface(0, 0, 134, 217))
        self.GregorSaindo.append(self.pngGregor.subsurface(0, 217, 134, 217))


class Bg():
    def __init__(self):
        d.decompress('imagens/quarto')
        self.ImagemSala = pygame.image.load('imagens/quarto.jpg')
        self.Quarto = pygame.transform.scale(self.ImagemSala, (1366, 768))
        self.rectQuarto = self.Quarto.get_rect()


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
