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

#Enemies
alien = pygame.image.load('pics/alien.png').convert_alpha()
aliens_list = []
#enemies respawn
ALIENS_TIMER = pygame.USEREVENT + 1
pygame.time.set_timer(ALIENS_TIMER,700)

#Border 
border = pygame.Rect(0,50,WIDTH, 5)

#Health 
heart = pygame.image.load('pics/health.png').convert_alpha()
heart_rect = heart.get_rect(midtop = (380,5))

#Bullets 
bullets = []

# Hitting the alliens
#A1_HIT = pygame.USEREVENT + 1
#A2_HIT = pygame.USEREVENT + 2

bullet_sound = pygame.mixer.Sound('audio/bulletsound.mp3')
space_sound = pygame.mixer.Sound('audio/spacesound.mp3')

game_active = True


'''def aliens_move(enemy_list):
    if enemy_list:
        for enemy in enemy_list:
            enemy.y += 3
            screen.blit(alien,enemy)
        enemy_list = [enemy for enemy in enemy_list if enemy.y > 700]
        return enemy_list
    else:
        return []'''
        
def handle_aliens(aliens_list):
    # Spawn new aliens periodically
    x = randint(0, WIDTH - alien.get_width())  # Random X position
    y = 60  # Fixed Y position
    new_alien_rect = alien.get_rect(midtop=(x, y))
    aliens_list.append(new_alien_rect)

def shoot(bullets,ah_rect):
    for bullet in bullets:
        bullet.y -=15
        '''if a1_rect.colliderect(bullet):
            pygame.event.post(pygame.event.Event(A1_HIT))
            bullets.remove(bullet)'''

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
            handle_aliens(aliens_list)
        
        
    if game_active:
        screen.blit(space_surf,(0,0))
        screen.blit(allien_hunter, ah_rect)
        screen.blit(heart, heart_rect)
        pygame.draw.rect(screen,'black', border)
        # Update positions of aliens in the list
        for alien_rect in aliens_list:
            screen.blit(alien, alien_rect)
            alien_rect.y += 3
        #Spaceship bullets
        for bullet in bullets:
            pygame.draw.rect(screen,'red',bullet)
                             
     
    keys_pressed= pygame.key.get_pressed()        
    move_spaceship(keys_pressed, ah_rect)     
    shoot(bullets,ah_rect)
    pygame.display.update()
    clk.tick(Fps)