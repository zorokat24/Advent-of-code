# importing pandas
import pandas as pd
import numpy as np

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 6\input_6.txt").read().splitlines()

data = data[0].split(',')
data = [int(x) for x in data]
data = np.array(data)

print("Initial number of fishes : ", len(data))

for i in range(80):
    count = np.count_nonzero(data == 0)   # find number of fishes having 0 days left
    data = data - 1   # reduce internal timer of all fishes
    data = np.where(data == -1, 6, data)   # update 0 as for fishes
    to_add = np.full(count,8)   # add new fishes with internal timer as 8
    data = np.append(data, to_add) 

print("Number of fishes after 80 days : ", len(data))