# importing pandas
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 10\input_10.txt").read()

data = [ line for line in data.splitlines()]

error_points = {')':3, ']':57, '}':1197, '>':25137}
open_char = ['(', '[', '{', '<']


total = 0
for line in data:
    characters = []
    illegal_char = ''
    for char in line:
        if(char in open_char):
            characters.append(char)
        elif(char in ')'):
            if(characters.pop() != '('):
                illegal_char = ')'
                break
        elif(char in ']'):
            if(characters.pop() != '['):
                illegal_char = ']'
                break
        elif(char in '}'):
            if(characters.pop() != '{'):
                illegal_char = '}'
                break
        elif(char in '>'):
            if(characters.pop() != '<'):
                illegal_char = '>'
                break
        else:
            continue
    if(illegal_char != ''):
        total += error_points[illegal_char]

print("Total syntax error score for those errors : ", total)