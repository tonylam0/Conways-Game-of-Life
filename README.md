# Conways-Game-of-Life

A Python recreation of the famous cellular automaton **Conway’s Game of Life**, built using **Pygame**.

## About This Project
This simulationn models life on a 2D grid, where:
- **Alive cells** are represented by 1's (white squares)
- **Dead cells** are represented by 0's (black squares)
- Each cell's state is determined by the eight neighboring cells around it


## Game Rules
1. **Survival**: An alive cell with 2 or 3 neighbors stays alive  
2. **Underpopulation**: An alive cell with fewer than 2 neighbors dies  
3. **Overpopulation**: An alive cell with more than 3 neighbors dies  
4. **Reproduction**: A dead cell with exactly 3 neighbors becomes alive  


## Features
1. Automatic population tracker that counts the amount of alive cells in a simulation over multiple generations
2. Automatic stable life tracker that tracks how long it took (amount of generations) & how many alive cells there were when a simulation reached stable life
3. Scatterplot that visualizes both the population tracker and stable life tracker
4. Automatic resetter that generates a new simulation every nth generation
5. Pause and reset buttons 
    - Press `SPACE` to pause/unpause the simulation
    - Press `R` to mannually reset and log the current generation's data


## Preview
<img width="200" height="820" alt="Stable Life in Conway's GOL" src="https://github.com/user-attachments/assets/4a6ff5ae-f8da-47b2-b49f-5250a30fc44c" />
<img width="200" height="820" alt="Conway's GOF Preview Card" src="https://github.com/user-attachments/assets/24d4d239-b3d8-4c68-ab73-1e33f375ec23" />
<img width="200" height="1084" alt="Conway's GOF Graph after 220 Simulations" src="https://github.com/user-attachments/assets/c639d63f-4053-4f49-aaee-520dd5c7d655" />
<img width="200" height="1074" alt="Stable Life Graph after 220 Simulations" src="https://github.com/user-attachments/assets/e814785e-dc29-4093-a2f6-7b7c70beb485" />