import pygame
import player
from constants import *


def main():

    #initialize pygame
    pygame.init()
    #create a screen object based on the values in constants.py
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: " + str(SCREEN_WIDTH))
    print(f"Screen height: " + str(SCREEN_HEIGHT))

    #game clock
    game_clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    player.Player.containers = (updatable, drawable)    
    player_one = player.Player((SCREEN_WIDTH / 2),(SCREEN_HEIGHT / 2))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0))
        dt = (game_clock.tick(60) / 1000)
        for item_update in updatable:
            item_update.update(dt)
        for item_draw in drawable:
            item_draw.draw(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()