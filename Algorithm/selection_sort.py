'''
Selection Sort
The Selection Sort algorithm finds the lowest value in an array and moves it to the front of the array.
Sort
The algorithm looks through the array again and again, moving the next lowest values to the front, until the array is sorted.
How it works:
    Go through the array to find the lowest value.
    Move the lowest value to the front of the unsorted part of the array.
    Go through the array again as many times as there are values in the array.
'''

'''
Manual Run Through
Before we implement the Selection Sort algorithm in Python program, let's manually run through a short array only one time, 
just to get the idea.

Step 1: We start with an unsorted array.
[ 7, 12, 9, 11, 3]

Step 2: Go through the array, one value at a time. Which value is the lowest? 3, right?
[ 7, 12, 9, 11, 3]

Step 3: Move the lowest value 3 to the front of the array.
[ 3, 7, 12, 9, 11]

Step 4: Look through the rest of the values, starting with 7. 7 is the lowest value, and already at the front of the array, 
so we don't need to move it.
[ 3, 7, 12, 9, 11]

Step 5: Look through the rest of the array: 12, 9 and 11. 9 is the lowest value.
[ 3, 7, 12, 9, 11]

Step 6: Move 9 to the front.
[ 3, 7, 9, 12, 11]

Step 7: Looking at 12 and 11, 11 is the lowest.
[ 3, 7, 9, 12, 11]

Step 8: Move it to the front.
[ 3, 7, 9, 11, 12]

Finally, the array is sorted.
'''

'''
Implement Selection Sort in Python
To implement the Selection Sort algorithm in Python, we need:
An array with values to sort.
An inner loop that goes through the array, finds the lowest value, and moves it to the front of the array. 
This loop must loop through one less value each time it runs.
An outer loop that controls how many times the inner loop must run. For an array with  n values, this outer loop must run  n − 1 times.
'''
# Using the Selection sort on a Python list:
mylist = [64, 34, 25, 5, 22, 11, 90, 12]

n = len(mylist)
for i in range(n-1):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  min_value = mylist.pop(min_index)
  mylist.insert(i, min_value)

print(mylist)


# The improved Selection Sort algorithm, including swapping values:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n):
  min_index = i
  for j in range(i+1, n):
     if mylist[j] < mylist[min_index]:
       min_index = j
  mylist[i], mylist[min_index] = mylist[min_index], mylist[i]

print(mylist)