import pygame
import Annie
import Gregor

FPS = 30
largura = 1366
altura = 768
player = Annie.Annie()
cenario = Annie.Cenario()
background = Annie.Bg()
gplayer = Gregor.Gregor()
gcenario = Gregor.Cenario()
gbackground = Gregor.Bg()
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Metamorfose - O jogo")
gravidade = 37
xAnnie = largura/2
yAnnie = 300
xGregor = 10
yGregor = altura - 250
velX = 0
gvelX = 0
gvelY = 0
tela_a = False
a = False
tela_b = False
tela_c = False
tela_d = False
d = False
tela_e = False
tela_f = False
direita = False
esquerda = False
ePulo = False
dPulo = False
bPulo = False
rodando = True
gdireita = False
gesquerda = False
cima = False
baixo = False
alavanca = False
alavanca_off = False
key = False
maca = 0
maca_a = 1290
maca_y = 0
macaVely = 0
macaVel = 0
macaVel_a = 0
pulo = -2.5
sPulo = 0
spritemov = 0
spriteg = 0
newx = 134
newy = 236
clock = pygame.time.Clock()
