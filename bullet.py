import pygame
from constants import *
from circleshape import CircleShape
import audio

class Bullet(CircleShape):
    def __init__(self, x, y, velocity):
        super().__init__(x, y, BULLET_RADIUS)
        audio.play_shoot_sound()
        self.velocity = velocity
    
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 30, 77), (self.position.x, self.position.y), BULLET_RADIUS) #, width=2
    
    def update(self, dt):
        # Once the bullets go beyond the border of the screen, they are deleted
        if (self.position.x - BULLET_RADIUS < 0 or 
            self.position.x + BULLET_RADIUS > SCREEN_WIDTH or
            self.position.y - BULLET_RADIUS < 0 or
            self.position.y + BULLET_RADIUS > SCREEN_HEIGHT):
                self.kill()
        self.position += self.velocity * dt