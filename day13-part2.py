# -*- coding: utf-8 -*-
"""
Created on Fri May 17 21:13:53 2024

@author: Francesco Brandoli
"""
###########################################################
#Advent of code 2020
#Day13 - Part 2 
###########################################################

import time 

start_time = time.time()


def read_input_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        number = int(lines[0].strip())
        bus_ids = [(bus_id) for bus_id in lines[1].strip().split(',')]
    return number, bus_ids

departure, bus_ids = read_input_file('input.txt')

#Consider that t+index≡1  (mod busid)
#Since MCD =1 for our pairs of ti, we can use this theorem 
def chinese_remainder_theorem(n, a):
    sum = 0
    prod = 1
    #Definition of N (see wiki)
    for ni in n:
        prod *= ni

    for ni, ai in zip(n, a):
        #calculate the (floor) division Ni
        Ni = prod // ni
        #find y = mul_inv(p, ni)
        #calculate the sum of xi=ai * y1*Ni
        sum += ai * mul_inv(Ni, ni) * Ni
    return sum % prod

#Multiplicative Inverse Function
#Euclid algorithm for the remainders see https://it.wikipedia.org/wiki/Algoritmo_esteso_di_Euclide
#-1 è l'inverso moltiplicativo di 20 modulo 7, cioè 20×(−1)≡1  (mod7)
def mul_inv(a, b):
    b0 = b
    #initial x y
    x, y = 0, 1
    if b == 1:
        return 1
    while a > 1:
        #floor division
        q = a // b
        #b becomes the remainder, if b =0, stop the iteration: the MCD is 1 (numbers are coprime)
        a, b = b, a % b
        #calculate x and y
        x, y = y - q * x, x
    if y < 0:
        y += b0
    return y

def find_earliest_timestamp(bus_ids):
    n = []
    a = []
    for i, bus_id in enumerate(bus_ids):
        if bus_id != 'x':
            n.append(int(bus_id))
            a.append(-i % int(bus_id))

    return chinese_remainder_theorem(n, a)

print(find_earliest_timestamp(bus_ids))

end_time = time.time()
execution_time = end_time - start_time
print(f"Execution time: {execution_time:.3f} s")

