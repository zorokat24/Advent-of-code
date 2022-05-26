# importing pandas
from pickle import NONE
import pandas as pd
  
# read text file into pandas DataFrame
df = pd.read_csv(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 3\input_3.txt", header = None, names = ['binary'], converters={0:str, 1:str})
df = df.astype({"binary": str})
df = df['binary'].str.split('', expand=True)
df.drop(columns=[0,13],inplace=True)

print(df)

def find_gamma_rate(df):
    gamma = ''
    for col in df.columns:
        c = df[col].value_counts()
        max = c.index[0]
        gamma += max
    return int(gamma, 2)

def find_inverse(gamma):
    gamma = bin(gamma)
    gamma = str(gamma)
    gamma = gamma[2:]
    epsilon = ''
    for num in gamma:
        if(num=='1'):
            epsilon+='0'
        else:
            epsilon+='1'
    return int(epsilon, 2)

gamma = find_gamma_rate(df)

epsilon = find_inverse(gamma)

power = gamma * epsilon

print(power)