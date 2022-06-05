"""
Name: Victor Dong
Purpose: 
Implementation: Base case - Array size = 0
                                return 0
                            Array size = 1
                                return the 0'th element of the array
                Recursive case - split array in half and recurse on the left and right half returning the max
         ** Algorithm taken from lecture **
         ** Some code was referenced from https://docs.python.org/3/library/csv.html and https://www.w3schools.com/python/python_ref_list.asp (Reading in from csv and python list) **
"""
import csv
import sys

def find_max(L):
    mid_index = len(L)//2
    if len(L) == 0:
        return 0
    elif len(L) == 1:
        return L[0]

    left = find_max(L[:mid_index])
    right = find_max(L[mid_index:])

    left_half = right_half = 0
    # to the left
    accum = 0
    for x in L[mid_index-1::-1]:
        accum += x
        left_half = max(left_half, accum)

    # to the right
    accum = 0
    for x in L[mid_index:]:
        accum += x
        right_half = max(right_half, accum)

    return max(left, right, left_half + right_half)

# Checks for correct input
numberOfArgs = len(sys.argv)
if numberOfArgs < 4 or (int(sys.argv[2]) <= 0 and int(sys.argv[3]) >= 9999):
    print("Invalid arguments... \nUsage: python max_sum.py [filename] [start time] [end time]")

else:
    numbers = []
    sum = 0
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    with open(sys.argv[1], 'r') as file:
        for row in csv.reader(file, skipinitialspace=True): # Converts data to tuple of integers
            numbers.append(int(row[0]))

    print("The maximum sum between", start, "-", end, "is:", find_max(numbers[start:end]))


