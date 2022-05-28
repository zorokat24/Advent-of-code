# importing pandas
import pandas as pd
import numpy as np

# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 5\input_5.txt", header = None, sep = '\s+|,|->')
df = df.drop([2,3],axis=1)
df.columns = ['x1', 'y1', 'x2', 'y2']

max_value = max(df[['x1', 'y1', 'x2', 'y2']].max())
#print(max_value)
matrix = np.zeros(shape=(max_value, max_value))

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

print("Number of points where at least 2 lines overlap are : ", np.count_nonzero(matrix>=2))