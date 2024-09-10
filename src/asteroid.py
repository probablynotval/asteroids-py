from typing import override

import pygame
from circleshape import CircleShape


class Asteroid(CircleShape):
    def __init__(self, x: float, y: float, radius: float):
        super().__init__(x, y, radius)

    @override
    def draw(self, surface: pygame.SurfaceType):
        pygame.draw.circle(surface, "white", self.position, self.radius, 2)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt
