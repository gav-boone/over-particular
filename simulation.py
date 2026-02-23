from particle import Particle
from typing import List
import pygame


class Simulation(object):
    def __init__(self, height: int, width: int, particles: List[Particle], screen: pygame.Surface) -> None:
        self.height = height
        self.width = width
        self.particles = particles
        self.screen = screen
        self.bounding_box = pygame.Rect(
            screen.get_width() / 2 - width / 2,  # x (left)
            screen.get_height() / 2 - height / 2,  # y (top)
            width,  # width
            height,
        )

    def update(self) -> None:
        for particle in self.particles:
            particle.update(self)

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(
            screen,
            "black",
            self.bounding_box,
            width=3,
        )

        for particle in self.particles:
            pygame.draw.circle(
                screen, particle.color, particle.location, particle.radius
            )

    def get_bounding_box(self) -> pygame.Rect:
        return self.bounding_box
    
    def get_height(self) -> int:
        return self.height

    def get_width(self) -> int:
        return self.width