from typing import List
import pygame

class Particle(object):
    def __init__(self, location: pygame.Vector2, velocity: pygame.Vector2, acceleration: pygame.Vector2, radius: float, color: str) -> None:
        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.color = color

    def update(self) -> None:
        self.velocity += self.acceleration
        self.location += self.velocity