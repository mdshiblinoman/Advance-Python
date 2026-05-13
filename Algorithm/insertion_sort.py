'''
Insertion Sort
The Insertion Sort algorithm uses one part of the array to hold the sorted values, and the other part of the array to hold values
that are not sorted yet.
The algorithm takes one value at a time from the unsorted part of the array and puts it into the right place
in the sorted part of the array, until the array is sorted.

How it works:
    Take the first value from the unsorted part of the array.
    Move the value into the correct place in the sorted part of the array.
    Go through the unsorted part of the array again as many times as there are values.
'''

'''
Manual Run Through
Before we implement the Insertion Sort algorithm in a Python program, let's manually run through a short array, just to get the idea.

Step 1: We start with an unsorted array.
[ 7, 12, 9, 11, 3]

Step 2: We can consider the first value as the initial sorted part of the array. If it is just one value, it must be sorted, right?
[ 7, 12, 9, 11, 3]

Step 3: The next value 12 should now be moved into the correct position in the sorted part of the array. 
But 12 is higher than 7, so it is already in the correct position.
[ 7, 12, 9, 11, 3]

Step 4: Consider the next value 9.
[ 7, 12, 9, 11, 3]

Step 5: The value 9 must now be moved into the correct position inside the sorted part of the array, so we move 9 in between 7 and 12.
[ 7, 9, 12, 11, 3]

Step 6: The next value is 11.
[ 7, 9, 12, > 11, 3]

Step 7: We move it in between 9 and 12 in the sorted part of the array.
[ 7, 9, 11, 12, 3]

Step 8: The last value to insert into the correct position is 3.
[ 7, 9, 11, 12, 3]

Step 9: We insert 3 in front of all other values because it is the lowest value.
[ 3,7, 9, 11, 12]

Finally, the array is sorted.
Run the simulation below to see the steps above animated:
Insertion Sort
[ 7,12,9,11,3 ]
'''
# Using the Insertion Sort on a Python list:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist.pop(i)
  for j in range(i-1, -1, -1):
    if mylist[j] > current_value:
      insert_index = j
  mylist.insert(insert_index, current_value)

print(mylist)

# Insert the improvements in the sorting algorithm:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(1,n):
  insert_index = i
  current_value = mylist[i]
  for j in range(i-1, -1, -1):
     if mylist[j] > current_value:
       mylist[j+1] = mylist[j]
       insert_index = j
     else:
       break
  mylist[insert_index] = current_value

print(mylist)