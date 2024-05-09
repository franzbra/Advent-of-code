# -*- coding: utf-8 -*-
"""
Created on Wed May  8 14:04:35 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day7 - Parts 1 and 2
###########################################################

import re

#read the input file, create a dictionary with outer bags as keys and contained bags as values
def read_input_file(file_path):
    bags_dict = {}
    
    with open(file_path, 'r') as file:
        for line in file:
            if line.strip():
                outer_bag, inner_bags = re.match(r'(.+?) bags contain (.+)', line).groups()
                inner_bags_list = re.findall(r'(\d+) (.+?) bags?', inner_bags)
                bags_dict[outer_bag] = [(int(count), color) for count, color in inner_bags_list]
    
    return bags_dict


#Count how many bags are inside a certain bag labeled by its color
def resolve_inner_bags(bags_dict, bag_color):
    total = 0
    if bag_color not in bags_dict:
        return 0
    #loop through the values of a certain key (a bag of a certain color)
    for count, color in bags_dict[bag_color]:
        #total = count of inner bags + count of innermost bags (those which are nested)
        total += count + count * resolve_inner_bags(bags_dict, color)
    return total

#Find if a bag contains or not a shiny gold bag, returning True or False
def can_contain_shiny_gold(bags_dict, bag, memo):
    if bag in memo:
        return memo[bag]
    #iterate true the keys of the dictionary. If it directly contains or can contain a shiny bag, add it to the memo dictionary
    #_ to skip  the counts and just considering the colors
    if any(color == "shiny gold" or can_contain_shiny_gold(bags_dict, color, memo) for _, color in bags_dict[bag]):
        memo[bag] = True
        return True
    memo[bag] = False
    return False


def count_containing_shiny_gold(bags_dict):
    memo = {}
    count = 0
    for bag in bags_dict:
        #if the can contain function returns true, count the bag
        if can_contain_shiny_gold(bags_dict, bag, memo):
            count += 1
    return count


filename = "input.txt"
bags = read_input_file(filename)
count = count_containing_shiny_gold(bags)
print(f'One shiny gold bag can be found inside {count} bags')

result = resolve_inner_bags(bags, 'shiny gold')
print('There are', result, 'bags inside the shiny gold bag')
