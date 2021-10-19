import pygame
from pygame.locals import *
from random import randrange
class Passaro(pygame.sprite.Sprite):
    def __init__(self, largura, altura, velocidade):
        pygame.sprite.Sprite.__init__(self)
        self.__largura_da_tela = largura
        self.__altura_da_tela = altura
        self. __sprites = []
        for i in range(1, 4):
            self.__sprites.append(pygame.image.load(f'assets/sprites/passaro/passaro_sprite_{i}.png'))
        self.__velocidade_do_passaro = velocidade * 10
        self.__index = 0
        self.image = self.__sprites[self.__index]
        self.rect = self.image.get_rect()
        self.rect.x = self.__largura_da_tela - 96
        self.__pos_chao = self.__altura_da_tela - 96
        self.rect.y = randrange(380, self.pos_chao, 50)
        self.rect.h = self.image.get_height() - 20
        self.rect.w = self.image.get_width() - 20

    @property
    def pos_chao(self):
        return self.__pos_chao
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = self.__largura_da_tela
            self.rect.y = randrange(350, self.pos_chao, 50)
        self.rect.x -= self.__velocidade_do_passaro
        self.__index += 0.5
        if self.__index >= len(self.__sprites):
            self.__index = 0
        self.image = self.__sprites[int(self.__index)]