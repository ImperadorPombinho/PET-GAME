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
        self.rect.h = self.image.get_height() - 30
        self.rect.w = self.image.get_width() - 30
        self.__tamanho_do_pulo = 15
        self.__tamanho_do_pulo_segurado = 8
        self.__pulou = False
        self.__limite_de_pulou = 204
        self.__segurou_pulo = False

    def pular(self):
        self.__pulou = True

    def segurou_pulo(self):
        self.image = self.__sprites[1]
        self.__segurou_pulo = True
    def desegurou_pulo(self):
        self.__segurou_pulo = False
    
    @property
    def pos_y_inicial(self):
        return self.__pos_y_inicial
    
    def update(self):
        self.__index += 0.5
        if self.__index >= len(self.__sprites):
            self.__index = 0
        self.image = self.__sprites[int(self.__index)]

        if self.__pulou:
            self.rect.y -= self.__tamanho_do_pulo
            self.image = self.__sprites[1]
            if self.rect.y <= self.__limite_de_pulou:
                self.__pulou = False
        else:
            if self.__segurou_pulo:
                self.rect.y += self.__tamanho_do_pulo_segurado
                if self.rect.y >= self.__pos_y_inicial:
                    self.rect.y = self.__pos_y_inicial
                    self.__segurou_pulo = False
            else:
                self.image = self.__sprites[1]
                self.rect.y += self.__tamanho_do_pulo
                if self.rect.y >= self.__pos_y_inicial:
                    self.rect.y = self.__pos_y_inicial
                    self.image = self.__sprites[int(self.__index)]
        


    