'''
Merge Sort
The Merge Sort algorithm is a divide-and-conquer algorithm that sorts an array by first breaking it down into smaller arrays, \
and then building the array back together the correct way so that it is sorted.
Divide: The algorithm starts with breaking up the array into smaller and smaller pieces until one such sub-array only consists of
one element.
Conquer: The algorithm merges the small pieces of the array back together by putting the lowest values first, resulting in a sorted array.
The breaking down and building up of the array to sort the array is done recursively.
In the animation above, each time the bars are pushed down represents a recursive call, splitting the array into smaller pieces.
When the bars are lifted up, it means that two sub-arrays have been merged together.
The Merge Sort algorithm can be described like this:

How it works:
    Divide the unsorted array into two sub-arrays, half the size of the original.
    Continue to divide the sub-arrays as long as the current piece of the array has more than one element.
    Merge two sub-arrays together by always putting the lowest value first.
    Keep merging until there are no sub-arrays left.
'''

'''
Manual Run Through
Let's try to do the sorting manually, just to get an even better understanding of how Merge Sort works before actually 
implementing it in a Python program.

Step 1: We start with an unsorted array, and we know that it splits in half until the sub-arrays only consist of one element. 
The Merge Sort function calls itself two times, once for each half of the array. That means that the first sub-array will 
split into the smallest pieces first.
[ 12, 8, 9, 3, 11, 5, 4]
[ 12, 8, 9] [ 3, 11, 5, 4]
[ 12] [ 8, 9] [ 3, 11, 5, 4]
[ 12] [ 8] [ 9] [ 3, 11, 5, 4]

Step 2: The splitting of the first sub-array is finished, and now it is time to merge. 8 and 9 are the first two elements to be merged. 
8 is the lowest value, so that comes before 9 in the first merged sub-array.
[ 12] [ 8, 9] [ 3, 11, 5, 4]

Step 3: The next sub-arrays to be merged is [ 12] and [ 8, 9]. Values in both arrays are compared from the start. 8 is 
lower than 12, so 8 comes first, and 9 is also lower than 12.
[ 8, 9, 12] [ 3, 11, 5, 4]

Step 4: Now the second big sub-array is split recursively.
[ 8, 9, 12] [ 3, 11, 5, 4]
[ 8, 9, 12] [ 3, 11] [ 5, 4]
[ 8, 9, 12] [ 3] [ 11] [ 5, 4]

Step 5: 3 and 11 are merged back together in the same order as they are shown because 3 is lower than 11.
[ 8, 9, 12] [ 3, 11] [ 5, 4]

Step 6: Sub-array with values 5 and 4 is split, then merged so that 4 comes before 5.
[ 8, 9, 12] [ 3, 11] [ 5] [ 4]
[ 8, 9, 12] [ 3, 11] [ 4, 5]

Step 7: The two sub-arrays on the right are merged. Comparisons are done to create elements in the new merged array:
3 is lower than 4
4 is lower than 11
5 is lower than 11
11 is the last remaining value
[ 8, 9, 12] [ 3, 4, 5, 11]

Step 8: The two last remaining sub-arrays are merged. Let's look at how the comparisons are done in more detail 
to create the new merged and finished sorted array:
3 is lower than 8:
Before [ 8, 9, 12] [ 3, 4, 5, 11]
After: [ 3, 8, 9, 12] [ 4, 5, 11]
Step 9: 4 is lower than 8:

Before [ 3, 8, 9, 12] [ 4, 5, 11]
After: [ 3, 4, 8, 9, 12] [ 5, 11]
Step 10: 5 is lower than 8:

Before [ 3, 4, 8, 9, 12] [ 5, 11]
After: [ 3, 4, 5, 8, 9, 12] [ 11]
Step 11: 8 and 9 are lower than 11:

Before [ 3, 4, 5, 8, 9, 12] [ 11]
After: [ 3, 4, 5, 8, 9, 12] [ 11]
Step 12: 11 is lower than 12:

Before [ 3, 4, 5, 8, 9, 12] [ 11]
After: [ 3, 4, 5, 8, 9, 11, 12]
'''
def mergeSort(arr):
  if len(arr) <= 1:
    return arr

  mid = len(arr) // 2
  leftHalf = arr[:mid]
  rightHalf = arr[mid:]

  sortedLeft = mergeSort(leftHalf)
  sortedRight = mergeSort(rightHalf)

  return merge(sortedLeft, sortedRight)

def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print("Sorted array:", mysortedlist)

# A Merge sort without recursion
def merge(left, right):
  result = []
  i = j = 0

  while i < len(left) and j < len(right):
    if left[i] < right[j]:
      result.append(left[i])
      i += 1
    else:
      result.append(right[j])
      j += 1

  result.extend(left[i:])
  result.extend(right[j:])

  return result

def mergeSort(arr):
  step = 1 # Starting with sub-arrays of length 1
  length = len(arr)

  while step < length:
    for i in range(0, length, 2 * step):
      left = arr[i:i + step]
      right = arr[i + step:i + 2 * step]

      merged = merge(left, right)

      # Place the merged array back into the original array
      for j, val in enumerate(merged):
        arr[i + j] = val

    step *= 2 # Double the sub-array length for the next iteration

  return arr

mylist = [3, 7, 6, -10, 15, 23.5, 55, -13]
mysortedlist = mergeSort(mylist)
print(mysortedlist)