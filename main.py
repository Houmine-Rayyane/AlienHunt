import pygame 
from pygame import mixer
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
allien_hunter = pygame.image.load('pics/Hero.png').convert_alpha()
ah_rect = allien_hunter.get_rect(midbottom =(200,600))
ah_mask = pygame.mask.from_surface(allien_hunter)

#Enemies
alien = pygame.image.load('pics/alien.png').convert_alpha()
aliens_list = []
almasks_list = []

#enemies respawn
ALIENS_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(ALIENS_TIMER,500)

#Border 
border = pygame.Rect(0,50,WIDTH, 5)

#Health 
heart = pygame.image.load('pics/health.png').convert_alpha()
heart_rect = heart.get_rect()
health = 5

#Bullets 
bullets = []

# Hitting the alliens
#A1_HIT = pygame.USEREVENT + 1
#A2_HIT = pygame.USEREVENT + 2

bullet_sound = pygame.mixer.Sound('audio/bulletsound.mp3')
game_active = True
        
def handle_aliens(aliens_list,almasks_list):
    # Spawn new aliens periodically
    x = randint(0, WIDTH - alien.get_width())  # Random X position
    y = 60  # Fixed Y position
    new_alien_rect = alien.get_rect(midtop=(x, y))
    aliens_list.append(new_alien_rect)
    almasks_list.append(pygame.mask.from_surface(alien))

def shoot(bullets):
    for bullet in bullets:
        bullet.y -=15
        #Check for aliens/bullet collisions
        for alien_rect, alien_mask in zip(aliens_list,almasks_list):
            if alien_rect.collidepoint(bullet.x, bullet.y):
                aliens_list.remove(alien_rect)
                almasks_list.remove(alien_mask)
                bullets.remove(bullet)
                
                
def move_spaceship(keys_pressed, ah_rect):
    if keys_pressed[pygame.K_LEFT] and ah_rect.x > - 20:
      ah_rect.x -=5   
    elif keys_pressed[pygame.K_RIGHT] and ah_rect.x  < WIDTH - 105  :
      ah_rect.x +=5  
      
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        #Shooting event   
        if event.type==pygame.KEYDOWN :
            if event.key == pygame.K_SPACE:
                bullet_sound.play()
                bullet=pygame.Rect(ah_rect.x + ah_rect.width//2 -2,ah_rect.y, 5 , 10)
                bullets.append(bullet)
        #Respawning event        
        if event.type == ALIENS_TIMER:
            handle_aliens(aliens_list, almasks_list)
        
        
    if game_active:
        screen.blit(space_surf,(0,0))
        screen.blit(allien_hunter, ah_rect)
        pygame.draw.rect(screen,'black', border)
        
        #Drawing hearts at the top of the window
        for i in range(health):
            screen.blit(heart,(10+ (heart_rect.width + 10) * i, 10))
        
        # Update positions of aliens in the list
        # Getting familiar with the built-in function  "zip"
        for alien_rect, alien_mask in zip(aliens_list,almasks_list):
            screen.blit(alien, alien_rect)
            alien_rect.y += 6
            if ah_mask.overlap(alien_mask,(alien_rect.x - ah_rect.x, alien_rect.y - ah_rect.y)):
                health -=1
                aliens_list.remove(alien_rect)
                almasks_list.remove(alien_mask)
                if health <= 0:
                    game_active = False
                    
        #Spaceship bullets
        for bullet in bullets:
            pygame.draw.rect(screen,'red',bullet)
    else:
        screen.blit(space_surf,(0,0))
                       
     
    keys_pressed= pygame.key.get_pressed()        
    move_spaceship(keys_pressed, ah_rect)     
    shoot(bullets)
    pygame.display.update()
    clk.tick(Fps)