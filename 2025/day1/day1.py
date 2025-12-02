# ====================================== #
# LIBRARIES
# ====================================== #
import os
import pandas as pd


# ====================================== #
# INPUTS
# ====================================== #
# set parameters
year = 2025
day = 1

# set file path
input_file_path = os.path.join("%d" % year, "day%d" % day, "input.csv")
# input_file_path = os.path.join("%d" % year, "day%d" % day, "example.csv")

# read inputs
inputs = pd.read_csv(input_file_path, header=None)
n_inputs = len(inputs)


# ====================================== #
# PART 1
# ====================================== #

# init
position = 50
positions = [position]

# loop over inputs
for k in range(n_inputs):
    
    # get input
    direction = inputs.iloc[k][0][0]
    ticks = int(inputs.iloc[k][0][1:])
    
    # apply rotation
    if direction == "R":
        position = (position + ticks) % 100
    elif direction == "L":
        position = (position - ticks) % 100
    
    # append position
    positions.append(position)

# compute solution
solution = positions.count(0)
print("Solution of part 1 is %s" % (solution))

# try 1 = 1071


# ====================================== #
# PART 2
# ====================================== #

# init
position = 50
positions = [position]
cpt = 0

# loop over inputs
for k in range(n_inputs):
    
    # display infos
    print("[%d] starting position = %d" % (k, position))
    
    # get input
    direction = inputs.iloc[k][0][0]
    ticks = int(inputs.iloc[k][0][1:])
    
    # apply right rotation and count 0 crossings
    if direction == "R":
        crossings = (position + ticks) // 100
        position = (position + ticks) % 100

    # apply left rotation and count 0 crossings
    elif direction == "L":
        
        # case where we land exactly on 0 (underestimation)
        if (position - ticks) % 100 == 0:
            crossings = abs((position - ticks) // 100) + 1
        else: 
            # case where we start from 0 (overestimation) 
            if position == 0:
                crossings = abs((position - ticks) // 100) - 1
            # general case
            else:
                crossings = abs((position - ticks) // 100)
        position = (position - ticks) % 100
        
    # increment 0 crossings
    cpt = cpt + crossings
    
    # display infos
    print("%s%d leads to position = %d - (crossings=%d, cpt=%d)" % (direction, ticks, position, crossings, cpt))
    
    # append position
    positions.append(position)

# compute solution
print("Solution of part 2 is %s" % (cpt))

# try 1 = 3094
# try 2 = 6671
# try 3 = 6149
# try 4 = 6700