import pygame
from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
import sys

from shots import Shot

def main():
    pygame.init()

    fps = pygame.time.Clock()
    dt = 0

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable_group = pygame.sprite.Group()
    drawable_group = pygame.sprite.Group()
    asteroids_group = pygame.sprite.Group()
    shot_group = pygame.sprite.Group()

    Player.containers = (updatable_group, drawable_group)
    Asteroid.containers = (asteroids_group, updatable_group, drawable_group)
    AsteroidField.containers = (updatable_group)
    Shot.containers = (shot_group, updatable_group, drawable_group)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # player.update(dt)
        for thing in updatable_group:
            thing.update(dt)

        for asteroid in asteroids_group:
            if asteroid.collides(player):
                sys.exit("Game over!")

            for bullet in shot_group:
                if asteroid.collides(bullet):
                    bullet.kill()
                    asteroid.split()

        screen.fill("black")

        for thing in drawable_group:
            thing.draw(screen)

        pygame.display.flip()

        fps.tick(60)

        dt = fps.tick(60) / 1000

if __name__ == "__main__":
    main()
