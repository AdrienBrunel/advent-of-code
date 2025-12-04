# ====================================== #
# LIBRARIES
# ====================================== #
import os
import numpy as np
import time

# ====================================== #
# INPUTS
# ====================================== #
# set parameters
year = 2025
day = 4

# set file path
input_file_path = os.path.join("%d" % year, "day%d" % day, "input.csv")
# input_file_path = os.path.join("%d" % year, "day%d" % day, "example.csv")

# read inputs
with open(input_file_path, "r") as file:
    inputs = [line.replace("\n", "") for line in file]
n_inputs = len(inputs)


# ====================================== #
# PREPROCESSING
# ====================================== #
n_rows = len(inputs)
n_cols = len(list(inputs[0]))
rolls = np.zeros((n_rows, n_cols)) 
for i in range(n_rows):
    for j in range(n_rows):
        if list(inputs[i])[j]=="@":
            rolls[i,j] = 1


# ====================================== #
# PART 1
# ====================================== #
# init
start_chrono = time.time()

# loop over rows and columns
accessible_rolls=[]
for i in range(n_rows):
    for j in range(n_cols):
        if rolls[i,j] == 1:
            neighboring_rolls = rolls[max(0, i-1):min(n_rows, i+2),max(0, j-1):min(n_cols, j+2)]
            if neighboring_rolls.sum() <= 4:
                accessible_rolls.append((i,j))
            
# compute solution
solution = len(accessible_rolls)
end_chrono = time.time()

# display solution
print("Solution of part 1 is %s" % (solution))
print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# try 1 : 1419  (0.12s)       
            

# ====================================== #
# PART 2
# ====================================== #
# init
start_chrono = time.time()

# loop over rows and columns
accessible_rolls=[]
total_accessible_rolls = []
iteration = 0
while((len(accessible_rolls)>0) | (iteration==0)):
    iteration = iteration + 1 
    accessible_rolls=[]
    for i in range(n_rows):
        for j in range(n_cols):
            if rolls[i,j] == 1:
                neighboring_rolls = rolls[max(0, i-1):min(n_rows, i+2),max(0, j-1):min(n_cols, j+2)]
                if neighboring_rolls.sum() <= 4:
                    accessible_rolls.append((i,j))
                    total_accessible_rolls.append((i,j))
    rolls[[pos[0] for pos in accessible_rolls], [pos[1] for pos in accessible_rolls]] = 0
    # print("Iteration %d : %d accessible rolls found" % (iteration, len(accessible_rolls)))
        
# compute solution
solution = len(total_accessible_rolls)
end_chrono = time.time()

# display solution
print("Solution of part 2 is %s" % (solution))
print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# try 1 : 8739 (1.36s)