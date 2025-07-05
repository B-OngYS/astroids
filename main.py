import pygame
from constants import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    switch = True
    while switch:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(color="black")
        pygame.display.flip()
        delta = clock.tick(60)
        dt = delta / 1000


if __name__ == "__main__":
    main()
