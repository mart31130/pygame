# class enemy
class Ennemy(object):
    def __init__(self):
        self.rect = rect1
        self.x = 0
        self.y = 0

    def move(self):
        self.rect.move_ip(0, -1)

    def draw(self, surface):
        pygame.draw.rect(surface, (100, 100, 100), self.rect)

enemy = Enemy()
enemies = [enemy]  # Create the enemies list

def collide(self,enemy,enemy_list):
    if self.rect.colliderect(enemy.rect):  # Tests if the player is touching an enemy
        enemy_list.remove(enemy)  # Removes the enemy from the enemy list (Explained lower)


si rect player touche rect_obj
	recupérer obj