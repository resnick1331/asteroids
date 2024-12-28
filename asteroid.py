import pygame
from constants import *
from circleshape import CircleShape
import random

# Base class for asteroid
class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position,self.radius,2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            asteroid_one = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid_one.velocity = pygame.math.Vector2.rotate(self.velocity, angle) * 1.2
            asteroid_two = Asteroid(self.position.x, self.position.y, (self.radius - ASTEROID_MIN_RADIUS))
            asteroid_two.velocity = pygame.math.Vector2.rotate(self.velocity, -angle) * 1.2
            