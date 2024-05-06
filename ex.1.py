# -*- coding: utf-8 -*-
"""
Created on Mon May  6 10:59:00 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day1 - Part 1
###########################################################

#Write a function that reads an input file

def read_text_file(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.readlines()
            float_array = [float(line.strip()) for line in content]
            return float_array
    except FileNotFoundError:
        print("File not found.")
  
#Write functions that finds values and avoid repetitions        
def find_pair(floats_array, target_sum):
    seen_numbers = set()  # Store seen numbers to avoid duplicates
    for number in floats_array:
        complement = target_sum - number
        if complement in seen_numbers:
            return number, complement
        seen_numbers.add(number)
    return None, None

#Read file and store values in an array
file_path = "input.txt"  
inpt = read_text_file(file_path)

if inpt:
    number1, number2 = find_pair(inpt, 2020)
    if number1 is not None and number2 is not None:
        print(f"{number1}+{number2}=2020")
        print("Their product is:", number1 * number2)
    else:
        print("No pair found with sum equal to 2020.")

##############################################################
#Day1 - Part 2
##############################################################
#Same as before, but with an additional loop

def find_triplet(floats_array, target_sum):
    seen_numbers = set(floats_array)  # Store seen numbers to avoid duplicates
    for i in range(len(floats_array)):
        for j in range(i + 1, len(floats_array)):
            complement = target_sum - (floats_array[i] + floats_array[j])
            if complement in seen_numbers:
                return floats_array[i], floats_array[j], complement
    return None, None, None

if inpt:
    number1, number2, number3 = find_triplet(inpt, 2020)
    if number1 is not None and number2 is not None and number3 is not None:
        print(f"{number1} + {number2}+{number3}=2020")
        print("Their product is:", number1 * number2 * number3)
    else:
        print("No triplet found with sum equal to 2020.")
