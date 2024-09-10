import pygame
from constants import PLAYER_RADIUS
from circleshape import CircleShape


class Player(CircleShape):
    def __init__(self, x: int, y: int, rotation: int = 0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = rotation

    def draw(self, surface, color="white", line_width=2):
        pygame.draw.polygon(surface, color, self.triangle(), line_width)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
