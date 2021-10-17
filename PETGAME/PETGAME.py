import pygame
from pygame.font import SysFont
from pygame.locals import *
from sys import exit
from cenario.chao import Chao
from gato import Gato
from cenario.nuvem import Nuvem
from obstaculo.cerca import Cerca
global pausou
global recomeca
pygame.init()
todas_as_sprites  = pygame.sprite.Group()
COR_DO_TEXTO = (28 ,31, 66)
fonte = pygame.font.SysFont('', 35, True, False)
largura = 700
altura = 500

size = (largura, altura)

    

tela = pygame.display.set_mode(size)
pygame.display.set_caption('PETGAME')
AZUL = (142, 211, 243)

velocidade = 1
loop_principal = True
score = velocidade   


textos_jogo = {
        'ponto': f'Pontos: {score}',
        'pausou': {
            'texto': 'PAUSADO',
            'ajuda': 'Aperte P para despausar'
        },
        'perdeu': {
            'texto': 'GAME OVER',
            'ajuda': 'Aperte R para reiniciar o jogo'
        }

    }
posicao_texto = {
        'centro': (largura / 2, altura / 2),
        'baixo': ((largura / 2), (altura / 2 + 100)),
        'alto': (largura / 2, (altura / 2 - 100)),
        'lado': (largura - 100, altura - 460)
    }

def jogo_iniciado(score):
    todas_as_sprites.empty()
    gato = Gato(altura)
    todas_as_sprites.add(gato)

    cerca = Cerca(altura, largura, velocidade)
    todas_as_sprites.add(cerca)

    lista_obstaculo = [cerca]

    relogio = pygame.time.Clock()

    for  i in range(4):
        nuv = Nuvem(largura, velocidade)
        todas_as_sprites.add(nuv)

    for i in range(int(largura*2.5) // 96):
        chao = Chao(i, altura, largura, velocidade)
        todas_as_sprites.add(chao)
    
    
    while loop_principal:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if gato.rect.y == gato.pos_y_inicial:
                        gato.pular()
                if event.key == K_p:
                    pausado()
        relogio.tick(30)
        tela.fill(AZUL)
        exibir_mensagem(f'Pontos: {score}', posicao_texto['lado'])
        todas_as_sprites.draw(tela)
        todas_as_sprites.update()   
        lista_colisao = pygame.sprite.spritecollide(gato, lista_obstaculo, False)
        if len(lista_colisao) > 0:
            print('colidiu')
            score = velocidade
            lista_colisao.clear()
            game_over(score)
        else:
            score += 1
        pygame.display.flip()

def definir_texto(texto: str, fonte: SysFont):
    texto_formatado = fonte.render(texto, True, COR_DO_TEXTO)
    return texto_formatado, texto_formatado.get_rect()

def exibir_mensagem(mensagem, posicao):
    texto_formatado, texto_rect = definir_texto(mensagem, fonte)
    texto_rect.center = posicao
    tela.blit(texto_formatado, texto_rect)

def pausado():
    pausou = True
    exibir_mensagem(textos_jogo['pausou']['texto'], posicao_texto['centro'])
    exibir_mensagem(textos_jogo['pausou']['ajuda'], posicao_texto['baixo'])
    todas_as_sprites.update()
    while pausou:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pausou = False
        pygame.display.flip()

def game_over(score):
    recomeca = True
    exibir_mensagem(textos_jogo['perdeu']['texto'], posicao_texto['centro'])
    exibir_mensagem(textos_jogo['perdeu']['ajuda'], posicao_texto['baixo'])
    while recomeca:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    print('recomeçar aqui')
                    recomeca = False
                    jogo_iniciado(score)
        pygame.display.flip()




jogo_iniciado(score)