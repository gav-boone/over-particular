from particle import Particle
from typing import List
import pygame

def init_pos(particle_radius: float, screen_width: int, screen_height: int) -> List[Particle]:
    spacing = particle_radius * 2.5
    particles = []
    grid_cols = 4
    start_x = screen_width / 2 - (grid_cols * spacing) / 2
    start_y = particle_radius * 3
    
    for i in range(12):
        row = i // grid_cols
        col = i % grid_cols
        x = start_x + col * spacing
        y = start_y + row * spacing
        
        particles.append(Particle(
            location=pygame.Vector2(x, y),
            velocity=pygame.Vector2(0, 0),
            acceleration=pygame.Vector2(0, 0.3),
            radius=particle_radius,
            color="blue",
        ))
    
    return particles