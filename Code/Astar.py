from heapq import *
import pygame
from random import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

WIDTH = 10  # width of each cell
HEIGHT = 10  # height of each cell

MARGIN = 1  # The margin between each cell


def source(board):  # determining the source in the board(maze) that we created
    x = randint(0, len(board))
    y = randint(0, len(board))
    board[x][y] = 2


def destination(board):  # determining the destination in the board(maze) that we created
    x = randint(0, len(board))
    y = randint(0, len(board))
    board[x][y] = 3


'''A* SEARCH'''


class Astar:

    def __init__(self, size, window, start, end):  # The constructor: defining the size,window,distance,f,g,h,start
        # and end points
        self.size = size
        self.window = window
        self.start = start
        self.end = end
        self.f = {}
        self.h = None
        self.g = set()
        self.cl = set()
        self.distance = None
        self.time = None
        self.grid = []

    def manhattan(self, a, b):  # as we are considering H values to be manhattan values in this project, this is a
        # function that calculates the manhattan values.
        return abs(a[0] - b[0]) + abs(a[1] - b[1])

    '''f(n) = g(n) + h(n)'''

    def F(self):
        return self.f

    def H(self):
        return self.h

    def G(self):
        return self.h

    def closelist(self):
        return self.cl

    # Repeated Forward A*
    def repeated_forward_astar(self, array):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # (0,1) = north, (0,-1) = south, (1,0) = west, (-1,0) = east

        closeList = set()  # closed list

        came_from = {}

        g = {self.start: 0}  # the g value of the starting node is always zero

        f = {self.start: self.manhattan(self.start,self.end)}  # f value is the sum of g value and h value, meaning g and the
        # manhattan distance between the nodes

        openList = []  # openlist

        heappush(openList, (f[self.start], self.start))  # pushing the nodes into the open list

        '''Traversing through the grid, by popping elements from the open list'''
        while openList:
            current = heappop(openList)[1]
            if current == self.end:
                total_path = []

                while current in came_from:
                    pygame.draw.rect(self.window, MAGENTA,
                                     [(MARGIN + WIDTH) * current[1] + MARGIN, (MARGIN + HEIGHT) * current[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    total_path.append(current)
                    current = came_from[current]
                self.distance = len(total_path)
                return total_path

            closeList.add(current)
            self.cl.add(current)

            '''Checking the neighbors calculating the f values'''
            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j

                heuristicg = g[current] + self.manhattan(current, neighbor)

                self.h = self.manhattan(current, self.end)

                if 0 <= neighbor[0] < self.size:
                    if 0 <= neighbor[1] < self.size:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in closeList and heuristicg >= g.get(neighbor, 0):
                    continue

                if heuristicg < g.get(neighbor, 0) or neighbor not in [i[1] for i in openList]:
                    self.g.add(heuristicg)

                    came_from[neighbor] = current
                    g[neighbor] = heuristicg
                    f[neighbor] = heuristicg + self.manhattan(neighbor, self.end)
                    pygame.draw.rect(self.window, CYAN,
                                     [(MARGIN + WIDTH) * neighbor[1] + MARGIN, (MARGIN + HEIGHT) * neighbor[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    heappush(openList, (f[neighbor], neighbor))
        print('Path not found: Repeated Forward A Star')
        return False

    '''Implementation of Repeated Backwards A*, the difference between Repeated Forward A* and Repeated Backward A* 
    is that while Forward A* goes from the start to the end node, Backward A* goes from the end to start nodes making 
    it faster. '''

    def repeated_backward_astar(self, array):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        close_set = set()

        previous = {}

        gscore = {self.end: 0}

        fscore = {self.end: self.manhattan(self.end, self.start)}

        open_set = []

        heappush(open_set, (fscore[self.end], self.end))

        while open_set:
            present = heappop(open_set)[1]
            if present == self.start:
                total_path = []

                while present in previous:
                    pygame.draw.rect(self.window, MAGENTA,
                                     [(MARGIN + WIDTH) * present[1] + MARGIN, (MARGIN + HEIGHT) * present[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    total_path.append(present)
                    present = previous[present]
                self.distance = len(total_path)
                return total_path

            close_set.add(present)

            for i, j in neighbors:
                neighbor = present[0] + i, present[1] + j

                heuristicg = gscore[present] + self.manhattan(present, neighbor)

                if 0 <= neighbor[0] < self.size:
                    if 0 <= neighbor[1] < self.size:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and heuristicg >= gscore.get(neighbor, 0):
                    continue

                if heuristicg < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_set]:
                    self.g.add(heuristicg)

                    previous[neighbor] = present
                    gscore[neighbor] = heuristicg
                    fscore[neighbor] = heuristicg + self.manhattan(neighbor, self.start)
                    pygame.draw.rect(self.window, CYAN,
                                     [(MARGIN + WIDTH) * neighbor[1] + MARGIN, (MARGIN + HEIGHT) * neighbor[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    heappush(open_set, (fscore[neighbor], neighbor))
        print('Path not found: Repeated Backward A Star')
        return False

    '''Adaptive A* is the modified version of Forward A* search, adaptive A* updates the h-values using information 
    from previous searches. It basically transforms consistent hvalues into more informed consistent h-values. This 
    allows it  to find shortest paths in state spaces where the action costs can increase over time since consistent 
    h-values remain consistent after action cost increases. '''

    def adaptive_astar(self, array):
        self.forward(array)
        newfscore = self.F()
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        close_set = set()

        came_from = {}

        gscore = {self.start: 0}

        fscore = newfscore

        open_set = []

        heappush(open_set, (fscore[self.start], self.start))

        while open_set:
            current = heappop(open_set)[1]
            if current == self.end:
                total_path = []

                while current in came_from:
                    pygame.draw.rect(self.window, MAGENTA,
                                     [(MARGIN + WIDTH) * current[1] + MARGIN, (MARGIN + HEIGHT) * current[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    total_path.append(current)
                    current = came_from[current]

                self.distance = len(total_path)
                return total_path

            close_set.add(current)
            self.cl.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j

                heuristicg = gscore[current] + self.manhattan(current, neighbor)

                self.h = self.manhattan(current, self.end)

                if 0 <= neighbor[0] < self.size:
                    if 0 <= neighbor[1] < self.size:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and heuristicg >= gscore.get(neighbor, 0):
                    continue

                if heuristicg < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_set]:
                    self.g.add(heuristicg)

                    came_from[neighbor] = current
                    gscore[neighbor] = heuristicg
                    fscore[neighbor] = heuristicg + self.manhattan(neighbor, self.end)
                    pygame.draw.rect(self.window, CYAN,
                                     [(MARGIN + WIDTH) * neighbor[1] + MARGIN, (MARGIN + HEIGHT) * neighbor[0] + MARGIN,
                                      WIDTH, HEIGHT])
                    pygame.display.update()
                    heappush(open_set, (fscore[neighbor], neighbor))
        print('Path not found: Visible Forwards A Star')
        return False

    def forward(self, array):
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        close_set = set()

        came_from = {}

        gscore = {self.start: 0}

        fscore = {self.start: self.manhattan(self.start, self.end)}

        open_set = []

        heappush(open_set, (fscore[self.start], self.start))

        while open_set:
            # print(open_set)
            current = heappop(open_set)[1]
            # print(current)
            if current == self.end:
                total_path = []

                while current in came_from:
                    total_path.append(current)
                    current = came_from[current]

                return total_path

            close_set.add(current)
            self.cl.add(current)

            for i, j in neighbors:
                neighbor = current[0] + i, current[1] + j

                heuristicg = gscore[current] + self.manhattan(current, neighbor)

                self.h = self.manhattan(current, self.end)

                if 0 <= neighbor[0] < self.size:
                    if 0 <= neighbor[1] < self.size:
                        if array[neighbor[0]][neighbor[1]] == 1:
                            continue
                    else:
                        continue
                else:
                    continue

                if neighbor in close_set and heuristicg >= gscore.get(neighbor, 0):
                    continue

                if heuristicg < gscore.get(neighbor, 0) or neighbor not in [i[1] for i in open_set]:
                    self.g.add(heuristicg)

                    came_from[neighbor] = current
                    gscore[neighbor] = heuristicg
                    fscore[neighbor] = heuristicg + self.manhattan(neighbor, self.end)
                    self.f = fscore
                    heappush(open_set, (fscore[neighbor], neighbor))
        return False
