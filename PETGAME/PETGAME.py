import pygame
from pygame.locals import *
from sys import exit
from cenario.chao import Chao
from gato import Gato
from cenario.nuvem import Nuvem
from obstaculo.cerca import Cerca

pygame.init()

largura = 700
altura = 500

size = (largura, altura)

fonte = pygame.font.SysFont('', 35, True, False)

tela = pygame.display.set_mode(size)
pygame.display.set_caption('PETGAME')
AZUL = (142, 211, 243)
PRETO = (0 ,0, 0)
velocidade = 1
posicao_texto = (largura / 2, altura / 2)
loop_principal = True
todas_as_sprites  = pygame.sprite.Group()
gato = Gato(altura)
todas_as_sprites.add(gato)

cerca = Cerca(altura, largura, velocidade)
todas_as_sprites.add(cerca)

lista_obstaculo = [cerca]


for  i in range(4):
    nuv = Nuvem(largura, velocidade)
    todas_as_sprites.add(nuv)

for i in range(largura*2 // 96):
    chao = Chao(i, altura, largura, velocidade)
    todas_as_sprites.add(chao)
score = velocidade
relogio = pygame.time.Clock()
while loop_principal:
    relogio.tick(30)
    tela.fill(AZUL)
    texto_formatado = fonte.render(f'Ponto: {score}', True, PRETO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_SPACE:
                if gato.rect.y == gato.pos_y_inicial:
                    gato.pular()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    tela.blit(texto_formatado, posicao_texto)
    lista_colisao = pygame.sprite.spritecollide(gato, lista_obstaculo, False)
    if len(lista_colisao) > 0:
        print('colidiu')
        lista_colisao.clear()
    else:
        score += 1
    pygame.display.flip()