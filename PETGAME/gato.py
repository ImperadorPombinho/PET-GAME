import pygame
import pygame
from pygame.locals import *

class Gato(pygame.sprite.Sprite):
    def __init__(self, altura):
        pygame.sprite.Sprite.__init__(self)
        self.__altura = altura
        self.__sprites = []
        for i in range(1, 4):
            self.__sprites.append(pygame.image.load(f'assets/sprites/gato/gato_sprite_{i}.png'))
        self.__index = 0
        self.image = self.__sprites[self.__index]
        self.rect = self.image.get_rect()
        self.__pos_y_inicial = self.__altura - 96
        self.rect.x = 100
        self.rect.y = self.__pos_y_inicial

    @property
    def pos_y_inicial(self):
        return self.__pos_y_inicial
    
    def update(self):
        self.__index += 0.5
        if self.__index >= len(self.__sprites):
            self.__index = 0
        self.image = self.__sprites[int(self.__index)]
    