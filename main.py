from constants import *
import pygame

if __name__ == "__main__":
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #handle event logic
    def handle_events():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
    #defining the game-loop
    while True:
        handle_events()
        screen.fill((0, 0, 0))
        pygame.display.flip()     
