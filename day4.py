# -*- coding: utf-8 -*-
"""
Created on Tue May  7 12:24:28 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day4 - Part 1
###########################################################
#Create a list of dictionary
def read_input_file(file_path):
    passports = []
    
    with open(file_path, 'r') as file:
        #create dictionary
        passport = {
        'byr': None,  # Birth Year
        'iyr': None,  # Issue Year
        'eyr': None,  # Expiration Year
        'hgt': None,  # Height
        'hcl': None,  # Hair Color
        'ecl': None,  # Eye Color
        'pid': None,  # Passport ID
        'cid': None   # Country ID
        }

        for line in file: #read through the file and consider the passport to end at blanck line
            line = line.strip()
            if line:
                fields = line.split()
                for field in fields:
                    key, value = field.split(':')
                    passport[key] = value
            else:
                passports.append(passport)
                passport = passport = {
                'byr': None,  # Birth Year
                'iyr': None,  # Issue Year
                'eyr': None,  # Expiration Year
                'hgt': None,  # Height
                'hcl': None,  # Hair Color
                'ecl': None,  # Eye Color
                'pid': None,  # Passport ID
                'cid': None   # Country ID
                }
        if passport:
            passports.append(passport)
    return passports

#Function that iterates through all dictionaries and looks for missing keys following
#the rules of the exercise
def emptypass(passports):
    empty_pass = []
    for passport in passports:
        #Check if some key reports None value
        missing_keys = [key for key, value in passport.items() if value is None]
        if len(missing_keys) == 1 and "cid" in missing_keys:
            continue  # Skip passports with only "cid" missing
        elif missing_keys:
            empty_pass.append(passport)
    return empty_pass

file_path = "input.txt" 
passports = read_input_file(file_path)
incomplete_pass = emptypass(passports)
print(f"We found {len(passports)-len(incomplete_pass)} valid passports")

###########################################################
#Advent of code 2020
#Day4 - Part 2
###########################################################
import re

#Modify the first function including the new restrictions
def read_input_file(file_path):
    passports = []
    
    with open(file_path, 'r') as file:
        #create dictionary
        passport = {
        'byr': None,  # Birth Year
        'iyr': None,  # Issue Year
        'eyr': None,  # Expiration Year
        'hgt': None,  # Height
        'hcl': None,  # Hair Color
        'ecl': None,  # Eye Color
        'pid': None,  # Passport ID
        'cid': None   # Country ID
        }

        for line in file: #read through the file and consider the passport to end at blanck line
            line = line.strip()
            if line:
                fields = line.split()
                for field in fields:
                    key, value = field.split(':')

                    #Add all new conditions                    
                    if key == 'byr': 
                        if int(value) <1920 or int(value) >2002 or len(value)!=4:
                            continue
                    
                    elif key == 'iyr': 
                        if int(value) < 2010 or int(value) >2020 or len(value)!=4:
                            continue
                                        
                    elif key == 'eyr': 
                        if int(value) < 2020 or int(value) >2030 or len(value)!=4:
                            continue
                    
                    elif key == "hgt":
                        if not value.endswith("cm") and not value.endswith("in"):
                            continue
                        elif value.endswith("cm"):
                            height_cm = int(value[:-2])
                            if height_cm < 150 or height_cm > 193:
                                continue
                        elif value.endswith("in"):
                            height_in = int(value[:-2])
                            if height_in < 59 or height_in > 76:
                                continue                           
                            
                    elif key == "hcl":
                        if not re.match(r'^#[0-9a-f]{6}$', value):
                            continue
                    
                    elif key == "ecl" and value not in {"amb", "blu", "brn", "gry", "grn", "hzl", "oth"}:
                        continue                        
                    
                    elif key == "pid":
                        if len(value)!=9:
                          #  print(key, 'error', value)
                            continue
                        else: print('Correct', value)
                    passport[key] = value       
            else:
                passports.append(passport)
                passport = passport = {
                'byr': None,  # Birth Year
                'iyr': None,  # Issue Year
                'eyr': None,  # Expiration Year
                'hgt': None,  # Height
                'hcl': None,  # Hair Color
                'ecl': None,  # Eye Color
                'pid': None,  # Passport ID
                'cid': None   # Country ID
                }
        if passport:
            passports.append(passport)
    return passports



def emptypass(passports):
    empty_pass = []
    for passport in passports:
        #Check if some key reports None value
        missing_keys = [key for key, value in passport.items() if value is None]
        if len(missing_keys) == 1 and "cid" in missing_keys:
            continue  # Skip passports with only "cid" missing
        elif missing_keys:
            empty_pass.append(passport)
    return empty_pass

passports = read_input_file(file_path)
incomplete_pass = emptypass(passports)
print(f"We found {len(passports)-len(incomplete_pass)} valid passports")



