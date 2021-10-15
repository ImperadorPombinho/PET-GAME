import pygame


import pygame
from pygame.locals import *

#Colocar nuvens aleatorias
class Nuvem(pygame.sprite.Sprite):
    def __init__(self, largura_tela):
        pygame.sprite.Sprite.__init__(self)
        self.largura = largura_tela
        self.image = pygame.image.load('assets/image/nuvemzinha.png')
        self.rect = self.image.get_rect()
        self.pos_x_inicial = self.largura - self.image.get_width()
        self.rect.x = self.pos_x_inicial
        self.rect.y = 50

    def update(self):
        self.rect.x -= 0.5
        if self.rect.x <= 0:
            self.rect.x = self.pos_x_inicial
        