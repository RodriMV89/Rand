# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:23:42 2023

@author: Rodrigo
"""

# intermediate python
# random numbers

import numpy as np
np.random.rand()

np.random.seed(123)
np.random.rand()

# example
np.random.seed(123)
coin = np.random.randint(0,2)
print(coin) # for testing
if coin == 0:
    print("heads")
else:
    print("tails")

# example
import numpy as np

np.random.seed(1)
np.random.rand()

np.random.randint(2)

# list = []
# if coin == 0:
#     list.append(coin)
#     print(coin)
# else:
#     print(coin)
# list

# roll the dice
# Import numpy and set seed
import numpy as np
np.random.seed()

# Use randint() to simulate a dice
print(np.random.randint(1, 7))

# Use randint() again
print(np.random.randint(1, 7))

# NumPy is imported, seed is set

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice == 3 and 4 or 5 :
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# Starting step
step = 50

# Roll the dice
dice = np.random.randint(1,7)

# Finish the control construct
if dice <= 2 :
    step = step - 1
elif dice == (3,6):
    step = step + 1
else :
    step = step + np.random.randint(1,7)

# Print out dice and step
print(dice)
print(step)

# 
np.random.seed(123)
outcomes = []
tails = [0]

for x in range(10):
    coin = np.random.randint(2)
    tails.append(tails[x] + coin)
    if coin == 0:
        outcomes.append("heads")
    else:
        outcomes.append("tails")
print(outcomes)
print(tails)
len(outcomes)

for x in range(10):
    coin = np.random.randint(2)
    tails.append(tails[x] + coin)
print(tails)

# Initialize random_walk
random_walk = [0]
# Complete the ___
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        # Replace below: use max to make sure step can't go below 0
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
print(step)

# Initialization
random_walk = [0]

for x in range(100) :
    step = random_walk[-1]
    dice = np.random.randint(1,7)

    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    random_walk.append(step)

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt

# Plot random_walk
plt.plot(random_walk)
plt.show()