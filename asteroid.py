import random
import pygame
from constants import ASTEROID_MIN_RADIUS
from circleshape import *

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.rotation = 0

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position +=  self.velocity * dt

    def split(self):
        self.kill()
        if self.radius > ASTEROID_MIN_RADIUS:
            angle = random.uniform(20, 50)
            rand_angle1 = self.velocity.rotate(angle)
            rand_angle2 = self.velocity.rotate(-angle)

            radius = self.radius - ASTEROID_MIN_RADIUS
            (x, y) = self.position
            a1 = Asteroid(x, y, radius)
            a1.velocity = rand_angle1
            a2 = Asteroid(x, y, radius)
            a2.velocity = rand_angle2
