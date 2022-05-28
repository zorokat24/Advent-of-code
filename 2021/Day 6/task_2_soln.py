# importing pandas
import pandas as pd
import numpy as np
from collections import Counter

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 6\input_6.txt").read().splitlines()

data = data[0].split(',')
data = [int(x) for x in data]

df = Counter(data)
print(df)

for i in range(9):
    if i not in df:
        df[i] = 0

print(df)

print("Initial number of fishes : ", len(data))

for j in range(256):
    for i in range(9):
        df[i-1] = df[i]
    df[6] += df[-1]
    df[8] = df[-1]
    df[-1] = 0   

total = 0
for i in range(9):
    total += df[i]

print("Number of fishes after 256 days : ", total)