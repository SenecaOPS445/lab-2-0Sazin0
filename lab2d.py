#!/usr/bin/env python3
import sys

# Check the number of arguments
if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} name age")
    sys.exit()

# Assign command line arguments to variables
name = sys.argv[1]  # First argument is the name
age = sys.argv[2]  # Second argument is the age

# Print the message
print(f"Hi {name}, you are {age} years old.")
