# -*- coding: utf-8 -*-
"""
Created on Mon May  6 18:30:04 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day2 - Part 1
###########################################################
count=0

# Read input from file
with open('input.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    parts = line.strip().split(' ')
    min_max, letter, password = parts[0].split('-'), parts[1][0], parts[2]
    letter_count = password.count(letter)
    if letter_count< int(min_max[0]) or letter_count>int(min_max[1]):
        continue
    else :
        count+=1    
print(f'Inside the database, only {count} passwords are valid out of {len(lines)}')

###########################################################
#Day2 - Part 2
###########################################################
count=0

for line in lines:
    parts = line.strip().split(' ')
    min_max, letter, password = parts[0].split('-'), parts[1][0], parts[2]
    letter1, letter2 = password[int(min_max[0])-1], password[int(min_max[1])-1]
    if letter1 == letter or letter2 == letter:
        if letter1 == letter2:
            continue       
        else :
            count+=1 
    else:
        continue
print(f'Inside the database, only {count} passwords are valid out of {len(lines)}')


