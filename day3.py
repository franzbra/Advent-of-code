# -*- coding: utf-8 -*-
"""
Created on Mon May  6 21:19:44 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day3 - Part 1
###########################################################

def read_text_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        grid = [list(line.strip()) for line in lines]
    return grid

#generate an array of grid points associated with our flight
def path(n, grid):
    path = []
    #estimate the number of columns to implement periodicity on the grid    
    cols = len(grid[0])
    for i in range(n):
        j = (i * 3) % cols
        path.append((i, j)) 
    return path

grid = read_text_file('input.txt')
flight = path(len(grid),grid)
count= 0

for pair in flight:
    row, col = pair
    point = grid[row][col]
    if point =="#":
        count += 1
#print(f'We found {count} trees')

###########################################################
#Advent of code 2020
#Day3 - Part 2
###########################################################

#generate an array of grid points associated with our flight
def path(x, y, grid):
    path = []
    #estimate number of columns to implement periodicity on the grid    
    cols = len(grid[0])
    if x<=y:
        for i in range(1, len(grid)):
            j = (i * y) % cols
            path.append((i, j)) 
    #For sure exists a better way to do this :(
    else:
        for i in range(2, len(grid),x):
            path.append((i, y))
            y += 1 
            y = y%cols            
#    print(path)
    return path


grid = read_text_file('input.txt')
flights = [[1,1],[1,3],[1,5],[1,7],[2,1]]
tot = 1
for i in range(0,len(flights)):
    count= 0
    flight = path(flights[i][0], flights[i][1],grid)
    for pair in flight:
        row, col = pair
        point = grid[row][col]
        if point =="#":
#            print("Albero in", pair)
            count += 1
    print(f'We found {count} trees')
    tot *=count
    print(f'We found, multiplied, {tot} trees')


