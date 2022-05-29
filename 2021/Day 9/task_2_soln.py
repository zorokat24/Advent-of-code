# importing pandas
from re import L
import pandas as pd
import numpy as np
from collections import Counter
from tqdm import tqdm

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 9\input_9.txt").read()

l = [ [int(num) for num in line] for line in data.splitlines()]
l = np.array(l)

from skimage.measure import label, regionprops

def find_basin(l):
    size = [r.area for r in regionprops(label(l < 9, connectivity=1))]
    largest_3 = sorted(size)[-3:]
    return np.prod(largest_3)

out = find_basin(l)
    
print("The largest 3 basins multiplied by their size together : ", out)