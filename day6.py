# -*- coding: utf-8 -*-
"""
Created on Tue May  7 17:08:37 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day6 - Part 1
###########################################################

with open("input.txt", "r") as file:
    content = file.read()

# Split the content by double newline to separate groups
groups = content.split("\n\n")

result_lists = []
yes_list = []

for group in groups:
    # Split the group by newline character ("\n") to get individual lines
    lines = group.split("\n")
    #create a set of unique characters
    unique_chars = set()
    result_lists.append(lines)
    for line in lines:
        #Store all the characters of the line without repetitions
        unique_chars.update(line)
    yes_list.append(len(unique_chars))

print('The summatory of yes is', sum(yes_list))

###########################################################
#Advent of code 2020
#Day6 - Part 2
###########################################################
result_lists = []
yes_list = []

for group in groups:
    lines = group.split("\n")   
    common_chars = set(lines[0]) #initiate first line as my check set

    for line in lines[1:]:
        
        # Convert the line into a set of characters so to use the intersection method
        line_chars = set(line)
        # Update common_chars to contain only the characters present in both lines
        common_chars.intersection_update(line_chars)    
    result_lists.append(common_chars)

for result in result_lists:
    yes_list.append(len(result))

print('The summatory of yes is', sum(yes_list))
    

