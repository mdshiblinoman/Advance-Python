'''
Binary Trees
A Binary Tree is a type of tree data structure where each node can have a maximum of two child nodes, a left child node and a right child node.
This restriction, that a node can have a maximum of two child nodes, gives us many benefits:
Algorithms like traversing, searching, insertion and deletion become easier to understand, to implement, and run faster.
Keeping data sorted in a Binary Search Tree (BST) makes searching very efficient.
Balancing trees is easier to do with a limited number of child nodes, using an AVL Binary Tree for example.
Binary Trees can be represented as arrays, making the tree more memory efficient.
'''

# The Binary Tree above can be implemented much like a Linked List, except that instead of linking each node to one next node,
# we create a structure where each node can be linked to both its left and right child nodes.
# Create a Binary Tree in Python:
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

root = TreeNode('R')
nodeA = TreeNode('A')
nodeB = TreeNode('B')
nodeC = TreeNode('C')
nodeD = TreeNode('D')
nodeE = TreeNode('E')
nodeF = TreeNode('F')
nodeG = TreeNode('G')

root.left = nodeA
root.right = nodeB

nodeA.left = nodeC
nodeA.right = nodeD

nodeB.left = nodeE
nodeB.right = nodeF

nodeF.left = nodeG

# Test
print("root.right.left.data:", root.right.left.data)

'''
Types of Binary Trees
There are different variants, or types, of Binary Trees worth discussing to get a better understanding of how 
Binary Trees can be structured.

The different kinds of Binary Trees are also worth mentioning now as these words and concepts will be used later in the tutorial.

Below are short explanations of different types of Binary Tree structures, and below the explanations are drawings of 
these kinds of structures to make it as easy to understand as possible.

A balanced Binary Tree has at most 1 in difference between its left and right subtree heights, for each node in the tree.

A complete Binary Tree has all levels full of nodes, except the last level, which is can also be full, or filled from left to right. 
The properties of a complete Binary Tree means it is also balanced.

A full Binary Tree is a kind of tree where each node has either 0 or 2 child nodes.

A perfect Binary Tree has all leaf nodes on the same level, which means that all levels are full of nodes, and all internal nodes have two child nodes.
The properties of a perfect Binary Tree means it is also full, balanced, and complete.
'''

'''
Binary Tree Traversal
Going through a Tree by visiting every node, one node at a time, is called traversal.
Since Arrays and Linked Lists are linear data structures, there is only one obvious way to traverse these: start at the first element, 
or node, and continue to visit the next until you have visited them all.

But since a Tree can branch out in different directions (non-linear), there are different ways of traversing Trees.

There are two main categories of Tree traversal methods:
Breadth First Search (BFS) is when the nodes on the same level are visited before going to the next level in the tree. 
This means that the tree is explored in a more sideways direction.

Depth First Search (DFS) is when the traversal moves down the tree all the way to the leaf nodes, 
exploring the tree branch by branch in a downwards direction.

There are three different types of DFS traversals:
    pre-order
    in-order
    post-order
'''

'''
Pre-order Traversal of Binary Trees
Pre-order Traversal is a type of Depth First Search, where each node is visited in a certain order..

Pre-order Traversal is done by visiting the root node first, then recursively do a pre-order traversal of the left subtree, 
followed by a recursive pre-order traversal of the right subtree. It's used for creating a copy of the tree, prefix notation of 
an expression tree, etc.

This traversal is "pre" order because the node is visited "before" the recursive pre-order traversal of the left and right subtrees.
This is how the code for pre-order traversal looks like:
The first node to be printed is node R, as the Pre-order Traversal works by first visiting, or printing, the current node (line 4), 
before calling the left and right child nodes recursively (line 5 and 6).
The preOrderTraversal() function keeps traversing the left subtree recursively (line 5), before going on to traversing 
the right subtree (line 6). So the next nodes that are printed are 'A' and then 'C'.
The first time the argument node is None is when the left child of node C is given as an argument (C has no left child).
After None is returned the first time when calling C's left child, C's right child also returns None, and then 
the recursive calls continue to propagate back so that A's right child D is the next to be printed.
The code continues to propagate back so that the rest of the nodes in R's right subtree gets printed.
'''
def preOrderTraversal(node):
  if node is None:
    return
  print(node.data, end=", ")
  preOrderTraversal(node.left)
  preOrderTraversal(node.right)

print("Pre Order Traversal!")
preOrderTraversal(root)
print()


'''
In-order Traversal of Binary Trees
In-order Traversal is a type of Depth First Search, where each node is visited in a certain order.
In-order Traversal does a recursive In-order Traversal of the left subtree, visits the root node, and finally, does a recursive 
In-order Traversal of the right subtree. This traversal is mainly used for Binary Search Trees where it returns values in ascending order.
What makes this traversal "in" order, is that the node is visited in between the recursive function calls. 
The node is visited after the In-order Traversal of the left subtree, and before the In-order Traversal of the right subtree.
This is how the code for In-order Traversal looks like:

The inOrderTraversal() function keeps calling itself with the current left child node as an argument (line 4) until 
that argument is None and the function returns (line 2-3).
The first time the argument node is None is when the left child of node C is given as an argument (C has no left child).
After that, the data part of node C is printed (line 5), which means that 'C' is the first thing that gets printed.
Then, node C's right child is given as an argument (line 6), which is None, so the function call returns without doing anything else.
After 'C' is printed, the previous inOrderTraversal() function calls continue to run, so that 'A' gets printed, then 'D', then 'R', and so on.
'''
# Create an In-order Traversal:
def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

print("In Order Traversal!")
inOrderTraversal(root)
print()

'''
Post-order Traversal of Binary Trees
Post-order Traversal is a type of Depth First Search, where each node is visited in a certain order..
Post-order Traversal works by recursively doing a Post-order Traversal of the left subtree and the right subtree, 
followed by a visit to the root node. It is used for deleting a tree, post-fix notation of an expression tree, etc.
What makes this traversal "post" is that visiting a node is done "after" the left and right child nodes are called recursively.
This is how the code for Post-order Traversal looks like:

The postOrderTraversal() function keeps traversing the left subtree recursively (line 4), until None is returned when C's 
left child node is called as the node argument.
After C's left child node returns None, line 5 runs and C's right child node returns None, and then the letter 'C' is printed (line 6).
This means that C is visited, or printed, "after" its left and right child nodes are traversed, 
that is why it is called "post" order traversal.
The postOrderTraversal() function continues to propagate back to previous recursive function calls, 
so the next node to be printed is 'D', then 'A'.
The function continues to propagate back and printing nodes until all nodes are printed, or visited.
'''
# Post-order Traversal
def postOrderTraversal(node):
  if node is None:
    return
  postOrderTraversal(node.left)
  postOrderTraversal(node.right)
  print(node.data, end=", ")

print("Post Order Traversal!")
postOrderTraversal(root)
print()