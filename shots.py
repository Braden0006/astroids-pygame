import pygame

from circleshape import CircleShape
from constants import SHOT_RADIUS
from math import pow

class Shot(CircleShape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
        self.rotation = 0
        position = pygame.Vector2(self.x, self.y)
        velocity = pygame.Vector2(0, 0)

        super().__init__(position, velocity, SHOT_RADIUS)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt
