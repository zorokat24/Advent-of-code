# importing pandas
import pandas as pd
  
# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 1\input_1.txt", header = None)
  
numbers = df[0].to_list()
first = 0
count = 0

for i in numbers:
    if(i > first):
        count += 1
    first = i
print(count-1)