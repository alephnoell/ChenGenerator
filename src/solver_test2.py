# -*- coding: utf-8 -*-
"""
Created on Mon Jul 22 12:21:06 2019

@author: noela
"""

# -*- coding: utf-8 -*-

from tools.system_tools import run_command
from time import time


print(" === SIMPLE GENERATOR 2 ===")
print("This module will check Type 2 formulas.")
n = input("[Enter a value for max. n (≥ 1)] ---> n = ")
n = int(n)

filename = "./output_files/times" + "times_check_2_quabs.txt"

file = open(filename, 'w')

i = 0
times = 0
while i <= n:
    
    if i == 0:
        i = i + 1
    elif i in range(1, 200):
        i += 1
    elif i in range(200, 300):
        times = 5
        i += 5
    elif i in range(300, 500):
        times = 25
        i += 25
    else:
        times = 100
        i += 100
    
    if i > n:
        times = i - n
        for j in range(times -1):
            file.write("NOT CHECKED" + "\n")
        break
    else:
        for j in range(times -1):
            file.write("NOT CHECKED" + "\n")
        
    if i > n:
        break
        
    print("Checking on QUABS... (n = {})".format(i))
    
    t0 = time()
    run_command("./output_files/quabs ./output_files/type2_size{}.qcir".format(i))
    t = time() - t0
    
    #print(o)
    
    print("Complete! ({} s)".format(t))
    file.write(str(t) + "\n")  
    print("")
    
file.close()
    


