import random
import pygame
import math

WIDTH, HEIGHT = 1000, 800
RESOLUTION = 20  # this constant represents the size of the cells within the grid
grid = []
columns, rows = 0, 0  # placeholder values

def make2DArray():  # creates a 2D array which will represent the grid
    global columns
    global rows

    columns = round(WIDTH / RESOLUTION)
    rows = round(HEIGHT / RESOLUTION)

    for i in range(columns):
        grid.append([])
        for j in range(rows):
            grid[i].append([])
            grid[i][j].append(math.floor(random.random() * 1.2))  # randomly assigns a state to each cell in the grid

    return grid