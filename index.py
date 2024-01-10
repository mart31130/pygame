import pygame
from random import*
from player import Player
from enemy import Enemy
from gamestates import *
pygame.init()

# couleurs et constantes: 
bleu = 0, 0,255
noir = 0,0,0
rouge = 255,0,0
vert = 0,255,0

pygame.display.set_caption("MyGame")
background = pygame.image.load("background.jpg")
largeur,hauteur = background.get_size()
window = pygame.display.set_mode((largeur,hauteur), pygame.RESIZABLE)

#appel des classes
player = Player()
enemy = Enemy()

clock = pygame.time.Clock()
timer = pygame.time.get_ticks()
# boucle principale:
run = True
scene = 0
while run:
        #affichage des images
        window.blit(background,(0,0))
        window.blit(player.image ,player.rect)
        window.blit(enemy.image ,enemy.rect)
        if scene == 0:
                if player.rect.y ==100:
                        scene += 1
                        pygame.image.load("test.png")
              
        clock.tick(60)
        pygame.display.flip()
        #Pour quitter le jeu
        for event in pygame.event.get():
             if event.type == pygame.QUIT:
                 run = False
    #mouvement du joueur
             if event.type == pygame.KEYDOWN:
                player.pressed[event.key] = True
             elif event.type == pygame.KEYUP:
                 player.pressed[event.key] = False
        if player.pressed.get(pygame.K_d) and player.rect.x + player.rect.width < window.get_width():
            player.move_right()
        elif player.pressed.get(pygame.K_q) and player.rect.x > 0 :
            player.move_left()
        elif player.pressed.get(pygame.K_z) and player.rect.y >0: 
                player.move_up()
        elif player.pressed.get(pygame.K_s) and player.rect.y + player.rect.width < window.get_height():
                player.move_down()
   

   

   