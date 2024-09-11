from typing import override

import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x: float, y: float, radius: float = SHOT_RADIUS):
        super().__init__(x, y, radius)

    @override
    def draw(self, surface: pygame.SurfaceType):
        pygame.draw.circle(surface, "white", self.position, SHOT_RADIUS)

    @override
    def update(self, dt: float):
        self.position += self.velocity * dt
