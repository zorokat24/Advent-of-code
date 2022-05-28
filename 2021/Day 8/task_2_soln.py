# importing pandas
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 8\input_8.txt").read().splitlines()

def get_key(dict, val):
    for key, value in dict.items():
        if val == value:
            return key

digits = {0: 6, 1: 2, 2: 5, 3: 5, 4: 4, 5: 5, 6: 6, 7: 3, 8: 7, 9: 6}
total = 0

for l in data:
    line = l.split('|')
    input = line[0].strip().split(' ')
    output = line[1].strip().split(' ')

    encoded = {}
    for i in input:
        if(len(i) == 2):
            encoded[1] = sorted(i)
        elif(len(i) == 3):
            encoded[7] = sorted(i)
        elif(len(i) == 4):
            encoded[4] = sorted(i)
        elif(len(i) == 7):
            encoded[8] = sorted(i)

    for index,value in enumerate(input):
        if(len(value)==5):
            if(len( set(value) & set(encoded[1])) ==2):
                encoded[3] = sorted(value)
            elif(len( set(value) & set(encoded[4])) ==2):
                encoded[2] = sorted(value)
            else:
                encoded[5] = sorted(value)
        elif(len(value)==6):
            if(len( set(value) & set(encoded[4]) )==4):
                encoded[9] = sorted(value)
            elif(len( set(value) & set(encoded[1]) )==2):
                encoded[0] = sorted(value)
            else:
                encoded[6] = sorted(value)

    out_number = ''
    for index,value in enumerate(output):
        number = get_key(encoded, sorted(value))
        out_number += str(number)
    total += int(out_number)

print("Total sum of values in the output : ", total)