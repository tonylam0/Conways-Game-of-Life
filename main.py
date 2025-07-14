import pygame
import gen


pygame.init()

WINDOW = pygame.display.set_mode((gen.WIDTH, gen.HEIGHT))
pygame.display.set_caption("Conway's Game of Life Sim")


def main():
    running = True
    clock = pygame.time.Clock()
    gen.stateAssign()

    while running:
        WINDOW.fill((0,0,0))
        clock.tick(20)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        for i in range(gen.columns):
            for j in range(gen.rows):
                if gen.grid[i][j] == [1]:
                    x = i * gen.RESOLUTION
                    y = j * gen.RESOLUTION
                    pygame.draw.rect(WINDOW, (255, 255, 255), (x, y, gen.RESOLUTION, gen.RESOLUTION))

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    