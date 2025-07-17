import matplotlib.pyplot as plt
import json
import random


plt.figure(1)
with open("populationTracker.json", "r") as file:
    populationLst = json.load(file) 

    for resetCount in populationLst:
        color = (random.random(), random.random(), random.random())

        for genCount in range(1, len(populationLst[resetCount])):
            plt.plot(genCount, populationLst[resetCount][str(genCount)], color=color, marker='_')

plt.title("Cellular Life Over Time")
plt.xlabel("Generations")
plt.ylabel("Alive Cell Population")
plt.xlim(0, 100)

plt.figure(2)
with open("stabilityTracker.json", "r") as file:
    stabilityLst = json.load(file)
    plt.scatter(stabilityLst[0], stabilityLst[1], marker='.')

plt.title("Stable Life Populations")
plt.xlabel("Generations")
plt.ylabel("Stable Life Population")
plt.ylim(0, 100)
plt.xlim(0, 100)

plt.show()

