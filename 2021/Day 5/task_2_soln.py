# importing pandas
from turtle import right
import pandas as pd
import numpy as np

# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 5\input_5.txt", header = None, sep = '\s+|,|->')
df = df.drop([2,3],axis=1)
df.columns = ['x1', 'y1', 'x2', 'y2']

max_value = max(df[['x1', 'y1', 'x2', 'y2']].max())
print(max_value)

matrix = np.zeros(shape=(max_value+1, max_value+1))

for i,row in df.iterrows():
    if(row['x1'] == row['x2']):   # vertical
        start = min(row['y1'], row['y2'])
        end = max(row['y1'], row['y2'])
        r = row['x1']
        matrix[start:end+1, r] = matrix[start:end+1, r] + 1
    elif(row['y1'] == row['y2']):   # horizontal
        start = min(row['x1'], row['x2'])
        end = max(row['x1'], row['x2'])
        r = row['y1']
        matrix[r, start:end+1] = matrix[r, start:end+1] + 1
    else:   # diagonal
        diff = abs(row['x1'] - row['x2'])
        for j in range(diff+1):
            if(row['x1'] < row['x2']):
                if(row['y1'] < row['y2']):
                    matrix[row['x1']+j, row['y1']+j] = matrix[row['x1']+j, row['y1']+j] + 1
                else:
                    matrix[row['x1']+j, row['y1']-j] = matrix[row['x1']+j, row['y1']-j] + 1
            else:
                if(row['y1'] < row['y2']):
                    matrix[row['x1']-j, row['y1']+j] = matrix[row['x1']-j, row['y1']+j] + 1
                else:
                    matrix[row['x1']-j, row['y1']-j] = matrix[row['x1']-j, row['y1']-j] + 1

print("Number of points where at least 2 lines overlap are : ", np.count_nonzero(matrix>1))

import numpy as np

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 5\input_5.txt").read().splitlines()
data = [x.replace(' -> ', ',').split(',') for x in data]
data = [list(map(int, x)) for x in data]

size = max(max(x) for x in data) + 1
diagram = np.zeros((size, size), dtype=int)

for x1, y1, x2, y2 in data:
    if x1 == x2 or y1 == y2:
        x1, y1, x2, y2 = min(x1, x2), min(y1, y2), max(x1, x2), max(y1, y2)
        diagram[y1: y2+1, x1: x2+1] += 1
    else:
        x = range(x1, x2+1) if x1 <= x2 else range(x1, x2-1, -1)
        y = range(y1, y2+1) if y1 <= y2 else range(y1, y2-1, -1)
        for i, j in zip(x, y):
            diagram[j, i] += 1

print(np.sum(diagram > 1))