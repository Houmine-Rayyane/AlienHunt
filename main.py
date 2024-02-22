import pygame 
import sys 


pygame.init()

WIDTH , HEIGHT = 400, 600 
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')
Fps = 60
clk = pygame.time.Clock()
game_active = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


pygame.display.update()
clk.tick(Fps)