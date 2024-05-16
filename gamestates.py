import pygame
from player import Player
from enemy import Enemy
class Game:
    def __init__(self):
        self.player = Player()
        self.all_players = pygame.sprite.Group()
        self.all_players.add(self.player)
        self.all_enemies = pygame.sprite.Group()
        self.scene = int(open("Scenes/config/config_scenes.txt","r").read())
        self.font = pygame.font.Font(None, 36)
        
    def spawn_enemy(self):
            enemy = Enemy(self)
            self.all_enemies.add(enemy)
              
    def next_scene(self): 
            self.scene +=1
            with open("Scenes/config/config_scenes.txt", 'w') as fichier_conf:
                fichier_conf.write(str(self.scene)) #conversion en string pour pouvoir l'écrire en format txt
                
    def fight(self, player, enemy):
        player = Player()
        enemy = Enemy()
        while player.health > 0 and enemy.health > 0:
        # Player attacks enemy
            enemy.health -= player.attack

            if enemy.health <= 0:
            # Enemy is defeated
                enemy.kill()
            break  # Exit the loop if enemy is defeated

        # Enemy attacks player
        player.health -= enemy.attack
        if player.health <= 0:
            # Player is defeated
            player.kill()
    def draw_text(self, text,font, color, x, y, surface):
        font = self.font
        text_surface = self.font.render(text, True, (0,0,0))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        surface.blit(text_surface, text_rect)
        
    def start_menu(self, surface , width, height):
        while True:
            surface.fill((255, 255, 255))
            self.draw_text(surface, "Start Game", self.font,(0 , 0, 0 ), width // 2, height // 2)
            self.draw_text(surface, "Options", self.font, (0 , 0, 0 ), width // 2, height // 2 + 50)
            self.draw_text(surface, "Exit", self.font, (0 , 0, 0 ),  width// 2, height // 2 + 100)
            
    def levelup_menu():
        pass