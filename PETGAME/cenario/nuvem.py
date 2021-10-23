import pygame
from pygame.locals import *
from random import randrange
from file import diretorio_images
import os

class Nuvem(pygame.sprite.Sprite):
    def __init__(self, largura_tela, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.velocidade_nuvem = velocidade * 6
        self.largura = largura_tela
        self.image = pygame.image.load(os.path.join(diretorio_images , 'nuvemzinha.png'))
        self.rect = self.image.get_rect()
        self.pos_x_inicial = self.largura - self.image.get_width()
        self.rect.x = self.largura - randrange(96, 200, 96)
        self.rect.y = randrange(50, 200, 50)

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.largura
            self.rect.y = randrange(50, 200, 50)
        self.rect.x -= self.velocidade_nuvem

        