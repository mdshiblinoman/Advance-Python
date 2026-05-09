'''
Linked Lists
A linked list consists of nodes with some sort of data, and a pointer, or link, to the next node.
A singly linked list.
Linked Lists vs Arrays
The easiest way to understand linked lists is perhaps by comparing linked lists with arrays.

Linked lists consist of nodes, and is a linear data structure we make ourselves, unlike arrays which is an existing data structure
in the programming language that we can use.

Nodes in a linked list store links to other nodes, but array elements do not need to store links to other elements.
'''

'''
These are some key linked list properties, compared to arrays:
Linked lists are not allocated to a fixed size in memory like arrays are, so linked lists do not require to move the whole 
list into a larger memory space when the fixed memory space fills up, like arrays must.
Linked list nodes are not laid out one right after the other in memory (contiguously), so linked list nodes do not have 
to be shifted up or down in memory when nodes are inserted or deleted.
Linked list nodes require more memory to store one or more links to other nodes. Array elements do not require that much memory,
ecause array elements do not contain links to other elements.
Linked list operations are usually harder to program and require more lines than similar array operations, 
because programming languages have better built in support for arrays.
We must traverse a linked list to find a node at a specific position, but with arrays we can access an element directly 
by writing myArray[5].
'''

'''
Types of Linked Lists
There are three basic forms of linked lists:

Singly linked lists
Doubly linked lists
Circular linked lists
A singly linked list is the simplest kind of linked lists. It takes up less space in memory because each node has only 
one address to the next node, like in the image below.

A singly linked list.
A doubly linked list has nodes with addresses to both the previous and the next node, like in the image below, and 
therefore takes up more memory. But doubly linked lists are good if you want to be able to move both up and down in the list.

A doubly linked list.
A circular linked list is like a singly or doubly linked list with the first node, the "head", and the last node, 
the "tail", connected.

In singly or doubly linked lists, we can find the start and end of a list by just checking if the links are null. 
But for circular linked lists, more complex code is needed to explicitly check for start and end nodes in certain applications.

Circular linked lists are good for lists you need to cycle through continuously.

The image below is an example of a singly circular linked list:

A circular singly linked list.
The image below is an example of a doubly circular linked list:
'''

'''
Linked List Operations
Basic things we can do with linked lists are:
    Traversal
    Remove a node
    Insert a node
    Sort
For simplicity, singly linked lists will be used to explain these operations below.

Traversal of a Linked List
Traversing a linked list means to go through the linked list by following the links from one node to the next.

Traversal of linked lists is typically done to search for a specific node, and read or modify the node's content, 
remove the node, or insert a node right before or after that node.

To traverse a singly linked list, we start with the first node in the list, the head node, and follow that node's next link, 
and the next node's next link and so on, until the next address is null.

The code below prints out the node values as it traverses along the linked list, in the same way as the animation above.
'''
# Traversal of a singly linked list in Python:
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

traverseAndPrint(node1)

'''
Find The Lowest Value in a Linked List
Let's find the lowest value in a singly linked list by traversing it and checking each value.
Finding the lowest value in a linked list is very similar to how we found the lowest value in an array, 
except that we need to follow the next link to get to the next node.

To find the lowest value we need to traverse the list like in the previous code. But in addition to traversing the list, 
we must also update the current lowest value when we find a node with a lower value.

In the code below, the algorithm to find the lowest value is moved into a function called findLowestValue.
'''
# Finding the lowest value in a singly linked list in Python:
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def findLowestValue(head):
  minValue = head.data
  currentNode = head.next
  while currentNode:
    if currentNode.data < minValue:
      minValue = currentNode.data
    currentNode = currentNode.next
  return minValue

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("The lowest value in the linked list is:", findLowestValue(node1))

'''
Delete a Node in a Linked List
If you want to delete a node in a linked list, it is important to connect the nodes on each side of the node before deleting it, 
so that the linked list is not broken.

So before deleting the node, we need to get the next pointer from the previous node, and connect the previous node 
to the new next node before deleting the node in between.

Also, it is a good idea to first connect next pointer to the node after the node we want to delete, before we delete it. 
This is to avoid a 'dangling' pointer, a pointer that points to nothing, even if it is just for a brief moment.

The simulation below shows the node we want to delete, and how the list must be traversed first to connect the list 
properly before deleting the node without breaking the linked list.

In the code below, the algorithm to delete a node is moved into a function called deleteSpecificNode.
'''
# Deleting a specific node in a singly linked list in Python:
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def deleteSpecificNode(head, nodeToDelete):
  if head == nodeToDelete:
    return head.next

  currentNode = head
  while currentNode.next and currentNode.next != nodeToDelete:
    currentNode = currentNode.next

  if currentNode.next is None:
    return head

  currentNode.next = currentNode.next.next

  return head

node1 = Node(7)
node2 = Node(11)
node3 = Node(3)
node4 = Node(2)
node5 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

print("Before deletion:")
traverseAndPrint(node1)

# Delete node4
node1 = deleteSpecificNode(node1, node4)

print("\nAfter deletion:")
traverseAndPrint(node1)

'''
Insert a Node in a Linked List
Inserting a node into a linked list is very similar to deleting a node, because in both cases we need to take care of 
the next pointers to make sure we do not break the linked list.

To insert a node in a linked list we first need to create the node, and then at the position where we insert it, 
we need to adjust the pointers so that the previous node points to the new node, and the new node points to the correct next node.

The simulation below shows how the links are adjusted when inserting a new node.

New node is created
Node 1 is linked to new node
New node is linked to next node
'''
# Inserting a node in a singly linked list in Python:
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

def traverseAndPrint(head):
  currentNode = head
  while currentNode:
    print(currentNode.data, end=" -> ")
    currentNode = currentNode.next
  print("null")

def insertNodeAtPosition(head, newNode, position):
  if position == 1:
    newNode.next = head
    return newNode

  currentNode = head
  for _ in range(position - 2):
    if currentNode.next is None:
      break
    currentNode = currentNode.next

  newNode.next = currentNode.next
  currentNode.next = newNode
  return head

node1 = Node(7)
node2 = Node(3)
node3 = Node(2)
node4 = Node(9)

node1.next = node2
node2.next = node3
node3.next = node4

print("Original list:")
traverseAndPrint(node1)

# Insert a new node with value 97 at position 2
newNode = Node(97)
node1 = insertNodeAtPosition(node1, newNode, 2)

print("\nAfter insertion:")
traverseAndPrint(node1)

'''
Time Complexity of Linked Lists Operations
Here we discuss time complexity of linked list operations, and compare these with the time complexity of the array algorithms 
that we have discussed previously in this tutorial.

Remember that time complexity just says something about the approximate number of operations needed by the algorithm based on 
a large set of data (n), and does not tell us the exact time a specific implementation of an algorithm takes.

This means that even though linear search is said to have the same time complexity for arrays as for linked list: O(n), 
it does not mean they take the same amount of time. The exact time it takes for an algorithm to run depends on programming language,
computer hardware, differences in time needed for operations on arrays vs linked lists, and many other things as well.

Linear search for linked lists works the same as for arrays. A list of unsorted values are traversed from the head node until 
the node with the specific value is found. Time complexity is O(n).

Binary search is not possible for linked lists because the algorithm is based on jumping directly to different array elements, 
and that is not possible with linked lists.

Sorting algorithms have the same time complexities as for arrays, and these are explained earlier in this tutorial. 
But remember, sorting algorithms that are based on directly accessing an array element based on an index, do not work on linked lists.
'''