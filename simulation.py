from particle import Particle
from typing import List
import pygame

class Simulation(object):
    def __init__(self, particles: List[Particle]) -> None:
        self.particles = particles

    def update(self) -> None:
        for particle in self.particles:
            particle.update()

    def draw(self, screen: pygame.Surface) -> None:
        for particle in self.particles:
            pygame.draw.circle(screen, particle.color, particle.location, particle.radius)