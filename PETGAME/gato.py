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
        self.pulou = False
        self.limite_de_pulou = 204
        self.limitePulo = False
        self.jumpPower = 10
        self.terminalVelocity = 24
        self.fallingSpeed = 0

    def pular(self):
        self.pulou = True
    
    def despular(self):
        self.pulou = False

    @property
    def pos_y_inicial(self):
        return self.__pos_y_inicial
    
    def update(self):
        if self.rect.y <= self.limite_de_pulou:
            self.despular()
        if self.pulou and self.limitePulo == False:
            self.fallingSpeed = self.fallingSpeed + (self.jumpPower/3)
            if self.fallingSpeed < -1 * self.jumpPower:
                self.fallingSpeed = self.jumpPower
            self.rect.y -= self.fallingSpeed
            if self.rect.y <= self.limite_de_pulou:
                self.limitePulo = True
                self.fallingSpeed = -2
        else:
            self.rect.y += self.fallingSpeed
            self.fallingSpeed = self.fallingSpeed + (self.terminalVelocity/20)
            if self.fallingSpeed > self.terminalVelocity:
                self.fallingSpeed = self.terminalVelocity
            if self.pulou and self.fallingSpeed > self.terminalVelocity / 3:
                self.fallingSpeed = self.terminalVelocity / 3
            if self.rect.y >= self.pos_y_inicial:
                self.limitePulo = False
                self.rect.y = self.__pos_y_inicial

        self.__index += 0.5
        if self.__index >= len(self.__sprites):
            self.__index = 0
        self.image = self.__sprites[int(self.__index)]
    