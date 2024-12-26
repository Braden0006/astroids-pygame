import pygame
import random

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, PLAYER_RADIUS
from math import pow

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        random_angle = random.uniform(20, 50)

        asteroid1 = self.velocity.rotate(random_angle)
        asteroid2 = self.velocity.rotate(-random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = asteroid1 * 1.2
        asteroid = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid.velocity = asteroid2 * 1.2