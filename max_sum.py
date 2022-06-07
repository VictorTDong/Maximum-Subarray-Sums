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
"""
def max_right(array):
    right_array = 0

    current_sum = 0
    for x in array[::-1]:
        current_sum += x
        right_array = max(right_array, current_sum)

    return right_array

def max_left(array):
    left_array = 0

    current_sum = 0
    for x in array[:]:
        current_sum += x
        left_array = max(left_array, current_sum)

    return left_array

"""
def max_left(array):
    if len(array) == 0:
        return 0
    else:
        mid_index = len(array)//2

        return max(max_left(array[:mid_index]) + array[0], sum(array[:mid_index]) + max_left(array[mid_index:]) + array[0])

def max_right(array):
    if len(array) == 0:
        return 0
    else:
        mid_index = len(array)//2

        return max(max_right(array[mid_index:]) + array[mid_index], sum(array[mid_index:]) + max_right(array[:mid_index]) + array[mid_index])



def max_sum(array):
    mid_index = len(array)//2

    if len(array) == 0:
        return 0
    elif len(array) == 1:
        return array[0]

    return max(max_sum(array[:mid_index]), max_sum(array[mid_index:]),  max_right(array[:mid_index]) + max_left(array[mid_index:]))

# Checks for correct input
numberOfArgs = len(sys.argv)
if numberOfArgs < 4 or (int(sys.argv[2]) <= 0 and int(sys.argv[3]) >= 9999):
    print("Invalid arguments... \nUsage: python max_sum.py [filename] [start time] [end time]")

else:
    numbers = []
    sum = 0
    start = int(sys.argv[2])
    end = int(sys.argv[3])

    
    sys.setrecursionlimit(999999)

    print(sys.getrecursionlimit())

    with open(sys.argv[1], 'r') as file:
        for row in csv.reader(file, skipinitialspace=True): # Converts data to tuple of integers
            numbers.append(int(row[0]))

    print("The maximum sum between", start, "-", end, "is:", max_sum(numbers[start:end]))


