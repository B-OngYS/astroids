from circleshape import CircleShape
import pygame
import random
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            surface=screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=2,
        )

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        split_angle = random.uniform(20, 50)
        new_vel1 = self.velocity.rotate(split_angle)
        new_vel2 = self.velocity.rotate(-split_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        new_ast1 = Asteroid(self.position.x, self.position.y, radius=new_radius)  # type: ignore
        new_ast1.velocity = new_vel1 * 1.2
        new_ast2 = Asteroid(self.position.x, self.position.y, radius=new_radius)  # type: ignore
        new_ast2.velocity = new_vel2 * 1.2
