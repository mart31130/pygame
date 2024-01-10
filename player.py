import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.health = 50
        self.max_health = 50
        self.attack = 10
        self.image = pygame.image.load("player.png")
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 170
        self.velocity =5
        self.pressed = {}
        
    #deplacement du joueur
    def move_right(self):
        self.rect.x +=self.velocity
    def move_left(self):
        self.rect.x -= self.velocity
    def move_up(self):
        self.rect.y -= self.velocity
    def move_down(self):
        self.rect.y +=self.velocity
    def jump(self):
        pass