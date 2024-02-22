import pygame 
import sys 
from random import randint


pygame.init()

#Drawing the window
WIDTH , HEIGHT = 400, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('AlienHunt')
game_icon = pygame.image.load('pics/alien.png')
pygame.display.set_icon(game_icon)
Fps = 60
clk = pygame.time.Clock()
#game background
space_surf = pygame.image.load('pics/space.png')
scoreact_font = pygame.font.Font('fonts/gamefont.ttf',20)
scoreinact_font = pygame.font.Font('fonts/gamefont.ttf',40)

#Allien hunter
allien_hunter = pygame.image.load('pics/Hero.png')
ah_rect = allien_hunter.get_rect(midbottom =(200,600))

#Enemies
alien = pygame.image.load('pics/alien.png')
a1_rect = alien.get_rect(midtop =(randint(30,200),50))
a2_rect = alien.get_rect(midtop =(randint(210,370),50))

#Border 
border = pygame.Rect(0,50,WIDTH, 5)

#Health 
heart = pygame.image.load('pics/health.png')
heart_rect = heart.get_rect(midtop = (380,5))

#Bullets 
bullets = []

game_active = True

def shoot(bullets,ah_rect):
    for bullet in bullets:
        bullet.y -=15
        


def move_spaceship(keys_pressed, ah_rect):
    if keys_pressed[pygame.K_LEFT] and ah_rect.x > -20:
      ah_rect.x -=5   
    elif keys_pressed[pygame.K_RIGHT] and ah_rect.x  < WIDTH -105  :
      ah_rect.x +=5  
      

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        if event.type==pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                bullet=pygame.Rect(ah_rect.x + ah_rect.width//2 -2,ah_rect.y, 5 , 10)
                bullets.append(bullet)
            
    if game_active:
        screen.blit(space_surf,(0,0))
        screen.blit(allien_hunter, ah_rect)
        screen.blit(alien,a1_rect)
        screen.blit(alien,a2_rect)
        screen.blit(heart, heart_rect)
        pygame.draw.rect(screen,'black', border)
        
        for bullet in bullets:
            pygame.draw.rect(screen,'red',bullet)
            
        a1_rect.y += 3       
        a2_rect.y += 3
        if a1_rect.y > 650 and a2_rect.y > 650 :
            if a1_rect.x != a2_rect.x:
                a1_rect.y = 50
                a2_rect.y = 50
                a1_rect.x = randint(30,200)
                a2_rect.x = randint(210,370)
    
           
    
    keys_pressed= pygame.key.get_pressed()        
    move_spaceship(keys_pressed, ah_rect)     
    shoot(bullets,ah_rect)
    pygame.display.update()
    clk.tick(Fps)