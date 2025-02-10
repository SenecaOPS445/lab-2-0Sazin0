#!/usr/bin/env python3

# Author: MD IBNA SAIM SAZIN
# Author ID: 109405225
# Date Created: 2025/01/24

import sys

# Check if an argument was provided, and set the timer accordingly
if len(sys.argv) == 2:
    timer = int(sys.argv[1])  # Use the argument as the timer value
else:
    timer = 3  # Default to 3 if no argument is provided

# Countdown using a while loop
while timer > 0:
    print(timer)
    timer -= 1  # Decrement the timer by 1

print('blast off!')
