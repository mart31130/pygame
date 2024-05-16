import pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.health = 50
        self.max_health = 50
        self.health_bar_length = 400
        self.health_ratio = self.max_health/self.health_bar_length
        self.attack = 10
        self.bullets = []
        self.bullet_image = pygame.Surface((10, 30))
        self.bullet_image.fill((255,0,0))
        self.bullet_rect = self.bullet_image.get_rect()
        #self.image = pygame.image.load("Sprites/player.png")
        self.image = pygame.Surface((60, 60))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = 200
        self.rect.y = 170
        self.velocity =5
        self.pressed = {}
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        
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
    
    #position du joueur
    def get_position(self):
        return (self.rect.x, self.rect.y)
    
    def death(self):
        if self.health <= 0:
            font = pygame.font.Font(None, 36)
            text = font.render('VOUS ÊTES MORTS', True, (255,0,0))
            return text
        
    def check_collision(self, enemy):
         return pygame.sprite.collide_rect(self, enemy)
         
    def update(self):
        self.hitbox = pygame.Rect(self.rect.x, self.rect.y, self.rect.width, self.rect.height)
        
    def draw(self, surface):
        pygame.draw.rect(surface, (255,0,0),(10,10,self.health/self.health_ratio,15))
        pygame.draw.rect(surface,(0,255,0),(10,10, self.health_bar_length,15),4)
        
    def draw_bullets(self,surface):
        for bullet in self.bullets:
            pygame.draw.rect(surface, (255,0,0), bullet)
            
    def  move_bullets(self):
        for bullet in self.bullets:
                bullet.y -= 5 
    def shoot(self):
        self.bullet_rect.center = self.rect.center
        

            

 
 