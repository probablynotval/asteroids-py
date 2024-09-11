from typing import override

import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, surface: pygame.SurfaceType):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        shard_radius = self.radius - ASTEROID_MIN_RADIUS
        random_angle = random.uniform(20, 50)

        shard_1 = Asteroid(self.position.x, self.position.y, shard_radius)
        shard_1_angle = self.velocity.rotate(random_angle)
        shard_1.velocity = shard_1_angle * 1.2

        shard_2 = Asteroid(self.position.x, self.position.y, shard_radius)
        shard_2_angle = self.velocity.rotate(-random_angle)
        shard_2.velocity = shard_2_angle * 1.2
