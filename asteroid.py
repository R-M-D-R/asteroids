import pygame
import random
from constants import *
from circleshape import CircleShape
import audio


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), self.radius, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius > 50:
            audio.play_explosion_sound("big")
        elif self.radius > 20:
            audio.play_explosion_sound("medium")
        else:
            audio.play_explosion_sound("small")

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # Values I need to calculate the split
        random_angle = random.uniform(20, 50)
        vector_1 = self.velocity.rotate(random_angle)
        vector_2 = self.velocity.rotate(-random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        
        # Create two new asteroids with new velocity calculations
        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_1.velocity = vector_1 * 1.2

        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2.velocity = vector_2 * 1.2
