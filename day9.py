# -*- coding: utf-8 -*-
"""
Created on Fri May 10 12:06:10 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day9 - Part 1 
###########################################################
def read_input_file(file_path):
    # Open the file
    with open(file_path, "r") as file:
        # Read all lines from the file
        lines = file.readlines()

    # Initialize an empty list to store the values
    values = []

    # Iterate through each line in the file
    for line in lines:
        # Convert the string to an integer and append it to the list
        values.append(int(line.strip()))

    # Return the list of values
    return values

def check_values(values, preamble):
    # Check if values after index 25 can be obtained as the sum of two other values
    for i in range(preamble+1, len(values)):
        current_value = values[i]
        found = False
        # Check if current value can be obtained as the sum of two values within the preceding 25 elements
        for j in range(i - preamble, i):
            for k in range(j + 1, i):
                if values[j] + values[k] == current_value:
                    found = True
                    break
            if found:
                break
        # If current value cannot be obtained as the sum of two values, print it
        if not found:
            invalid_value = current_value
            return invalid_value

values = read_input_file('input.txt')
invalid_value=check_values(values, 25)
print(f"Value {invalid_value} cannot be obtained")

###########################################################
#Advent of code 2020
#Day9 - Part 2 
###########################################################

def find_contiguous_set(values, invalid_number):
    #iterate through all values
    for i in range(len(values)):
        total = values[i]
        #pick the other numbers of the set (skip the first)
        j = i + 1
        #sum all the values and check if they return the invalid number
        while total < invalid_number and j < len(values):
            total += values[j]
            j += 1
        if total == invalid_number:
            return values[i:j]
    return None

contiguous_set = find_contiguous_set(values, invalid_value)
print(f"Contiguous set that sums up to {invalid_value}:{contiguous_set}")
print('The smallest and the largest sum to', min(contiguous_set)+max(contiguous_set))
