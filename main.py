import pygame
import grid


pygame.init()

WINDOW = pygame.display.set_mode((grid.WIDTH, grid.HEIGHT))
pygame.display.set_caption("Conway's Game of Life Sim")


def main():
    running = True
    clock = pygame.time.Clock()

    while running:
        WINDOW.fill((0,0,0))
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    