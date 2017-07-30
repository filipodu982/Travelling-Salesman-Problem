import pygame
from random import shuffle, randint,random
from math import hypot, factorial
from time import sleep

# some setup and variables/lists
pygame.init()
size = (400,400)
screen = pygame.display.set_mode((size))
points = 8                                                                      # how many cities do we want?
cords = []                                                                      # array storing coordinates of every city e.g. [(255,350), (310,270)]
black = 0, 0, 0                                                                 # RGB values of black color
best = float('inf')                                                             # I guess the biggest number is infinity so...
popSize = 200
mutationRate = 0.01
clock = pygame.time.Clock()
done = False

# generating starting population
def generatePopulation(n):
    default = []
    population = []
    if n > factorial(points):
        print 'Number too big! Pick a smaller population'
    for i in range(points):
        default.append(i)
    for i in range(popSize):
        shuffle(default)
        population.append(default[:])
    return population

# function calculating distance betweent all points in array
def calcDistance(array):
    dist = 0
    for i in range(len(array)-1):
        dist += hypot((cords[array[i]][0] - cords[array[i+1]][0]), (cords[array[i]][1] - cords[array[i+1]][1]))
    return dist

# generating random coordinates of circles
for i in range(points):
    x = randint(0,size[0])
    y = randint(0,size[0])
    cords.append((x,y))

# these lines were made for debugging to check whether a solution is trully the best
# I have another program which is TSP by brute forcing every solution
# so I modified it to check solutions from GA, you can uncomment if you want to check

#with open('places.txt', 'w') as f:
#    for i in cords:
#        f.write(str(i[0])+','+str(i[1])+ '\n')

# calculating fitness which is basically 1/distance * a constant which is in this case 5000
def calcFitness():
    d = []
    for i in pop:
        d.append(calcDistance(i))
    worst = max(d)
    for i in range(len(d)):
        d[i] = round((float(1)/d[i]) * 5000)
    return d

# generating gene pool e.g. if a list has fitness of 5, it will be added to the pool 5 times
def genPool():
    species = []
    for i in range(len(pop)):
        for j in range(int(fitness[i])):
            species.append(pop[i])
    return species

def crossover():
    children = []
    for i in range(popSize):
        # take two random parents, the bigger the fitness, the more likely the parent is to be picked
        parentA = pool[randint(0, len(pool)-1)]
        parentB = pool[randint(0, len(pool)-1)]

        # check if we don't have two same parents
        if parentA == parentB:
            parentB = pool[randint(0, len(pool)-1)]

        # take half points of parentA
        child = parentA[0:(points/2)]
        for j in parentB:
            # add remaining points of parent B
            if j not in child:
                child.append(j)

        # randomly mutate by replacing two nearby points with each other
        for j in range(len(child)-1):
            if random() < mutationRate:
                buff = child[j]
                child[j] = child[j+1]
                child[j+1] = buff
        children.append(child)
    return children

pop = generatePopulation(points)                                                # generating first population

# main loop
while not done:
    distances = []
    fitness = calcFitness()                                                     # a list which stores all fitness values
    pool = genPool()                                                            # a list which stores population members according to their fitness
    pop = crossover()                                                           # making a new population by crossover

    # finding the quickest route in population
    for i in range(len(pop)):
        distances.append(calcDistance(pop[i]))
    dist = min(distances)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # main condition which searches for the best route
    if dist <= best:
        screen.fill(black)
        # drawing circles all over again in each frame. Not the most effective solution, but it's the only one so far
        for i in cords:
            pygame.draw.circle(screen, (255,255,255), i,5)
            pygame.display.update()

        # drawing the best route
        for i in range(points - 1):
            pygame.draw.line(screen, (255,255,255), cords[pop[distances.index(dist)][i]], cords[pop[distances.index(dist)][i+1]])
            pygame.display.update()
        best = dist

    print max(fitness), best                                                    # printing the best fitness score and the best distance so far
    clock.tick(120)
    #sleep(0.2)
