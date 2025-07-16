import matplotlib.pyplot as plt
import json
import random


x_coordinates = []
y_coordinates = []

with open("populationTracker.json", "r") as file:
    populationLst = json.load(file) 
    generation = 0

    for resetCount in populationLst:
        color = (random.random(), random.random(), random.random())

        for genCount in range(1, len(populationLst[resetCount])):
            plt.plot(genCount, populationLst[resetCount][str(genCount)], color=color, marker='.')

plt.title("Cellular Life Over Time")
plt.xlabel("Generations")
plt.ylabel("Alive Cell Population")
plt.xlim(0, 100)
plt.show()

