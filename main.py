import pygame 
import sys 
from random import randint


pygame.init()

WIDTH , HEIGHT = 400, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
Fps = 60
clk = pygame.time.Clock()
game_active = True

#game background
space_surf = pygame.image.load('pics/space.png')

#Allien hunter
allien_hunter = pygame.image.load('pics/Hero.png')
ah_rect = allien_hunter.get_rect(midbottom =(200,600))

#Enemies
alien1 = pygame.image.load('pics/alien.png')
a1_rect = alien1.get_rect(midtop =(50,10))
alien2 = pygame.image.load('pics/alien2.png')
a2_rect = alien2.get_rect(midtop =(200,10))

def move(keys_pressed, ah_rect):
    if keys_pressed[pygame.K_LEFT] and ah_rect.x > -20:
      ah_rect.x -=5   
    elif keys_pressed[pygame.K_RIGHT] and ah_rect.x  < WIDTH -105  :
      ah_rect.x +=5  

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    
            
    if game_active:
        screen.blit(space_surf,(0,0))
        screen.blit(allien_hunter, ah_rect)
        screen.blit(alien1,a1_rect)
        screen.blit(alien2,a2_rect)
        a1_rect.y += 3
        a2_rect.y +=3
        if a1_rect.y > 650 and a2_rect.y > 650 :
            a1_rect.y = -10
            a2_rect.y = -10
            a1_rect.x = randint(0,350)
            a2_rect.x = randint(0,300)
            
    
    keys_pressed= pygame.key.get_pressed()        
    move(keys_pressed, ah_rect)        
    pygame.display.update()
    clk.tick(Fps)