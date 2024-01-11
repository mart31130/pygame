import pygame
from random import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.health = 50
        self.max_health = 50
        self.attack = 10
        self.image = pygame.image.load("enemy.png")
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 170
        self.velocity =5
        self.position_x = randint(0,(400-self.rect.width))
        self.position_y = randint(0.300)
    def move(self):
        if self.rect.x <self.position_x:
            self.rect.x+=self.velocity
        elif self.rect.x >self.position_x:
            self.rect.x-=self.velocity
        if self.rect.y <self.position_y:
            self.rect.y+=self.velocity
        elif self.rect.y >self.position_y:
            self.rect.y-=self.velocity  
