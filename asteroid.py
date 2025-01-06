import circleshape, player, constants
import pygame
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white",self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        angle = random.uniform(20, 50)
        ast1 = self.velocity.rotate(angle)
        ast2 = self.velocity.rotate(-angle)
        new_radius = self.radius - constants.ASTEROID_MIN_RADIUS
        gen_ast1 = Asteroid(self.position[0], self.position[1], new_radius)
        gen_ast1.velocity = ast1
        gen_ast2 = Asteroid(self.position[0], self.position[1], new_radius)
        gen_ast2.velocity = ast2