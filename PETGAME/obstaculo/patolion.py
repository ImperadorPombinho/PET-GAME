import pygame
from pygame.locals import *

class PatoLion(pygame.sprite.Sprite):
    def __init__(self, largura, altura, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.__largura_da_tela = largura
        self.__altura_da_tela = altura
        self.__sprites = []
        for i in range(1, 4):
            self.__sprites.append(pygame.image.load(f'assets/sprites/patolion/sprite_leao_pato_{i}.png'))

        self.__index = 0
        self.__velocidade_lion = velocidade * 10
        self.image = self.__sprites[self.__index]
        self.rect = self.image.get_rect()
        self.rect.x = self.__largura_da_tela
        self.rect.y = self.__altura_da_tela - 96
        self.rect.h = self.image.get_height() - 30
        self.rect.w = self.image.get_width() - 30
    
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.__largura_da_tela
        self.rect.x -= self.__velocidade_lion
        self.__index += 0.5
        if self.__index >= len(self.__sprites):
            self.__index = 0
        self.image = self.__sprites[int(self.__index)]
        