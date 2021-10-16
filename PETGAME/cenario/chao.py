import pygame
from pygame.locals import *


class Chao(pygame.sprite.Sprite):
    def __init__(self, pos_x, altura, largura, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.velocidade_chao = velocidade * 10
        self.altura_da_tela = altura
        self.largura_da_tela = largura
        self.image = pygame.image.load('assets/image/chao.png')
        self.rect = self.image.get_rect()
        self.rect.x = pos_x * self.image.get_width()
        self.rect.y = self.altura_da_tela - self.image.get_height()
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.largura_da_tela
        self.rect.x -= self.velocidade_chao
        