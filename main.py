from constants import *
import pygame

def main():
    pygame.init()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    #defining the game-loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        pygame.display.flip()
        mls = time.tick(60)
        dt = mls/1000
if __name__ == "__main__":
    main()
