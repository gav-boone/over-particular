from typing import List
import pygame


class Particle(object):
    def __init__(self, location: pygame.Vector2, velocity: pygame.Vector2, acceleration: pygame.Vector2, radius: float, color: str) -> None:
        self.location = location
        self.velocity = velocity
        self.acceleration = acceleration
        self.radius = radius
        self.color = color
        self.dampening_factor = 0.5

    def update(self, sim: Simulation) -> None:
        self.velocity += self.acceleration
        self.location += self.velocity

        self.resolve_collisions(sim)

    def is_in_sim(self, sim: Simulation) -> bool:
        box = sim.get_bounding_box()
        return box.collidepoint(self.location)

    def resolve_collisions(self, sim: Simulation) -> None:
        if self.is_in_sim(sim):
            return None

        self.location = self.location - self.velocity
        self.velocity = self.velocity * -1 * self.dampening_factor

