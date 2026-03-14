
import random
from logger import log_event
from circleshape import CircleShape
import pygame
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    
    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        spawn_angle = random.uniform(20, 50)
        child_vector1 = self.velocity.rotate(spawn_angle)
        child_vector2 = self.velocity.rotate(-spawn_angle)
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child_asteroid1 = Asteroid(self.position.x, self.position.y, child_radius)
        child_asteroid1.velocity = child_vector1 * 1.2
        child_asteroid2 = Asteroid(self.position.x, self.position.y, child_radius)
        child_asteroid2.velocity = child_vector2 * 1.2