import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

SCREEN_SIZE = (SCREEN_WIDTH, SCREEN_HEIGHT)


def main():
    pygame.init()
    screen = pygame.display.set_mode(SCREEN_SIZE)
    clock = pygame.time.Clock()
    dt: float = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill("black")
        for obj in drawable:
            obj.draw(screen)
        for obj in updatable:
            obj.update(dt)
        pygame.display.flip()

        dt: float = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
