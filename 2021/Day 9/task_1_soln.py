# importing pandas
from re import L
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 9\input_9.txt").read()

l = [ [int(num) for num in line] for line in data.splitlines()]
l = np.array(l)

# add a padded layer of 10 around the matrix to treat all points with 4 adjacent locations
l = np.pad(l, pad_width=1, constant_values=10)

rows = len(l)
cols = len(l[0])

low_points = []

# corners
for i in range(rows):
    for j in range(cols):
        if(i==0 or j==0 or i==rows-1 or j==rows-1):
            continue
        else:
            num = l[i][j]
            # check top, bottom, left and right
            if( (num < l[i-1][j]) and (num < l[i+1][j]) and (num < l[i][j-1]) and (num < l[i][j+1]) ):
                low_points.append(num)

print("Total number of low points : ", len(low_points))

low_points = np.array(low_points)
low_points = low_points + 1
risk = np.sum(low_points)

print("Risk level : ", risk)