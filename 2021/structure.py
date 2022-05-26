# importing os module
import os
  
# Parent Directory path
parent_dir = r"C:\Users\Kat\Desktop\Advent\Advent-of-code\2021"
files = ['task_1', 'task_2', 'task_1_soln.py', 'task_2_soln.py']

for i in range(3,26):
    # Directory
    directory = "Day " + str(i)
    # Path
    path = os.path.join(parent_dir, directory)
    try: 
        os.mkdir(path)   # create directory
        for file in files:
            with open(os.path.join(path, file), 'w') as fp:   # create files
                pass
    except OSError as error: 
        print(error) 