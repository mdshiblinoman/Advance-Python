'''
Binary Search
The Binary Search algorithm searches through a sorted array and returns the index of the value it searches for.
Run the simulation to see how the Binary Search algorithm works.
Binary Search is much faster than Linear Search, but requires a sorted array to work.
The Binary Search algorithm works by checking the value in the center of the array. If the target value is lower,
the next value to check is in the center of the left half of the array. This way of searching means that the search
area is always half of the previous search area, and this is why the Binary Search algorithm is so fast.
This process of halving the search area happens until the target value is found, or until the search area of the array is empty.
How it works:
    Check the value in the center of the array.
    If the target value is lower, search the left half of the array. If the target value is higher, search the right half.
    Continue step 1 and 2 for the new reduced part of the array until the target value is found or until the search area is empty.
    If the value is found, return the target value index. If the target value is not found, return -1.
'''

'''
Manual Run Through
Let's try to do the searching manually, just to get an even better understanding of how Binary Search works before actually 
implementing it in a Python program. We will search for value 11.

Step 1: We start with an array.
[ 2, 3, 7, 7, 11, 15, 25]
Step 2: The value in the middle of the array at index 3, is it equal to 11?

[ 2, 3, 7, 7, 11, 15, 25]
Step 3: 7 is less than 11, so we must search for 11 to the right of index 3. The values to the right of index 3 are [ 11, 15, 25]. 
The next value to check is the middle value 15, at index 5.

[ 2, 3, 7, 7, 11, 15, 25]
Step 4: 15 is higher than 11, so we must search to the left of index 5. We have already checked index 0-3, 
so index 4 is only value left to check.

[ 2, 3, 7, 7, 11, 15, 25]
We have found it!

Value 11 is found at index 4.
Returning index position 4.
Binary Search is finished.
Run the simulation below to see the steps above animated:
'''

'''
Implementing Binary Search in Python
To implement the Binary Search algorithm we need:
An array with values to search through.
A target value to search for.
A loop that runs as long as left index is less than, or equal to, the right index.
An if-statement that compares the middle value with the target value, and returns the index if the target value is found.
An if-statement that checks if the target value is less than, or larger than, the middle value, and updates the "left" or "right" 
variables to narrow down the search area.
After the loop, return -1, because at this point we know the target value has not been found.
'''
# Create a Binary Search algorithm in Python:
def binarySearch(arr, targetVal):
  left = 0
  right = len(arr) - 1

  while left <= right:
    mid = (left + right) // 2

    if arr[mid] == targetVal:
      return mid

    if arr[mid] < targetVal:
      left = mid + 1
    else:
      right = mid - 1

  return -1

mylist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
x = 11

result = binarySearch(mylist, x)

if result != -1:
  print("Found at index", result)
else:
  print("Not found")

