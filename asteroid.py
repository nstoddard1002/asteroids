import circleshape
import pygame
import random
from constants import *

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.containers = ()
    
    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        pos_x,pos_y = self.position
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            new_angle = random.uniform(20,50)
            new_vector1 = self.velocity.rotate(new_angle)
            new_vector2 = self.velocity.rotate(-abs(new_angle))
            new_radii = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(pos_x,pos_y,new_radii)
            asteroid2 = Asteroid(pos_x,pos_y,new_radii)
            asteroid1.velocity = new_vector1 * 1.2
            asteroid2.velocity = new_vector2 * 1.2
            return
        
