import pygame
from pygame.locals import *
from sys import exit
from cenario.chao import Chao
from gato import Gato
from cenario.nuvem import Nuvem

pygame.init()

largura = 700
altura = 500

size = (largura, altura)

tela = pygame.display.set_mode(size)
pygame.display.set_caption('PETGAME')
BRANCO = (255, 255, 255)
velocidade = 1
loop_principal = True
todas_as_sprites  = pygame.sprite.Group()
nuv = Nuvem(largura, velocidade)
gato = Gato(altura)
todas_as_sprites.add(nuv)
todas_as_sprites.add(gato)
for i in range(largura*2 // 96):
    chao = Chao(i, altura, largura, velocidade)
    todas_as_sprites.add(chao)

relogio = pygame.time.Clock()
while loop_principal:
    relogio.tick(30)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()