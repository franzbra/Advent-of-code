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
#create a set to store already visited indices
visited_indices = set()


while index < len(instructions):
    # If the command has been visited before, break
    if index in visited_indices:
        break    # Otherwise, add the command to the set of visited commands
    visited_indices.add(index)
    command, value = instructions[index]
#    print(command, value)
    #trace the index of execution
    instructions[index] = (command, value, ex_index)

    # If command is 'jmp', adjust the index
    if command == 'jmp':
        index += value
        ex_index +=1
        continue
    #count the occurancies of acc
    elif command == 'acc' :
        count += value
    index += 1
    ex_index +=1
    
print('Acc found:', count)

###########################################################
#Advent of code 2020
#Day8 - Part 2
###########################################################

#create a function to make iterations more readable
def run_instructions(instructions):
    count = 0
    index = 0
    ex_index = 0
    visited_indices = set()

    while index < len(instructions):
        # If the command has been visited before, break
        if index in visited_indices:
            break
        # Otherwise, add the command to the set of visited commands
        visited_indices.add(index)

        command, value = instructions[index]
        # Trace the index of execution
        instructions[index] = (command, value, ex_index)

        # If command is 'jmp', adjust the index
        if command == 'jmp':
            index += value
            ex_index += 1
            continue
        elif command == 'acc':
            count += value

        index += 1
        ex_index += 1

    return count, index

instructions = read_input_file(file_path)

# Find all 'jmp' instructions and their indices
jmp_indices = []
for i, (command, value) in enumerate (instructions):
    if command == 'jmp':
        jmp_indices.append(i)

for jmp_index in jmp_indices:
    # Make a copy of the original instructions
    modified_instructions = instructions[:]
    # Change the 'jmp' instruction to 'nop'
    modified_instructions[jmp_index] = ('nop', instructions[jmp_index][1])

    # Run the modified instructions
    acc_value, last_index = run_instructions(modified_instructions)
    if last_index == len(instructions):
        print(f"After changing \'jmp\' at index {jmp_index}, \'acc\' is found {acc_value} times, the last index is {last_index}")