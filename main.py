import sys
import pygame
def piirrä(näyttö):
    pygame.draw.circle(näyttö, (200, 200, 0), (250, 250), 80)
    pygame.display.flip()
    pass
pygame.init()  
scr = pygame.display.set_mode((600,500))  
pygame.display.set_caption('Pygame Window')
while True:
    # Näppäimet
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                pass
        if event.type == pygame.KEYUP:
            pass
    piirrä(scr)

