# ====================================== #
# LIBRARIES
# ====================================== #
import os
import math
import numpy as np
import pandas as pd
import time

# ====================================== #
# INPUTS
# ====================================== #
# set parameters
year = 2025
day = 3

# set file path
# input_file_path = os.path.join("%d" % year, "day%d" % day, "input.csv")
input_file_path = os.path.join("%d" % year, "day%d" % day, "example.csv")

# read inputs
# with open(input_file_path, "r") as file:
#     inputs = [line.replace("\n", "") for line in file]
# n_inputs = len(inputs)

inputs = pd.read_csv(input_file_path, header=None).astype(str)
n_inputs = len(inputs)


# ====================================== #
# PART 1
# ====================================== #
# init
start_chrono = time.time()
joltages = []

# loop over inputs
for k in range(n_inputs):
    
    digits = [int(digit) for digit in list(inputs.iloc[k, 0])]
    n_digits = len(digits)
    max_joltage = -1
    for k in range(n_digits-1):
        digit = digits[k]
        current_joltage = digit*10 + np.flip(np.sort(digits[(k+1):]))[0]
        if current_joltage > max_joltage:
            max_joltage = current_joltage
    joltages.append(max_joltage)
    
# compute solution
solution = sum(joltages)
end_chrono = time.time()

# display solution
print("Solution of part 1 is %s" % (solution))
print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# try 1 : 17745  (0.19s)       
            

# # ====================================== #
# # PART 2
# # ====================================== #
# # init
# start_chrono = time.time()
# joltages = []

# joltage_length = 12

# # loop over inputs
# for k in range(n_inputs):
    
#     digits = [int(digit) for digit in list(inputs.iloc[k, 0])]
#     n_digits = len(digits)
#     max_joltage = -1
    
#     pos = 0
#     current_joltage = []
#     while len(current_joltage) != joltage_length:        
#         availabe_digits = digits[pos:]
#         available_space = joltage_length - len(current_joltage)
#         max_idx = np.flip(np.argsort(availabe_digits))[0]
#         if ((len(availabe_digits) - max_idx) > available_space):
#             digit = availabe_digits[max_idx]
#             current_joltage.append(digit)
#         pos = pos+1
#         print(pos)
    
#     for k in range(n_digits-1):
#         digit = digits[k]
        
#         cpt = 0
#         if n_digits - idx <= joltage_length:
            
#         np.flip(np.sort(digits[(k+1):]))[0]
#         if current_joltage > max_joltage:
#             max_joltage = current_joltage
#     joltages.append(max_joltage)

#     # idx = np.flip(np.argsort(digits))
#     # sorted_digits = [digits[i] for i in idx]
#     # joltage = int("".join([str(digits[i]) for i in np.sort(idx[0:2])]))
#     # joltages.append(joltage)
        
# # compute solution
# solution = sum(joltages)
# end_chrono = time.time()

# # display solution
# print("Solution of part 2 is %s" % (solution))
# print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# # try 1 : 34284458938 (58.89s)