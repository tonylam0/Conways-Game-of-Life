import pygame
import gen


pygame.init()

WINDOW = pygame.display.set_mode((gen.WIDTH, gen.HEIGHT))
pygame.display.set_caption("Conway's Game of Life Sim")


def main():
    running = True
    genFlag = True  # used to check for pausing
    clock = pygame.time.Clock()
    gen.make2DArray()

    while running:
        WINDOW.fill((0,0,0))
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        gen.mousePos = event.pos
                        gen.switchSignal = True

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    gen.grid = []
                    gen.make2DArray()
                elif event.key == pygame.K_SPACE and genFlag:
                    genFlag = False
                elif event.key == pygame.K_SPACE and not genFlag:
                    genFlag = True

        for i in range(1, gen.columns - 1):
            for j in range(1, gen.rows - 1):
                # finds which cell the mouse position clicked on by finding the column and row
                # column and row is found by dividing by the resolution 
                if gen.mousePos[0] // gen.RESOLUTION == i and gen.mousePos[1] // gen.RESOLUTION == j and gen.switchSignal:
                    if gen.grid[i][j] == 0:  # clicking a dead cell turns it into an alive cell  
                        gen.grid[i][j] = 1
                    else:
                        gen.grid[i][j] = 0  # clicking an alive cell turns it into a dead cell
                    gen.switchSignal = False

                if gen.grid[i][j] == 1:
                    x = i * gen.RESOLUTION
                    y = j * gen.RESOLUTION
                    pygame.draw.rect(WINDOW, (255, 255, 255), (x, y, gen.RESOLUTION, gen.RESOLUTION))
        
        if genFlag:
            gen.updateState()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    