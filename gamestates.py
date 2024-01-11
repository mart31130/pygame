import pygame
from player import Player

enemy = Enemy()
enemies = [enemy]  # Create the enemies list        
    def collide(self,enemy,enemy_list):
            if self.rect.colliderect(enemy.rect):  # Tests if the player is touching an enemy
                enemy_list.remove(enemy)  # Removes the enemy from the enemy list (Explained lower)
