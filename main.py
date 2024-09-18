import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    update_group = pygame.sprite.Group()
    draw_group = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (update_group, draw_group)
    Asteroid.containers = (asteroids, update_group, draw_group)
    Shot.containers = (shots, update_group, draw_group)
    AsteroidField.containers = (update_group)

    asteroid_field = AsteroidField()

    dt = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for obj in update_group:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.check_collision(player):
                print("Game over!")
                exit(0)
        for shot in shots:
            for asteroid in asteroids:
                if asteroid.check_collision(shot):
                    asteroid.split()
                    shot.kill()

        screen.fill("black")

        for obj in draw_group:
            obj.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()
