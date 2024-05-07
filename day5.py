# -*- coding: utf-8 -*-
"""
Created on Tue May  7 15:31:33 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day5 - Part 1
###########################################################

def read_input_file(file_path):
    lines = []
    max_row = 127
    min_row = 0
    max_column=7
    min_column=0
    seat = []
    with open(file_path, 'r') as file:
        for line in file:
            part1 = line[:7]
            part2 = line[7:10]
            lines.append([part1, part2])
            
            for letter in part1:
                midpoint = (min_row + max_row) // 2
        
                # Update the interval based on the letter
                if letter == 'F':
                    max_row = midpoint
                elif letter == 'B':
                    min_row = midpoint + 1  
                               
            for letter in part2:
                midpoint_col = (min_column + max_column) // 2
        
                # Update the interval based on the letter
                if letter == 'R':
                    min_column = midpoint_col +1
                elif letter == 'L':
                    max_column = midpoint_col  
            seat.append([max(max_row, min_row), max(max_column, min_column)])
            max_row = 127
            min_row = 0     
            max_column=7
            min_column=0                     
    return seat

file_path = "input.txt"
seats = read_input_file(file_path)

id_plane = []
for seat in seats:
    id_plane.append(seat[0]*8+seat[1])
print(max(id_plane))

###########################################################
#Advent of code 2020
#Day5 - Part 2
###########################################################
#Simulate all available seats on the plane
plane = [(x, y) for x in range(124) for y in range(8)] 

#Filter the seat excluding the front and back rows and those on your list
free = [[x, y] for x, y in plane if [x, y] not in seats and x not in range(0,6) and x not in range (101,124)]

id_plane = []
for seat in free:
    id_plane.append(seat[0]*8+seat[1])
print((id_plane))

