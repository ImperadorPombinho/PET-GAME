import pygame
import pygame
from pygame.locals import *

class Gato(pygame.sprite.Sprite):
    def __init__(self, altura):
        pygame.sprite.Sprite.__init__(self)
        self.altura = altura
        self.sprites = []
        for i in range(1, 4):
            self.sprites.append(pygame.image.load(f'assets/sprites/gato/gato_sprite_{i}.png'))
        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 150
        self.rect.y = self.altura - (self.image.get_height() * 3)

    def update(self):
        self.index += 0.5
        if self.index >= len(self.sprites):
            self.index = 0
        self.image = self.sprites[int(self.index)]
        