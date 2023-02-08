from random import *
import numpy as np
import os

'''Generating 50 gridworlds of 101x101 size and saving them to the project folder'''
for grids in range(0, 50):
    grid = []
    for row in range(101):
        grid.append([])
        for col in range(101):
            grid[row].append(0)
    gridLength = len(grid)
    for i in range(gridLength):
        for j in range(gridLength):
            if random() < 0.7:
                grid[i][j] = 0
            else:
                grid[i][j] = 1
    grid[0][0] = 10  # setting the initial cell(source) to a random number so that it is easy to identify it
    grid[gridLength - 1][gridLength - 1] = 5  # setting the final cell(destination) to a random number to identify it
    filename = 'grid' + str(grids + 1) + '.txt'
    np.savetxt(filename, grid, delimiter=",", newline="\n", fmt='%i')

