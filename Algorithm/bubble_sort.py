'''
Bubble Sort
Bubble Sort is an algorithm that sorts an array from the lowest value to the highest value.
Run the simulation to see how it looks like when the Bubble Sort algorithm sorts an array of values.
Each value in the array is represented by a column.
The word 'Bubble' comes from how this algorithm works, it makes the highest values 'bubble up'.

How it works:
    Go through the array, one value at a time.
    For each value, compare the value with the next value.
    If the value is higher than the next one, swap the values so that the highest value comes last.
    Go through the array as many times as there are values in the array.
'''

'''
Manual Run Through
Before we implement the Bubble Sort algorithm in a programming language, let's manually run through a short array only one time, 
just to get the idea.

Step 1: We start with an unsorted array.
[7, 12, 9, 11, 3]

Step 2: We look at the two first values. Does the lowest value come first? Yes, so we don't need to swap them.
[7, 12, 9, 11, 3]

Step 3: Take one step forward and look at values 12 and 9. Does the lowest value come first? No.
[7, 12, 9, 11, 3]

Step 4: So we need to swap them so that 9 comes first.
[7, 9, 12, 11, 3]

Step 5: Taking one step forward, looking at 12 and 11.
[7, 9, 12, 11, 3]

Step 6: We must swap so that 11 comes before 12.
[7, 9, 11, 12, 3]

Step 7: Looking at 12 and 3, do we need to swap them? Yes.
[7, 9, 11, 12, 3]

Step 8: Swapping 12 and 3 so that 3 comes first.
[7, 9, 11, 3, 12]
'''

# Create a Bubble Sort algorithm in Python:
mylist = [64, 34, 25, 12, 22, 11, 90, 5]

n = len(mylist)
for i in range(n-1):
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]

print(mylist)

'''
Bubble Sort Improvement
The Bubble Sort algorithm can be improved a little bit more.
Imagine that the array is almost sorted already, with the lowest numbers at the start, like this for example:
In this case, the array will be sorted after the first run, but the Bubble Sort algorithm will continue to run, 
without swapping elements, and that is not necessary.
If the algorithm goes through the array one time without swapping any values, the array must be finished sorted, 
and we can stop the algorithm, like this:
'''

# Improved Bubble Sort algorithm:
mylist = [7, 3, 9, 12, 11]

n = len(mylist)
for i in range(n-1):
  swapped = False
  for j in range(n-i-1):
    if mylist[j] > mylist[j+1]:
      mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
      swapped = True
  if not swapped:
    break

print(mylist)