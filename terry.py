import pygame
from constants import *
from asteroid import Asteroid

class Terry(Asteroid):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.imageSource = pygame.image.load("./assets/images/terry.png").convert_alpha()
        self.image = pygame.transform.scale(self.imageSource, (self.radius*2, self.radius*2))
    
    def draw(self, screen):
        screen.blit(self.image, self.MidPointToTopLeft(self.position))

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.radius += ASTEROID_MIN_RADIUS
        self.image = pygame.transform.scale(self.imageSource, (self.radius*2, self.radius*2))

    def MidPointToTopLeft(self, position):
        return (position.x - self.radius, position.y - self.radius)