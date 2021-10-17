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
        self.pulou = False
        self.limite_de_pulou = 204

    def pular(self):
        self.pulou = True

    @property
    def pos_y_inicial(self):
        return self.__pos_y_inicial
    
    def update(self):
        if self.pulou:
            self.rect.y -= 12
            if self.rect.y <= self.limite_de_pulou:
                self.pulou = False
        else:
            self.rect.y += 4.8
            if self.rect.y >= self.pos_y_inicial:
                self.rect.y = self.__pos_y_inicial

        self.__index += 0.5
        if self.__index >= len(self.__sprites):
            self.__index = 0
        self.image = self.__sprites[int(self.__index)]
    