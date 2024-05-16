import pygame
from random import *
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.health = 50
        self.max_health = 50
        self.health_bar_length = 150
        self.health_ratio = self.max_health/self.health_bar_length
        self.attack = 10
        #self.image = pygame.image.load("Sprites/monster.png")
        self.image = pygame.Surface((40, 40))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = 450
        self.rect.y = 150
        self.velocity = 0.5
        self.all_monsters = pygame.sprite.Group()  
          
    def move(self):
        self.rect.x -=self.velocity
    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0),(10,10,self.health/self.health_ratio,15))
        pygame.draw.rect(surface,(0,255,0),(10,10, self.health_bar_length,15),4)
