'''
As the name suggests, Quicksort is one of the fastest sorting algorithms.
The Quicksort algorithm takes an array of values, chooses one of the values as the 'pivot' element, and moves the other values so that
lower values are on the left of the pivot element, and higher values are on the right of it.
In this tutorial the last element of the array is chosen to be the pivot element, but we could also have chosen the first element of
the array, or any element in the array really.
Then, the Quicksort algorithm does the same operation recursively on the sub-arrays to the left and right side of the pivot element.
This continues until the array is sorted.
Recursion is when a function calls itself.
After the Quicksort algorithm has put the pivot element in between a sub-array with lower values on the left side, and a sub-array
with higher values on the right side, the algorithm calls itself twice, so that Quicksort runs again for the sub-array on the left side,
and for the sub-array on the right side. The Quicksort algorithm continues to call itself until the sub-arrays are too small to be sorted.
The algorithm can be described like this:

How it works:
    Choose a value in the array to be the pivot element.
    Order the rest of the array so that lower values than the pivot element are on the left, and higher values are on the right.
    Swap the pivot element with the first element of the higher values so that the pivot element lands in between the lower and higher values.
    Do the same operations (recursively) for the sub-arrays on the left and right side of the pivot element.
'''

'''
Manual Run Through
Before we implement the Quicksort algorithm in a programming language, let's manually run through a short array, just to get the idea.

Step 1: We start with an unsorted array.
[ 11, 9, 12, 7, 3]

Step 2: We choose the last value 3 as the pivot element.
[ 11, 9, 12, 7, 3]

Step 3: The rest of the values in the array are all greater than 3, and must be on the right side of 3. Swap 3 with 11.
[ 3, 9, 12, 7, 11]

Step 4: Value 3 is now in the correct position. We need to sort the values to the right of 3. We choose the last value 11 as 
the new pivot element.
[ 3, 9, 12, 7, 11]

Step 5: The value 7 must be to the left of pivot value 11, and 12 must be to the right of it. Move 7 and 12.

[ 3, 9, 7, 12, 11]
Step 6: Swap 11 with 12 so that lower values 9 and 7 are on the left side of 11, and 12 is on the right side.
[ 3, 9, 7, 11, 12]

Step 7: 11 and 12 are in the correct positions. We choose 7 as the pivot element in sub-array [ 9, 7], to the left of 11.
[ 3, 9, 7, 11, 12]

Step 8: We must swap 9 with 7.
[ 3, 7, 9, 11, 12]

And now, the array is sorted.
Run the simulation below to see the steps above animated:

Implement Quicksort in Python:
To write a 'quickSort' method that splits the array into shorter and shorter sub-arrays we use recursion. 
This means that the 'quickSort' method must call itself with the new sub-arrays to the left and right of the pivot element. 
Read more about recursion here.
To implement the Quicksort algorithm in a Python program, we need:
    An array with values to sort.
    A quickSort method that calls itself (recursion) if the sub-array has a size larger than 1.
    A partition method that receives a sub-array, moves values around, swaps the pivot element into the sub-array and returns 
    the index where the next split in sub-arrays happens.
    The resulting code looks like this:
'''
# Using the Quicksort algorithm in a Python program:
def partition(array, low, high):
  pivot = array[high]
  i = low - 1

  for j in range(low, high):
     if array[j] <= pivot:
       i += 1
       array[i], array[j] = array[j], array[i]

  array[i+1], array[high] = array[high], array[i+1]
  return i+1

def quicksort(array, low=0, high=None):
  if high is None:
    high = len(array) - 1

  if low < high:
    pivot_index = partition(array, low, high)
    quicksort(array, low, pivot_index-1)
    quicksort(array, pivot_index+1, high)

mylist = [64, 34, 25, 5, 22, 11, 90, 12]
quicksort(mylist)
print(mylist)