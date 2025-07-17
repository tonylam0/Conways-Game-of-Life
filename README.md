# Conways-Game-of-Life

Recreated the famous cellular automata "Conway's Game of Life" using Pygame

## About This Project
A game that simulates life through a grid of cells with alive cells (represented by 1) & dead cells (represented by 0)

The future state of cells are determined by its neighborhood (8 surrounding cells)

## Rules
1. if an alive cell has 2 or 3 surrounding alive cells -> stays alive
2. if an alive cell has 1 or less surrounding alive cells -> dies due to loneliness
3. if an alive cell has 4 or more surrounding alive cells -> dies from overpopulation
4. if an dead cell has exactly 3 surrounding alive cells -> become alive by reproduction

## Features
1. Added an **automatic population tracker** that counts the amount of alive cells in a simulation over multiple generations
2. An **automatic stable life tracker** that tracks how long it took (amount of generations) & how many alive cells there were when a simulation reached stable life
3. A **graph** that illustrates both the population tracker and stable life tracker
4. An **auto resetter** that generates a new simulation every nth generation
5. A **pause and reset button**