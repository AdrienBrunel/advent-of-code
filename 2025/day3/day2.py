# ====================================== #
# LIBRARIES
# ====================================== #
import os
import math
import numpy as np
import time

# ====================================== #
# INPUTS
# ====================================== #
# set parameters
year = 2025
day = 2

# set file path
input_file_path = os.path.join("%d" % year, "day%d" % day, "input.csv")
# input_file_path = os.path.join("%d" % year, "day%d" % day, "example.csv")

# read inputs
with open(input_file_path, "r") as file:
    inputs = [line.split(",") for line in file][0]
n_inputs = len(inputs)


# ====================================== #
# PART 1
# ====================================== #
# init
start_chrono = time.time()
invalid_ids = []

# loop over inputs
for k in range(n_inputs):
    
    # set range of ids
    range_start = int(inputs[k].split("-")[0])
    range_end = int(inputs[k].split("-")[1])
    ids = range(range_start, range_end + 1)
    
    # loop over ids
    for id in ids:

        # only consider id if even number of digits
        if ((math.floor(math.log10(id))+1) % 2 == 0):
            
            # separate id in two equal halves 
            id_first_half = str(id)[:len(str(id))//2]
            id_second_half = str(id)[len(str(id))//2:]
            
            if id_first_half == id_second_half:
                invalid_ids.append(id)
        
# compute solution
solution = sum(invalid_ids)
end_chrono = time.time()

# display solution
print("Solution of part 1 is %s" % (solution))
print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# try 1 : 23701357374  (1.7s)       
            
# ====================================== #
# PART 2
# ====================================== #
# init
start_chrono = time.time()
invalid_ids = []

# loop over inputs
for k in range(n_inputs):
    
    # set range of ids
    range_start = int(inputs[k].split("-")[0])
    range_end = int(inputs[k].split("-")[1])
    ids = range(range_start, range_end + 1)
    
    # loop over ids
    for id in ids:

        # get divisors of number of digits
        nb_digits = (math.floor(math.log10(id))+1)
        divisors = [div for div in range(1, nb_digits+1) if nb_digits % div == 0][1:]
        
        # detect possible repetition
        for nb_rep in divisors:
            pattern_length = nb_digits // nb_rep
            split_id = [str(id)[i:i+pattern_length] for i in range(0, nb_digits, pattern_length)]
            if((len(split_id)>1) and (len(np.unique(split_id))==1)):
                invalid_ids.append(id)
                break

# compute solution
solution = sum(invalid_ids)
end_chrono = time.time()

# display solution
print("Solution of part 2 is %s" % (solution))
print("Solution found in %.2f seconds" % (end_chrono - start_chrono))

# try 1 : 34284458938 (58.89s)