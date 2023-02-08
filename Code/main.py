import time
from Astar import *
import timeit
from Astar import *

''' Opening and Loading the grid world into the code'''
num = int(input('Enter a world from 1 to 50: \n'))
if num > 50 or num < 0:
    print("Please enter a number between 0 and 49")
string = 'grid' + str(num) + '.txt'
text_file = open(string, 'r')
lines = text_file.readlines()
grid = []
for line in lines:
    line = line.strip().split(',')
    line = list(map(int, line))
    grid.append(line)

start_state = (0, 0)
goal_state = (len(grid) - 1, len(grid) - 1)
ROWS = len(grid)

'''Initialising pygame'''
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(((ROWS * 11) + 1, (ROWS * 11) + 1))
pygame.display.set_caption("Fast Trajectory Replanning")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
time = 0
distance = 0
# Creating the screen
for row in range(ROWS):
    for column in range(ROWS):
        color = WHITE
        if grid[row][column] == 1:
            color = BLACK
        pygame.draw.rect(screen, color,
                         [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

        if grid[row][column] == 10:
            color = RED
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                              HEIGHT])
        if grid[row][column] == 5:
            color = GREEN
            pygame.draw.rect(screen, color,
                             [(MARGIN + WIDTH) * column + MARGIN, (MARGIN + HEIGHT) * row + MARGIN, WIDTH,
                              HEIGHT])

pygame.display.flip()

'''Main Program'''

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # If user clicked close, close the screen
            done = True
        elif event.type == pygame.KEYDOWN:  # in the keydown library, pygame takes keyboard keys as input and response
            # accordingly
            if event.key == pygame.K_c:  # if we press c(clear) the screen will be cleared
                for row in range(ROWS):
                    for column in range(ROWS):
                        color = WHITE
                        if grid[row][column] != 1:
                            if grid[row][column] != 10:
                                if grid[row][column] != 5:
                                    color = WHITE
                                    grid[row][column] = 0
                                    pygame.draw.rect(screen, color, [(MARGIN + WIDTH) * column + MARGIN,
                                                                     (MARGIN + HEIGHT) * row + MARGIN, WIDTH, HEIGHT])

                pygame.display.flip()
                time = 0
                distance = 0
                print('Path Cleared')
            elif event.key == pygame.K_1:  # If we press 1, Repeated Forward A* will be called
                start = timeit.default_timer()
                astar = Astar(ROWS, screen, start_state, goal_state)
                astar.repeated_forward_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                print(
                    'Running Repeated Forward A*: \nTime Taken: {} seconds \nDistance: {}'.format(time, astar.distance))
            elif event.key == pygame.K_2:  # If we press 2, Repeated Backward A* will be called
                start = timeit.default_timer()
                astar = Astar(ROWS, screen, start_state, goal_state)
                astar.repeated_backward_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                print('Running Repeated Backwards A*: \nTime Taken: {} seconds \nDistance: {}'.format(time,
                                                                                                      astar.distance))
            elif event.key == pygame.K_3:  # If we press 3, Repeated Backward A* will be called
                start = timeit.default_timer()
                astar = Astar(ROWS, screen, start_state, goal_state)
                astar.adaptive_astar(grid)
                stop = timeit.default_timer()
                pygame.display.flip()
                time = stop - start
                print('Running Adaptive A*: \nTime Taken: {} seconds \nDistance: {}'.format(time, astar.distance))

    pygame.display.flip()

pygame.quit()
