import pygame
import random
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width=LINE_WIDTH)

    def update(self,dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        log_event("asteroid_split")
        ran_angle = random.uniform(20,50)
        new_vel_1 = self.velocity.rotate(ran_angle) * 1.2
        new_vel_2 = self.velocity.rotate(-ran_angle) * 1.2
        new_rad = self.radius - ASTEROID_MIN_RADIUS
        ast_part_1 = Asteroid(self.position.x, self.position.y, new_rad)
        ast_part_1.velocity = new_vel_1 
        ast_part_2 = Asteroid(self.position.x,self.position.y, new_rad)
        ast_part_2.velocity = new_vel_2


