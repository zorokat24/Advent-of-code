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
    return np.any(np.sum(board, axis=1) == -5)
#print(check_horizontal(board))

def check_vertical(board):
    return np.any(np.sum(board, axis=0) == -5)
#print(check_vertical(board))

def play_bingo(numbers_drawn, boards):
    boards_won = []
    for n in numbers_drawn:
        for i, board in enumerate(boards):
            X, Y = board.shape
            for x in range(X):
                for y in range(Y):
                    if board[x, y] == n:
                        board[x, y] = -1
                        if check_horizontal(board):                        
                            if(i not in boards_won):
                                boards_won.append(i)
                                if(len(boards_won) == number_boards):
                                    return board, n 
                            boards[i] = np.full((5,5), 0)
                        elif(check_vertical(board)):
                            if(i not in boards_won):                       
                                boards_won.append(i)
                                if(len(boards_won) == number_boards):
                                    return board, n 
                            boards[i] = np.full((5,5), 0) 
                                                              
winning_board, winning_number = play_bingo(numbers_drawn, boards)

print(winning_board)
print(winning_number)

def find_score(winning_board, number):
    sum = 0
    for row in winning_board:
        for val in row:
            if(val != -1):
                sum += val
    score = sum * number
    print("Score ", score)
    return score

score = find_score(winning_board, winning_number)