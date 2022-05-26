# importing pandas
import pandas as pd
import numpy as np

data = open(r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021\Day 4\input_4.txt", encoding='utf-8').read().splitlines()

#print(type(data[0]))
numbers_drawn = data[0].split(',')
#print(type(numbers_drawn))
numbers_drawn = [int(i) for i in numbers_drawn ]
#print(numbers_drawn)

number_boards = (len(data) - 1) // 6   # empty line along with 5 rows of numbers

def get_boards(data):
    data = data[1:]
    b_val = np.array_split(data, number_boards)
    b_val = np.delete(b_val, 0, axis = 1)
    new_boards = []
    for b in b_val:
        board = []
        for i in b:
            val = [int(j) for j in i.split(" ") if j!=""]
            board.append(val)
        new_boards.append(board)
    return np.array(new_boards)

boards = get_boards(data)
#print(boards.shape)

board = [ [1,1,0,0,1], 
          [1,0,0,0,1], 
          [1,1,0,0,0], 
          [1,1,0,0,1], 
          [1,1,0,0,1]  ]

def check_horizontal(board):
    return np.any(np.sum(board, axis=1) == 5)
#print(check_horizontal(board))

def check_vertical(board):
    return np.any(np.sum(board, axis=0) == 5)
#print(check_vertical(board))

def update_boards(n, boards):
    pass

def play_bingo(numbers_drawn, boards):
    for n in numbers_drawn:
        for i, board in enumerate(boards):
            
            print(board)
            break
        break

play_bingo(numbers_drawn, boards)