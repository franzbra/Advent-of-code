# -*- coding: utf-8 -*-
"""
Created on Fri May 17 11:54:43 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day13 - Part 1 
###########################################################
import time

start_time = time.time()


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        number = int(lines[0].strip())
        bus_ids = [int(bus_id) for bus_id in lines[1].strip().split(',') if bus_id != 'x']
    return number, bus_ids

departure, buses = read_input_file('input.txt')
valid_times = []
for t in range(departure, departure+10):
    for bus in buses:
        if t%bus == 0:
            valid_times.append((t,bus))
waiting =  min(valid_times, key=lambda x: x[0])[0]-departure
bus_id =min(valid_times, key=lambda x: x[0])[1]
print('We have to wait', min(valid_times, key=lambda x: x[0])[0]-departure, 'minutes')
print('The number wanted is',waiting*bus_id )

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} s")
