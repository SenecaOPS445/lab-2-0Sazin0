#!/usr/bin/env python3

# Author: MD IBNA SAIM SAZIN
# Author ID: 109405225
# Date Created: 2025/01/24

import sys

# Ensure that the user provides at least one argument
if len(sys.argv) != 2:
    print("Usage: ./lab2f.py <timer_value>")
    sys.exit(1)

# Convert the first argument to an integer and assign it to timer
timer = int(sys.argv[1])

# While loop that counts down from the timer value
while timer > 0:
    print(timer)
    timer -= 1  # Decrease the timer by 1

print('blast off!')

