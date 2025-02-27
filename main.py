from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shots import Shot
import pygame
import sys

def main():
    pygame.init()
    # defining initial player position vector
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    # defining the game groups
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatables, drawables)
    Asteroid.containers = (updatables, drawables, asteroids)
    AsteroidField.containers = (updatables)
    Shot.containers = (updatables, drawables, shots)
    player = Player(x, y, PLAYER_RADIUS)
    asteroid_field = AsteroidField()
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    time = pygame.time.Clock()
    dt = 0
    #defining the game-loop
    while True:
        font = pygame.font.Font(None, 36)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        for updatable in updatables:
            updatable.update(dt)
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collision(asteroid):
                    bullet.kill()
                    asteroid.split()
                    player.up_score()
            if asteroid.collision(player):
                player.decrement_health()
                #if player.health < 0:
                 #   sys.exit()
        for drawable in drawables:
            drawable.draw(screen)
        # Draw score to the screen
        score_text = font.render(f'Score: {player.health}', True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        pygame.display.flip()
        mls = time.tick(60)
        dt = mls/1000
if __name__ == "__main__":
    main()
