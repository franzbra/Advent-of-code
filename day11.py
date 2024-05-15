# -*- coding: utf-8 -*-
"""
Created on Wed May 15 09:47:33 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day11 - Part 1 
###########################################################
import numpy as np
import time

start_time = time.time()

def read_input_file(file_path):
    with open(file_path, 'r') as file:
        grid = np.array([list(line.strip()) for line in file.readlines()])
    return grid

#Calculate the values of the 8 neighbours around a cell
def get_neighbors(grid, i, j):
    # List of possible 8 directions
    directions = [(-1, -1), (-1, 0), (-1, 1),
                  (0, -1),         (0, 1),
                  (1, -1), (1, 0), (1, 1)]
    
    neighbors = []
    rows, cols = grid.shape

    for direction in directions:
        ni, nj = i + direction[0], j + direction[1]
        # Check if the neighbor is within grid bounds
        if 0 <= ni < rows and 0 <= nj < cols:
            neighbors.append(grid[ni, nj])
    
    return neighbors

seats = read_input_file('prova.txt')
#PROBLEM: THE EXERCISE SOLUTION IS NOT SERIALIZED!?
#Pretend all the guests arrive at once without seeing the others!?
for t in range(0,100):
    #don't overwrite the initial plane, but create a replica
    empty_plane = np.copy(seats)

    for i,row in enumerate(seats):
        for j,seat in enumerate(row):
            neighbours = get_neighbors(seats, i, j)
            if seat == 'L' and "#" not in neighbours:
                empty_plane[i,j] = '#'
            elif seat == '#' and neighbours.count('#') >= 4:
                empty_plane[i,j] = "L"
    if np.sum(empty_plane == '#') == np.sum(seats == '#') :
        print('Steady state reached')
        break
    seats= np.copy(empty_plane)
    
    
print('There are', np.sum(seats == '#'), 'occupied seats')
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} s") #TOO MUCH TIME :(

###########################################################
#Advent of code 2020
#Day11 - Part 2 
###########################################################
start_time = time.time()

#function that calculates the neighbors according to the new rules
def get_extended_neighbors(grid, i, j):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1), 
                  (-1, -1), (-1, 1), (1, -1), (1, 1)] 
    neighbors = []

    for di, dj in directions:
        ni, nj = i + di, j + dj
        while 0 <= ni < grid.shape[0] and 0 <= nj < grid.shape[1]:
            #stop the research of the neighbors in this direction
            #if # or L are found
            if grid[ni, nj] == '#':
                neighbors.append(grid[ni, nj])
                break
            elif grid[ni, nj] == 'L':
                neighbors.append(grid[ni, nj])
                break
            ni += di
            nj += dj

    return neighbors

seats = read_input_file('input.txt')

for t in range(0,100):
    empty_plane = np.copy(seats)

    for i,row in enumerate(seats):
        for j,seat in enumerate(row):
            neighbours = get_extended_neighbors(seats, i, j)
            if seat == 'L' and "#" not in neighbours:
                empty_plane[i,j] = '#'
            elif seat == '#' and neighbours.count('#') >= 5:
                empty_plane[i,j] = "L"
    if np.sum(empty_plane == '#') == np.sum(seats == '#') :
        print('Steady state reached')
        break
    seats= np.copy(empty_plane)


print('There are', np.sum(seats == '#'), 'occupied seats')
end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time} s") #TOO MUCH TIME :(

