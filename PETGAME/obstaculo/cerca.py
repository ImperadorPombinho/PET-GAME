import pygame
from pygame.locals import *
from file import diretorio_images
import os
class Cerca(pygame.sprite.Sprite):
    def __init__(self, altura, largura, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.__altura_da_tela = altura
        self.__largura_da_tela = largura
        self.image = pygame.image.load(os.path.join(diretorio_images ,'sprite_cerca.png'))
        self.rect = self.image.get_rect()
        self.__velocidade_cerca = velocidade * 10
        self.rect.y = self.__altura_da_tela - (self.image.get_height() * 1.4)
        self.rect.x = self.__largura_da_tela
        self.rect.h = self.image.get_height() - 10
        self.rect.w = self.image.get_width() - 10

    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.__largura_da_tela
        self.rect.x -= self.__velocidade_cerca
