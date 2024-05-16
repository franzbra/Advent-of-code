# -*- coding: utf-8 -*-
"""
Created on Thu May 16 09:44:48 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day12 - Part 1 
###########################################################

def read_file(file_path):
    with open(file_path, 'r') as file:
        commands = file.read().splitlines()
    
    split_commands = [(command[0], int(command[1:])) for command in commands]
    
    return split_commands


def traslation(N, S, E, W, direction, value):
    if direction == 'N':
        N+=value
    elif direction == 'S':
        S+=value
    elif direction == 'E':
        E+=value
    elif direction == 'W':
        W+=value

    return N, S, E, W


def rotation (orientation, direction, value):
    directions = ['N', 'W', 'S', 'E']
    index = directions.index(orientation)   
    step = int(value/90)
    if direction == 'R':
        index = (index - step) % len(directions)
    elif direction == 'L':
        index = (index + step) % len(directions)
    return directions[index]

def procede_forward (N,S,E,W,orientation, value):
    directions = ['N', 'S', 'E', 'W']
    values = [N,S,E,W]  
    index = directions.index(orientation)
    values[index] +=value
    return values
    
def Manhattan_distance(N,S,E,W):
    vertical_direction = abs(N-S)
    horizontal_direction = abs(W-E)
    return vertical_direction+ horizontal_direction

actions = read_file('prova.txt')
orientation = 'E'
location = [['N', 0], ['S', 0], ['E', 0],['W', 0]]

N, S, E, W = location[0][1], location[1][1], location[2][1], location[3][1]
for action in actions:
    direction, value = action
    if direction in ['N', 'S', 'W', 'E']:
        N, S, E, W = traslation(N,S,E,W,direction, value)
    elif direction in ['R','L']:
        orientation = rotation(orientation, direction, value)
    elif direction == 'F':
        N, S, E, W= procede_forward(N,S,E,W,orientation, value)


print('The Manhattan distance is', Manhattan_distance(N,S,E,W) )  

###########################################################
#Advent of code 2020
#Day12 - Part 2 
###########################################################
import numpy as np

def procede_forward_waypoint(x_boat, y_boat, x_w, y_w,forward_value):
    x_boat +=forward_value*x_w
    y_boat +=forward_value*y_w    
    return x_boat, y_boat



def rotation_matrix(direction, angle_degrees):
    if direction == 'R':
        angle_radians = np.radians(angle_degrees)
    elif direction == 'L':
        angle_radians = -np.radians(angle_degrees)
    return np.array([[np.cos(angle_radians), -np.sin(angle_radians)],
                     [np.sin(angle_radians), np.cos(angle_radians)]])


def traslation_waypoint(x,y, traslation_direction, traslation_value):
    if traslation_direction == 'N':
        y += traslation_value
    elif traslation_direction == 'S':
        y -= traslation_value
    elif traslation_direction == 'W':
        x += traslation_value
    elif traslation_direction == 'E':
        x -= traslation_value
    
    
    return x,y


actions = read_file('input.txt')

x_boat, y_boat = 0,0

x_w, y_w = -10,1

for action in actions:
    direction, value = action
    if direction in ['N', 'S', 'W', 'E']:
        x_w, y_w = traslation_waypoint(x_w, y_w, direction, value)
        print(x_w, y_w)
    elif direction in ['R','L']:
        rotation = rotation_matrix(direction, value)
        x_w,y_w = np.dot(rotation, (x_w,y_w)).astype(np.int64)
        print(x_w, y_w)
    elif direction == 'F':
      x_boat, y_boat = procede_forward_waypoint(x_boat, y_boat,x_w, y_w,value)
      print(x_boat, y_boat)
print('The Manhattan distance is',abs(x_boat) + abs(y_boat) )  
      