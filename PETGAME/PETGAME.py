import pygame
from pygame.font import SysFont
from pygame.locals import *
from sys import exit
from obstaculo.patolion import PatoLion
from obstaculo.passaro import Passaro
from cenario.chao import Chao
from Gatos.gato import Gato
from cenario.nuvem import Nuvem
from obstaculo.cerca import Cerca
from random import randint
from file import diretorio_musics
import os

global pausou
global recomeca
pygame.init()
pygame.mixer.init()
todas_as_sprites  = pygame.sprite.Group()
COR_DO_TEXTO = (28 ,31, 66)

largura = 700
altura = 500

size = (largura, altura)

    

tela = pygame.display.set_mode(size)
pygame.display.set_caption('PETGAME')
AZUL = (142, 211, 243)

velocidade = 1

score = velocidade   


textos_jogo = {
        'pausou': {
            'texto': 'PAUSADO',
            'ajuda': 'Aperte P para despausar'
        },
        'perdeu': {
            'texto': 'GAME OVER',
            'ajuda': 'Aperte R para reiniciar o jogo'
        },
        'credito': 'Music: www.bensound.com'

    }
posicao_texto = {
        'centro': (largura / 2, altura / 2),
        'baixo': ((largura / 2), (altura / 2 + 100)),
        'alto': (largura / 2, (altura / 2 - 100)),
        'lado_dir': (largura - 100, altura - 460),
        'lado_esq': (largura - 600, altura - 460)
    }

def obstaculo_aleatorio(passaro: Passaro, cerca: Cerca, pato_lion: PatoLion):
    obstaculo_escolhido = randint(0, 2)
    obstaculo = None
    escolhido = obstaculo_escolhido
    if obstaculo_escolhido == 0:
        obstaculo = passaro
    elif obstaculo_escolhido == 1:
        obstaculo = cerca
    else:
        obstaculo = pato_lion
    return obstaculo, escolhido
def jogo_iniciado(score):
    musica_de_fundo = pygame.mixer.music.load(os.path.join(diretorio_musics, 'bensound-sweet.mp3'))
    pygame.mixer.music.set_volume(0.5)
    pulo = pygame.mixer.Sound(os.path.join(diretorio_musics, 'smb_jump-small.wav'))
    pulo.set_volume(0.8)
    todas_as_sprites.empty()
    gato = Gato(altura)
    todas_as_sprites.add(gato)

    passaro = Passaro(largura, altura, velocidade)
    cerca = Cerca(altura, largura, velocidade)
    pato_lion = PatoLion(largura, altura, velocidade)

    lista_obstaculo = [passaro, cerca, pato_lion]
    obs = obstaculo_aleatorio(passaro, cerca, pato_lion)
    todas_as_sprites.add(obs[0])
    relogio = pygame.time.Clock()

    for  i in range(4):
        nuv = Nuvem(largura, velocidade)
        todas_as_sprites.add(nuv)

    for i in range(int(largura*2.5) // 96):
        chao = Chao(i, altura, largura, velocidade)
        todas_as_sprites.add(chao)
    global loop_principal
    loop_principal = True
    pygame.mixer.music.play(-1)
    while loop_principal:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    if gato.rect.y == gato.pos_y_inicial:
                        gato.pular()
                        pulo.play()
                if event.key == K_p:
                    pausado()
        if pygame.key.get_pressed()[K_LEFT]:
            gato.segurou_pulo()
        else:
            gato.desegurou_pulo()
        relogio.tick(30)
        tela.fill(AZUL)
        exibir_mensagem(f'Pontos: {score}', posicao_texto['lado_dir'],35)
        if score <= 50:
            exibir_mensagem(textos_jogo['credito'], posicao_texto['lado_esq'], 20)
        todas_as_sprites.draw(tela)
        todas_as_sprites.update()   
        lista_colisao = pygame.sprite.spritecollide(gato, lista_obstaculo, False)
        if len(lista_colisao) > 0:
            print('colidiu')
            score = velocidade
            lista_colisao.clear()
            loop_principal = False
            game_over(score)
        else:
            score += 1
        if obs[1] == 0 and obs[0].rect.topright[0] < 0:
            todas_as_sprites.remove(passaro)
            obs = obstaculo_aleatorio(passaro, cerca, pato_lion)
            todas_as_sprites.add(obs[0])
        elif obs[1] == 1 and obs[0].rect.topright[0] < 0:
            todas_as_sprites.remove(cerca)
            obs = obstaculo_aleatorio(passaro, cerca, pato_lion)
            todas_as_sprites.add(obs[0])
        elif obs[1] == 2 and obs[0].rect.topright[0] < 0:
            todas_as_sprites.remove(pato_lion)
            obs = obstaculo_aleatorio(passaro, cerca, pato_lion)
            todas_as_sprites.add(obs[0])
        
        pygame.display.flip()

def definir_texto(texto: str, fonte: SysFont):
    
    texto_formatado = fonte.render(texto, True, COR_DO_TEXTO)
    return texto_formatado, texto_formatado.get_rect()

def exibir_mensagem(mensagem, posicao, num_fonte):
    fonte = pygame.font.SysFont('', num_fonte, True, False)
    texto_formatado, texto_rect = definir_texto(mensagem, fonte)
    texto_rect.center = posicao
    tela.blit(texto_formatado, texto_rect)

def pausado():
    pygame.mixer.music.pause()
    pausou = True
    exibir_mensagem(textos_jogo['pausou']['texto'], posicao_texto['centro'], 35)
    exibir_mensagem(textos_jogo['pausou']['ajuda'], posicao_texto['baixo'], 35)
    todas_as_sprites.update()
    while pausou:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_p:
                    pausou = False
                    pygame.mixer.music.unpause()
        pygame.display.flip()

def game_over(score):
    pygame.mixer.music.pause()
    terminou = pygame.mixer.Sound(os.path.join(diretorio_musics, 'smb_mariodie.wav'))
    terminou.set_volume(0.5)
    recomeca = True
    terminou.play()
    exibir_mensagem(textos_jogo['perdeu']['texto'], posicao_texto['centro'],35)
    exibir_mensagem(textos_jogo['perdeu']['ajuda'], posicao_texto['baixo'],35)
    while recomeca:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            if event.type == KEYDOWN:
                if event.key == K_r:
                    print('recomeçar aqui')
                    terminou.stop()
                    recomeca = False
                    jogo_iniciado(score)
        pygame.display.flip()




jogo_iniciado(score)