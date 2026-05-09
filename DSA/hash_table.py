'''
Hash Table
A Hash Table is a data structure designed to be fast to work with.

The reason Hash Tables are sometimes preferred instead of arrays or linked lists is because searching for, adding, and deleting
data can be done really quickly, even for large amounts of data.

In a Linked List, finding a person "Bob" takes time because we would have to go from one node to the next, checking each node,
until the node with "Bob" is found.

And finding "Bob" in an list/array could be fast if we knew the index, but when we only know the name "Bob", we need to compare each
element and that takes time.

With a Hash Table however, finding "Bob" is done really fast because there is a way to go directly to where "Bob" is stored,
using something called a hash function.

Building A Hash Table from Scratch
To get the idea of what a Hash Table is, let's try to build one from scratch, to store unique first names inside it.

We will build the Hash Table in 5 steps:
    Create an empty list (it can also be a dictionary or a set).
    Create a hash function.
    Inserting an element using a hash function.
    Looking up an element using a hash function.
    Handling collisions.
'''
# Step 1: Create an Empty List
# To keep it simple, let's create a list with 10 empty elements.
my_list = [None, None, None, None, None, None, None, None, None, None]

'''
Step 2: Create a Hash Function
Now comes the special way we interact with Hash Tables.
We want to store a name directly into its right place in the array, and this is where the hash function comes in.
A hash function can be made in many ways, it is up to the creator of the Hash Table. A common way is to find a way to convert 
the value into a number that equals one of the Hash Table's index numbers, in this case a number from 0 to 9.

In our example we will use the Unicode number of each character, summarize them and do a modulo 10 operation to get index numbers 0-9.
'''
# Create a Hash Function that sums the Unicode numbers of each character and return a number between 0 and 9:
def hash_function(value):
  sum_of_chars = 0
  for char in value:
    sum_of_chars += ord(char)

  return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

'''
Step 3: Inserting an Element
According to our hash function, "Bob" should be stored at index 5.
Lets create a function that add items to our hash table:
'''
def add(name):
  index = hash_function(name)
  my_list[index] = name

add('Bob')
print(my_list)

# We can use the same functions to store "Pete", "Jones", "Lisa", and "Siri" as well.
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
print(my_list)

'''
Step 4: Looking up a name
Now that we have a super basic Hash Table, let's see how we can look up a name from it.
To find "Pete" in the Hash Table, we give the name "Pete" to our hash function. The hash function returns 8, 
meaning that "Pete" is stored at index 8.
'''
def contains(name):
  index = hash_function(name)
  return my_list[index] == name

print("'Pete' is in the Hash Table:", contains('Pete'))

'''
Step 5: Handling collisions
Let's also add "Stuart" to our Hash Table.
We give "Stuart" to our hash function, which returns 3, meaning "Stuart" should be stored at index 3.
Trying to store "Stuart" in index 3, creates what is called a collision, because "Lisa" is already stored at index 3.

To fix the collision, we can make room for more elements in the same bucket. Solving the collision problem in this way is called chaining, 
and means giving room for more elements in the same bucket.

Start by creating a new list with the same size as the original list, but with empty buckets:
'''
def add(name):
  index = hash_function(name)
  my_list[index].append(name)

add('Bob')
add('Pete')
add('Jones')
add('Lisa')
add('Siri')
add('Stuart')
print(my_list)

# After implementing each bucket as a list, "Stuart" can also be stored at index 3, and our Hash Set now looks like this:
my_list = [
  [None],
  ['Jones'],
  [None],
  ['Lisa', 'Stuart'],
  [None],
  ['Bob'],
  [None],
  ['Siri'],
  ['Pete'],
  [None]
]

'''
Uses of Hash Tables
Hash Tables are great for:

Checking if something is in a collection (like finding a book in a library).
Storing unique items and quickly finding them (like storing phone numbers).
Connecting values to keys (like linking names to phone numbers).
The most important reason why Hash Tables are great for these things is that Hash Tables are very fast compared Arrays and Linked Lists, 
especially for large sets. Arrays and Linked Lists have time complexity O(n) for search and delete, 
while Hash Tables have just O(1) on average.

Hash Tables Summarized
Hash Table elements are stored in storage containers called buckets.

A hash function takes the key of an element to generate a hash code.

The hash code says what bucket the element belongs to, so now we can go directly to that Hash Table element: to modify it, 
or to delete it, or just to check if it exists.

A collision happens when two Hash Table elements have the same hash code, because that means they belong to the same bucket.

Collision can be solved by Chaining by using lists to allow more than one element in the same bucket.
'''