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
#    print('the next jolt is',min_adapter_tuple[0])
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

#print(f'There are {count_one} differences of 1 and {count_three} differences of 3')

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

#modified version of previous function
def find_direct_jolt(bag, out):
    interval = [*range(out+1, out + 4)]
    fine_adapters = []
    for adapter in bag:
        if adapter in interval:
            fine_adapters.append([adapter,adapter-out])
#            print(adapter)
    return extract_first_elements(fine_adapters),len(fine_adapters)

bag= read_input_file('input.txt')
built_in_adapter = add_built_in_adapter(bag)
bag.append(built_in_adapter)
bag.sort()
charging_outlet = 0
count=1
counter_removal=0
pair_removal=0
number_subset=0
cumulative_combinations=[]
combination_per_subset=[]

while charging_outlet != built_in_adapter:
    jolts,n = find_direct_jolt(bag, charging_outlet)
    cumulative_combinations.append(total_combinations(n))
    bag_without_set = [item for item in bag if item not in jolts]
#    print(bag_without_set)
#    print(f'after {charging_outlet}, I can insert {jolts}')
#    print(f'there are {total_combinations(n)} ways to extract these numbers ')
    counter_removal =0
    if n>1 :
        number_subset+=1
       
    for i in jolts:
        cond1= i+1
        cond2 = i+2
        cond3 = i+3
        if total_combinations(n) == 1:
            continue
        if cond1 in bag_without_set or cond2 in bag_without_set or cond3 in bag_without_set:
            print(f"{i} is ok, there is {cond1} or {cond2} or {cond3}")
        else:
#            print(f"but combinations with {i} alone can't be considered")
            counter_removal +=1
            if i != min(jolts):
                counter_removal +=1
#    print(f'so the combinations are {(total_combinations(n)-counter_removal)}')        
    count*= (total_combinations(n)-counter_removal)
#    print('total count:', count)

    charging_outlet = max(jolts)
print(f'There are {count-(number_subset-1)*counter_removal} way of arranging the jolts')