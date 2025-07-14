import random
import pygame

WIDTH, HEIGHT = 100, 100
resolution = 20
grid = []
columns, rows = 0, 0  # placeholder values

def make2DArray():  # creates a 2D array which will represent the grid
    global columns
    global rows

    columns = round(WIDTH / resolution)
    rows = round(HEIGHT / resolution)

    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append([])

    return grid, columns, rows

def stateAssign():
    make2DArray()

    for i in range(columns):
        for j in range(rows):
            grid[i][j].append(random.randint(0, 1))  # randomly assigns a state to each cell in the grid

    return grid

def draw():
    stateAssign()

    for i in range(columns):
        for j in range(rows):
            pygame.draw.rect()

print(stateAssign())

