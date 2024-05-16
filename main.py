import pygame
from random import*
from player import Player
from enemy import Enemy
from gamestates import Game

pygame.init()
pygame.display.set_caption("MyGame")
background = pygame.image.load("Sprites/Map.png")
width,height = background.get_size()
window = pygame.display.set_mode((width,height), pygame.RESIZABLE)

#appel des classes
player = Player()
enemy = Enemy()
game = Game()

enemies = [enemy]  # Create the enemies list
clock = pygame.time.Clock()
timer = pygame.time.get_ticks()
pygame.font.init()
# boucle principale:
run = True
scene = 0
while run:
        window.blit(background,(0,0))
        #hitbox = pygame.draw.rect(window, rouge, player.hitbox, 2)
        player.update()
        #draw health bar
        player.draw(window)
        #enemy.draw(window)
        window.blit(player.image , player.rect)
        window.blit(enemy.image, enemy.rect)
        window.blit(player.bullet_image, player.bullet_rect)
           
        clock.tick(60)
        pygame.display.flip()
        #Pour quitter le jeu
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
        menu = game.start_menu(window, height, width)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            player.shoot()
        if keys[pygame.K_d] and player.rect.x + player.rect.width < window.get_width():
            player.move_right()
        elif keys[pygame.K_q] and player.rect.x > 0:
            player.move_left()
        elif keys[pygame.K_z] and player.rect.y > 0:
            player.move_up()
        elif keys[pygame.K_s] and player.rect.y + player.rect.width < window.get_height():
            player.move_down()
        for enemy in enemies:
            player.check_collision(enemy)
            game.fight(player, enemy)

        if enemy.rect.x == player.rect.x:
            enemy.velocity = 0
        else: enemy.move()
        player.draw_bullets(window)
        player.move_bullets()
        with open("Scenes/scene_" + str(game.scene) + ".py", "r") as scene:
           exec(scene.read())
                                    
      
        
   

   

   