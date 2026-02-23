import pygame
from particle import Particle
from simulation import Simulation


def main():

    SCREEN_HEIGHT = 720
    SCREEN_WIDTH = 1280
    FPS = 60

    # pygame setup
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True
    dt = 0

    particle = Particle(
        location=pygame.Vector2(SCREEN_WIDTH/2, SCREEN_HEIGHT/4),
        velocity=pygame.Vector2(0, 0),
        acceleration=pygame.Vector2(0, 1),
        radius=10,
        color="blue",
    )

    sim = Simulation([particle])

    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("black")

        sim.update()

        sim.draw(screen)

        # flip() the display to put your work on screen
        pygame.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(FPS) / 1000

    pygame.quit()


if __name__ == "__main__":
    main()
