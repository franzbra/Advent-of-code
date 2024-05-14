# -*- coding: utf-8 -*-
"""
Created on Tue May 14 08:40:02 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day10 - Part 1 
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

def add_built_in_adapter(bag):
    return max(bag)+3

def count_jolt_difference(differences, counter):
    counter +=1
    return counter


def find_direct_jolt(bag, out):
    interval = [*range(out+1, out + 4)]
    fine_adapters = []
    for adapter in bag:
        if adapter in interval:
            fine_adapters.append([adapter,adapter-out])
    min_adapter_tuple = min(fine_adapters, key=lambda x: x[0])
    print('the next jolt is',min_adapter_tuple[0])
    return min_adapter_tuple[0], min_adapter_tuple[1]



bag= read_input_file('prova1.txt')
built_in_adapter = add_built_in_adapter(bag)
bag.append(built_in_adapter)
charging_outlet = 0
count_one=0
count_three=0
final_adapter_list = []


while charging_outlet != built_in_adapter:
    join, difference = find_direct_jolt(bag, charging_outlet)
    if difference == 1:
        count_one = count_jolt_difference(difference, count_one)
    elif difference ==3:
        count_three = count_jolt_difference(difference, count_three)
    final_adapter_list.append(join)
    charging_outlet = join

print(f'There are {count_one} differences of 1 and {count_three} differences of 3')

###########################################################
#Advent of code 2020
#Day10 - Part 2 
#DA FARE!!!!!!!!!!
###########################################################

#import tools for combinatory calculations
from itertools import combinations
import math


#in how many unique ways can I extract k elements out of n?
def total_combinations(n):
    total = 0
    for k in range(1, n + 1):
        total += len(list(combinations(range(n), k)))
    return total
       
def extract_first_elements(list_of_lists):
    return [sublist[0] for sublist in list_of_lists]

#modify this function
def find_direct_jolt(bag, out):
    interval = [*range(out+1, out + 4)]
    fine_adapters = []
    for adapter in bag:
        if adapter in interval:
            fine_adapters.append([adapter,adapter-out])
    return extract_first_elements(fine_adapters),len(fine_adapters)

bag= read_input_file('prova1.txt')
built_in_adapter = add_built_in_adapter(bag)
bag.append(built_in_adapter)
charging_outlet = 0
count=1

while charging_outlet != built_in_adapter:
    jolts,n = find_direct_jolt(bag, charging_outlet)
    count*= total_combinations(n)
    print(count, jolts, n)
    for i in jolts:
        if i+3 not in bag:
            count-=1
        
            
        
        #combination_per_subset.append(total_combinations(n))
    charging_outlet = jolts[0]
        
#tot= total_combinations(math.prod(combination_per_subset))
print(f'There are {count} way of arranging the jolts')