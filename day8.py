# -*- coding: utf-8 -*-
"""
Created on Thu May  9 10:18:45 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day8 - Part 1 
###########################################################


def read_input_file(file_path):
    with open(file_path, "r") as file:
        lines = file.readlines()

# Create a list of pairs (command, value)
    pairs = [(line.split()[0], int(line.split()[1])) for line in lines]
    return pairs
file_path = 'input.txt'
instructions = read_input_file(file_path)

count=0
index = 0
ex_index =0  
visited_indices = set()

while index < len(instructions):
    # If the command has been visited before, break
    if index in visited_indices:
        break    # Otherwise, add the command to the set of visited commands
    visited_indices.add(index)
    command, value = instructions[index]
    print(command, value)
    #trace the index of execution
    instructions[index] = (command, value, ex_index)

    # If command is 'jmp', adjust the index
    if command == 'jmp':
        index += value
        ex_index +=1
        continue
    elif command == 'acc' :
        count += value
    index += 1
    ex_index +=1
    
print('Acc found:', count)

###########################################################
#Advent of code 2020
#Day8 - Part 2
###########################################################

