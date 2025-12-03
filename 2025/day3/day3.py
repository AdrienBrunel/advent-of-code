# ====================================== #
# LIBRARIES
# ====================================== #
import os
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
input_file_path = os.path.join("%d" % year, "day%d" % day, "input.csv")
# input_file_path = os.path.join("%d" % year, "day%d" % day, "example.csv")

# read inputs
# with open(input_file_path, "r") as file:
#     inputs = [line.replace("\n", "") for line in file]
# n_inputs = len(inputs)

# read inputs
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
            

# ====================================== #
# PART 2
# ====================================== #
# init
start_chrono = time.time()
joltages = []

joltage_length = 12

# loop over inputs
for k in range(n_inputs):
    
    digits = [int(digit) for digit in list(inputs.iloc[k, 0])]
    n_digits = len(digits)
    
    pos = 0
    current_joltage = []
    while len(current_joltage) != joltage_length:
        eligible_digits = digits[pos:(n_digits-(joltage_length-len(current_joltage)-1))]
        selected_digit_idx = np.argmax(eligible_digits)
        selected_digit = eligible_digits[selected_digit_idx]
        current_joltage.append(selected_digit)
        pos = pos+selected_digit_idx+1

    jultage = 0
    for k in range(len(current_joltage)):
        jultage = jultage + current_joltage[k]*10**(joltage_length-k-1)
    joltages.append(jultage)
    
# compute solution
solution = sum(joltages)
end_chrono = time.time()

# display solution
print("Solution of part 2 is %s" % (solution))
print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# try 1 : 173229689350551 (0.11s)