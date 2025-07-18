# Conways-Game-of-Life

Recreated the famous cellular automata "Conway's Game of Life" using Pygame

## About This Project
A game that simulates life through a grid of cells with alive cells (represented by 1's) & dead cells (represented by 0's)

The future state of cells is determined by its neighborhood (8 surrounding cells)

<img width="200" height="820" alt="Stable Life in Conway's GOL" src="https://github.com/user-attachments/assets/4a6ff5ae-f8da-47b2-b49f-5250a30fc44c" />
<img width="200" height="820" alt="Conway's GOF Preview Card" src="https://github.com/user-attachments/assets/24d4d239-b3d8-4c68-ab73-1e33f375ec23" />
<img width="200" height="1084" alt="Conway's GOF Graph after 220 Simulations" src="https://github.com/user-attachments/assets/c639d63f-4053-4f49-aaee-520dd5c7d655" />
<img width="200" height="1074" alt="Stable Life Graph after 220 Simulations" src="https://github.com/user-attachments/assets/e814785e-dc29-4093-a2f6-7b7c70beb485" />

## Rules
1. if an alive cell has 2 or 3 surrounding alive cells -> stays alive
2. if an alive cell has 1 or less surrounding alive cells -> dies due to loneliness
3. if an alive cell has 4 or more surrounding alive cells -> dies from overpopulation
4. if an dead cell has exactly 3 surrounding alive cells -> become alive by reproduction

## Features
1. Added an **automatic population tracker** that counts the amount of alive cells in a simulation over multiple generations
2. An **automatic stable life tracker** that tracks how long it took (amount of generations) & how many alive cells there were when a simulation reached stable life
3. A **graph** that illustrates both the population tracker and stable life tracker
4. An **automatic resetter** that generates a new simulation every nth generation
5. A **pause and reset button**