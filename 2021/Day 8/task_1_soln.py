# importing pandas
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 8\input_8.txt").read().splitlines()

count = 0
for l in data:
    line = l.split('|')
    input = line[0].strip().split(' ')
    output = line[1].strip().split(' ')
    d = {}
    for index,value in enumerate(input):
        d[index] = len(value)

    u = pd.Series(d.values()).value_counts()
    uni = []
    for i,j in enumerate(u):
        if(j==1):
            uni.append(u.index[i])

    for index,value in enumerate(output):
        if(len(value) in uni):
            count+=1
    
print("Number of unique segments in the output : ", count)