# Find the number of seconds it takes to run any operation
# Output it in a format that can be graphed in google sheets

from time import time
import random



# STRETCH: implement the Bubble Sort function below
def bubble_sort( arr ):
    # Repeat this until you make it through an entire pass without any swaps.
    is_sorted = False
    while not is_sorted:
        is_sorted = True
        # Walk through the array
        for i in range(len(arr) - 1):
            # comparing each element to its right neighbor.
            # If it's smaller than that neighbor,
            if arr[i] > arr[i + 1]:
                # swap the elements.
                arr[i], arr[i+1] = arr[i+1], arr[i]
                is_sorted = False
    # return arr



# TO-DO: implement the Insertion Sort function below
def insertion_sort( arr ):
    # For each element after the first
    for i in range(1, len(arr)):
        # Find the right spot for the element in the sorted sub-array on the left
        # Insert it there:
        # Store the current element
        current_element = arr[i]
        # walk backwards through the sublist, shifting elements to the right by 1
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        # Until we reach a smaller or equal element, then put the current element in that place
        arr[j+1] = current_element
    return arr




l = [random.randint(0, 1000) for i in range(0, 10000)]

inputSizes = [i * 100 for i in range(1, 30)]
times = []

for inputSize in inputSizes:
    print(f"running: {inputSize}")
    l = [random.randint(0, 1000) for i in range(0, inputSize)]
    # Store a starting time
    start_time = time()
    # Run our code
    insertion_sort(l)
    # Store the ending time
    end_time = time()
    # Print out the ending time - starting time
    times.append(end_time - start_time)


print("LENGTHS")
for element in inputSizes:
    print(element)

print("TIMES")
for t in times:
    print(t)





