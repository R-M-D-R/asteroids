import pygame
from constants import *
from circleshape import CircleShape

class Bullet(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, BULLET_RADIUS)
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), (self.position.x, self.position.y), BULLET_RADIUS, width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt