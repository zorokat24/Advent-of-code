# importing pandas
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 7\input_7.txt").read().splitlines()
data = [int(x) for x in data[0].split(',')]

crabs = len(data)
min_fuel = float('inf')

print(min_fuel)

for position in tqdm(range(crabs)):
    align_position = position
    total_fuel = 0
    for c in data:
        diff = abs(c-align_position)
        fuel_needed = (diff*(diff+1))/2   # suum of this series 1,2,3,4...n is ( n*(n+1) / 2 )
        total_fuel += fuel_needed
    if(total_fuel<=min_fuel):
        min_fuel = total_fuel
        optimal_position = position

print("Total fuel needed : ", min_fuel)
print("Align position : ", optimal_position)