from __future__ import annotations

import pygame


class CircleShape(pygame.sprite.Sprite):
    def __init__(self, x: float, y: float, radius: float):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position = pygame.Vector2(x, y)
        self.velocity = pygame.Vector2(0, 0)
        self.radius = radius

    def draw(self, surface: pygame.SurfaceType):
        # sub-classes must override
        pass

    def update(self, dt: float):
        # sub-classes must override
        pass

    def collides_with(self, obj: CircleShape) -> bool:
        radii = self.radius + obj.radius
        distance_from_center = self.position.distance_to(obj.position)
        # for debugging
        # if distance_from_center - radii <= -8:
        #     print(f"Radius of self: {self.radius}")
        #     print(f"Radius of obj: {obj.radius}")
        #     print(f"Position of self: {self.position}")
        #     print(f"Position of obj: {obj.position}")
        #     return True
        return distance_from_center - radii <= -8
