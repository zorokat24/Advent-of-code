# importing pandas
import pandas as pd
  
columns = ['command', 'value']
# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 2\input_2.txt", header = None, sep=' ', names = columns )

horizontal = 0
depth = 0

for index, row in df.iterrows():
    if(row['command'] == 'forward'):
        horizontal += row['value']
    elif(row['command'] == 'down'):
        depth += row['value']
    elif(row['command'] == 'up'):
        depth -= row['value']

out = horizontal * depth
print(out)