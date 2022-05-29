# importing pandas
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 10\input_10.txt").read()

data = [ line for line in data.splitlines()]

error_points = {'(':1, '[':2, '{':3, '<':4}
open_char = ['(', '[', '{', '<']

score = []

for line in data:
    characters = []
    total = 0
    flag = False
    for char in line:
        if(char in open_char):
            characters.append(char)
        elif(char in ')'):
            if(characters.pop() != '('):
                flag = True
                break
        elif(char in ']'):
            if(characters.pop() != '['):
                flag = True
                break
        elif(char in '}'):
            if(characters.pop() != '{'):
                flag = True
                break
        elif(char in '>'):
            if(characters.pop() != '<'):
                flag = True
                break
        else:
            continue

    characters = characters[::-1]

    if(flag == False):
        for i in characters:
            total *= 5
            total += error_points[i]
        score.append(total)

score.sort()
out = score[int(len(score)/2)]

print("The middle score after making corrections : ", out)