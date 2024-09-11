from typing import override

import pygame
from constants import (
    PLAYER_RADIUS,
    PLAYER_SPEED,
    PLAYER_TURN_SPEED,
    PLAYER_SHOT_SPEED,
    PLAYER_SHOOT_COOLDOWN,
)
from circleshape import CircleShape
from shot import Shot


class Player(CircleShape):
    def __init__(self, x: float, y: float, rotation: float = 0):
        super().__init__(x, y, PLAYER_RADIUS)
        self.rotation = rotation
        self.shoot_cooldown = 0

    @override
    def draw(self, surface, color="white", line_width=2):
        pygame.draw.polygon(surface, color, self.triangle(), line_width)

    @override
    def update(self, dt: float):
        self.shoot_cooldown -= dt

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt: float):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt: float):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += dt * forward * PLAYER_SPEED

    def shoot(self):
        if self.shoot_cooldown > 0:
            print(f"On cooldown! {self.shoot_cooldown}s")
            return

        shot = Shot(self.position.x, self.position.y, self.radius)
        shot.velocity = pygame.Vector2(0, 1).rotate(self.rotation) * PLAYER_SHOT_SPEED
        self.shoot_cooldown = PLAYER_SHOOT_COOLDOWN
