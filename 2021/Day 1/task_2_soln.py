# import os
# import sys

# with open(os.path.join(sys.path[0], "input_2.txt"), "r") as fp:
#     Lines = fp.readlines()
# importing pandas
import numpy as np
import pandas as pd
  
# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 1\input_1.txt", header = None)
  
numbers = df[0].to_list()

step = 3
first = 0
count = 0

for i in range(len(numbers)):
    second = np.sum(numbers[i:i+step])
    if(second > first):
        count += 1
    first = second
print(count-1)