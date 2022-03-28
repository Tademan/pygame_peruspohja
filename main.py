import math
import sys
import pygame
def piirrä(näyttö,aika):
    näyttö.fill((255, 255, 255))
    pygame.draw.circle(näyttö, (200, 000, 0), (250, 250), (math.sin(aika/20)+1)*100)
    pygame.display.flip()
    pass
def main():
    pygame.init()
    scr = pygame.display.set_mode((600, 500))
    pygame.display.set_caption('Pygame Window')
    clock = pygame.time.Clock()
    Hiiri = [0, 0, 0]
    aika = 0
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
        piirrä(scr,aika)
        aika += 1
        clock.tick(60)
        if pygame.mouse.get_pressed()[0]:
            if Hiiri[0]:
                Hiiri[0] = 0
                pass
        else:
            Hiiri[0] = 1

if __name__ == "__main__":
    main()


