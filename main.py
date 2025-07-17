import pygame
import gen
import json
import copy


pygame.init()
WINDOW = pygame.display.set_mode((gen.WIDTH, gen.HEIGHT))
pygame.display.set_caption("Conway's Game of Life Sim")

def checkLibraryEmpty(fileName, type):
    try:
        with open(fileName, "r") as file:
            data = json.load(file)
            if not data:
                with open(fileName, "w") as file:
                    json.dump(type, file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(fileName, "w") as file:
            json.dump(type, file)

def reset():  # used to automatically reset the cellular automaton after a certain amount of generations
    gen.grid = []
    gen.make2DArray()

def matchResetCount():  # handles the error if the resetCount is different than the popTracker count
    with open("populationTracker.json", "r") as file:
        length = len(json.load(file))

    with open("resetCount.txt", "w") as file:
        file.write(str(length))

def main():
    running = True
    genFlag = True  # used to check for pausing
    stableFlag = False  # used to check if program should track stable life populaiton
    clock = pygame.time.Clock()

    checkLibraryEmpty("populationTracker.json", {})
    checkLibraryEmpty("stabilityTracker.json", [[],[]])
    matchResetCount()

    population = {}  # used to store the amount of alive cells per generation
    prevGrid = []  # used to check for stable life
    aliveCount = 0  # amount of alive cells in a generation
    genCount = 0  # amount of generations an automaton has gone through
    resetCount = 0  # amount of times the simulation has been reset

    with open("resetCount.txt", "r") as file:
        resetCount = int(file.read())

    gen.make2DArray()

    while running:
        WINDOW.fill((0,0,0))
        clock.tick(10)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                resetCount += 1
                currentGen = {resetCount: population}

                with open("populationTracker.json", "r") as file:
                    populationLst = json.load(file)
                    populationLst.update(currentGen)

                with open("populationTracker.json", "w") as file:
                    json.dump(populationLst, file, indent=1)

                with open("resetCount.txt", "w") as file:
                    file.write(str(resetCount))
            
                running = False

            elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:
                        gen.mousePos = event.pos
                        gen.switchSignal = True

            elif event.type == pygame.KEYDOWN:
                '''
                if a new generation is created, the old generation population
                is tracked in the json file
                '''
                if event.key == pygame.K_r:
                    resetCount += 1
                    currentGen = {resetCount: population}

                    with open("populationTracker.json", "r") as file:
                        populationLst = json.load(file)
                        populationLst.update(currentGen)

                    with open("populationTracker.json", "w") as file:
                        json.dump(populationLst, file, indent=1)

                    genCount = 0
                    population = {}  # population has to reset to restart the population tracking
                    stableFlag = False  # resets stability check
                    reset()

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
                    if genFlag:
                        aliveCount += 1

                    x = i * gen.RESOLUTION
                    y = j * gen.RESOLUTION
                    pygame.draw.rect(WINDOW, (255, 255, 255), (x, y, gen.RESOLUTION, gen.RESOLUTION))
        
        if genFlag:
            # deepcopy used b/c the nested list in grid will still be referenced with a shallow copy
            prevGrid = copy.deepcopy(gen.grid)
            gen.updateState()
            population[genCount] = aliveCount

            if gen.grid == prevGrid and not stableFlag:  # used to check for stable life
                with open("stabilityTracker.json", "r") as file:
                    stabilityLst = json.load(file)
                    stabilityLst[0].append(genCount)
                    stabilityLst[1].append(aliveCount)

                with open("stabilityTracker.json", "w") as file:
                    json.dump(stabilityLst, file)
                stableFlag = True

            genCount += 1
            aliveCount = 0  # reset in order to count the amount of alive cells in the next generation

        if genCount > 100:  # resets automaton when the simulation reaches 100 generations
            resetCount += 1
            currentGen = {resetCount: population}

            with open("populationTracker.json", "r") as file:
                populationLst = json.load(file)
                populationLst.update(currentGen)

            with open("populationTracker.json", "w") as file:
                json.dump(populationLst, file, indent=1)

            genCount = 0
            population = {}
            stableFlag = False
            reset()

        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
    