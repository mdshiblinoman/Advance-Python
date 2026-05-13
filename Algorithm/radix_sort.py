'''
Radix Sort
The Radix Sort algorithm sorts an array by individual digits, starting with the least significant digit (the rightmost one).
The radix (or base) is the number of unique digits in a number system. In the decimal system we normally use,
there are 10 different digits from 0 till 9.

Radix Sort uses the radix so that decimal values are put into 10 different buckets (or containers) corresponding to the digit
that is in focus, then put back into the array before moving on to the next digit.
Radix Sort is a non comparative algorithm that only works with non negative integers.
The Radix Sort algorithm can be described like this:

How it works:
    Start with the least significant digit (rightmost digit).
    Sort the values based on the digit in focus by first putting the values in the correct bucket based on the digit in focus,
    and then put them back into array in the correct order.
    Move to the next digit, and sort again, like in the step above, until there are no digits left.
'''

'''
Manual Run Through
Let's try to do the sorting manually, just to get an even better understanding of how Radix Sort works before actually 
implementing it in a programming language.
Step 1: We start with an unsorted array, and an empty array to fit values with corresponding radices 0 till 9.
myArray = [ 33, 45, 40, 25, 17, 24]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

Step 2: We start sorting by focusing on the least significant digit.
myArray = [ 33, 45, 40, 25, 17, 24]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

Step 3: Now we move the elements into the correct positions in the radix array according to the digit in focus. 
Elements are taken from the start of myArray and pushed into the correct position in the radixArray.
myArray = [ ]
radixArray = [ [40], [], [], [33], [24], [45, 25], [], [17], [], [] ]

Step 4: We move the elements back into the initial array, and the sorting is now done for the least significant digit. 
Elements are taken from the end radixArray, and put into the start of myArray.
myArray = [ 40, 33, 24, 45, 25, 17 ]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

Step 5: We move focus to the next digit. Notice that values 45 and 25 are still in the same order relative to each other as
they were to start with, because we sort in a stable way.
myArray = [ 40, 33, 24, 45, 25, 17 ]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]

Step 6: We move elements into the radix array according to the focused digit.
myArray = [ ]
radixArray = [ [], [17], [24, 25], [33], [40, 45], [], [], [], [], [] ]

Step 7: We move elements back into the start of myArray, from the back of radixArray.
myArray = [ 17, 24, 25, 33, 40, 45 ]
radixArray = [ [], [], [], [], [], [], [], [], [], [] ]
'''
# Using the Radix Sort algorithm in a Python program:
mylist = [170, 45, 75, 90, 802, 24, 2, 66]
print("Original array:", mylist)
radixArray = [[], [], [], [], [], [], [], [], [], []]
maxVal = max(mylist)
exp = 1

while maxVal // exp > 0:

  while len(mylist) > 0:
    val = mylist.pop()
    radixIndex = (val // exp) % 10
    radixArray[radixIndex].append(val)

  for bucket in radixArray:
    while len(bucket) > 0:
      val = bucket.pop()
      mylist.append(val)

  exp *= 10

print(mylist)

# A Radix Sort algorithm that uses Bubble Sort:
def bubbleSort(arr):
  n = len(arr)
  for i in range(n):
    for j in range(0, n - i - 1):
      if arr[j] > arr[j + 1]:
        arr[j], arr[j + 1] = arr[j + 1], arr[j]

def radixSortWithBubbleSort(arr):
  max_val = max(arr)
  exp = 1

  while max_val // exp > 0:
    radixList = [[],[],[],[],[],[],[],[],[],[]]

    for num in arr:
      radixIndex = (num // exp) % 10
      radixList[radixIndex].append(num)

    for bucket in radixList:
      bubbleSort(bucket)

    i = 0
    for bucket in radixList:
      for num in bucket:
        arr[i] = num
        i += 1

    exp *= 10

mylist = [170, 45, 75, 90, 802, 24, 2, 66]

radixSortWithBubbleSort(mylist)

print(mylist)