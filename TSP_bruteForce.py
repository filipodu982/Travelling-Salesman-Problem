import pygame, random, math,time
#some setup and variables/lists
pygame.init()
passed = 0                                                                      #how many cycles has already passed
size = (400,400)
screen = pygame.display.set_mode((size))
done = False
points = 10                                                                     # how many cities do we want?
cords = []                                                                      # array storing coordinates of every city e.g. [(255,350), (310,270)]
black = 0, 0, 0                                                                 # RGB values of black color
best = 999999999999999
pop = []                                                                        # the order in which the points should be visited
checked = []                                                                    # array storing all checked permutations

for i in range(points):                                                         # generating first order to begin with
    pop.append(i)

clock = pygame.time.Clock()
howMany = math.factorial(points)                                                # how many permutations there are

# function which checks whether a specified array has already been checked and evaluated
def exists(what):
    for i in checked:
        if what == i:
            return True
            break
    return False

# function calculating distance betweent points in array
def calcDistance(array):
    dist = 0
    for i in range(len(array)-1):
        dist += math.hypot((cords[array[i]][0] - cords[array[i+1]][0]), (cords[array[i]][1] - cords[array[i+1]][1]))
    return dist

# generating coordinates of circles
for i in range(points):
    x = random.randint(0,size[0])
    y = random.randint(0,size[0])
    cords.append((x,y))

# main loop
while not done:
    distance = calcDistance(pop)
    checked.append(pop[:])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # main condition which searches for the best route
    if distance < best:
        screen.fill(black)
        # drawing circles all over again in each frame. Not the most effective solution, but it's the only one so far
        for i in cords:
            pygame.draw.circle(screen, (255,255,255), i,5)
            pygame.display.update()

        # drawing the best route
        for i in range(len(pop) - 1):
            pygame.draw.line(screen, (255,255,255), cords[pop[i]], cords[pop[i+1]])
            pygame.display.update()
            best = distance

    random.shuffle(pop)
    # here we check whether a new, shuffled order has already been used
    if exists(pop):
        random.shuffle(pop)

    passed += 1.0
    percent = round((passed/howMany)*100,2)
    print percent                                                               # percent of finished permutations. however not the most accurate way, because shuffle function repeats some permutations which are not checked anywhere
    clock.tick(60)                                                              # how many FPS
    # time.sleep(0.2)                                                            # uncomment if you want to reduce the speed of simulation

    # finishing program after it has checked all possible permutations
    if percent >= 100:
        s = raw_input('Search finished. This is the most optimal route between points.')
        print len(checked)
        break
