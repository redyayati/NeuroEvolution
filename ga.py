import random 
from bird import Bird
from variables import *
def nextGeneration() :
    calculateFitness()
    for i in range(total) :
        newBird = pickOne()
        birds.append(newBird)
    del savedBirds[:]
def pickOne(): 
    index = 0 
    r = random.random()
    while r > 0 :
        r = r - savedBirds[index].fitness
        index += 1
    index -= 1 
    theChoosenOne = savedBirds[index]
    child = Bird(theChoosenOne.brain)
    child.mutate()
    return child
def calculateFitness() : 
    sum = 0
    for bird in savedBirds : 
        sum += bird.score
    for bird in savedBirds : 
        bird.fitness = bird.score / sum
