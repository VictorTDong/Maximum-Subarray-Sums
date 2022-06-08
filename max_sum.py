"""
Name: Victor Dong
Purpose: Find the maximum subarray sum between two indices
Implementation: Base case - Array size = 1
                            return the 0'th element of the array
                Recursive case - split array in half and recurse on the left and right half returning
                                 1. The maximum left-aligned sum
                                 2. The maximum right-aligned sum
                                 3. The maximum subarray sum
                                 4. The sum of all elements in the array

         ** Algorithm taken from lecture **
         ** Some code was referenced from https://docs.python.org/3/library/csv.html and https://www.w3schools.com/python/python_ref_list.asp (Reading in from csv and python list) **
"""
import csv
import sys

def max_subarray(array):
    # Base case
    if (len(array) == 1):
        return [array[0], array[0], array[0], array[0]]

    # Recursive cases
    mid_index = len(array)//2
    left_array = max_subarray(array[:mid_index]) # Left half
    right_array = max_subarray(array[mid_index:]) # Right half

    max_left = max(left_array[0], left_array[3] + right_array[0])

    max_right = max(right_array[1], right_array[3] + left_array[1])

    max_sum = max(left_array[2], right_array[2], left_array[1] + right_array[0])

    sum = left_array[3] + right_array[3]

    return [max_left, max_right, max_sum, sum]



numberOfArgs = len(sys.argv)
start = int(sys.argv[2])
end = int(sys.argv[3])

# Checks for correct input
if numberOfArgs < 4 or int(sys.argv[2]) <= 0 and int(sys.argv[3]) > 9999 or int(sys.argv[3]) <= 0 or int(sys.argv[3]) < int(sys.argv[2]) :
    print("Invalid arguments... \nUsage: python max_sum.py [filename] [start time] [end time]")

else:
    numbers = []

    with open(sys.argv[1], 'r') as file:
        for row in csv.reader(file, skipinitialspace=True):
            numbers.append(int(row[0]))

# If the start and end index is the same, then just output that number
    if(start == end):
        max_sum_subarray = [numbers[start], numbers[start], numbers[start], numbers[start]]
    if (len(numbers) == 0):
        max_sum_subarray = [0, 0, 0, 0]
    else:
        max_sum_subarray = max_subarray(numbers[start:end])

    print("The maximum sum between", start, "-", end, "is:", max(max_sum_subarray))


