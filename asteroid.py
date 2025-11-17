import random

import pygame

from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS, LINE_WIDTH
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        return pygame.draw.circle(
            screen, "white", self.position, self.radius, LINE_WIDTH
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        angle = random.uniform(20, 50)
        position = self.position
        x = position[0]
        y = position[1]
        asteroid_one_angle = pygame.math.Vector2.rotate(self.velocity, angle)
        asteroid_two_angle = pygame.math.Vector2.rotate(self.velocity, -abs(angle))
        rad = self.radius - ASTEROID_MIN_RADIUS
        asteroid_one = Asteroid(x, y, rad)
        asteroid_two = Asteroid(x, y, rad)
        asteroid_one.velocity = asteroid_one_angle * 1.2
        asteroid_two.velocity = asteroid_two_angle * 1.2
