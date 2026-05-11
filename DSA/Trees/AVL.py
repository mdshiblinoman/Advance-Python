'''
AVL Trees
The only difference between a regular Binary Search Tree and an AVL Tree is that AVL Trees do rotation operations in addition,
to keep the tree balance.
A Binary Search Tree is in balance when the difference in height between left and right subtrees is less than 2.
By keeping balance, the AVL Tree ensures a minimum tree height, which means that search, insert, and delete operations
can be done really fast.

The two trees above are both Binary Search Trees, they have the same nodes, and the same in-order traversal (alphabetical),
but the height is very different because the AVL Tree has balanced itself.
Step through the building of an AVL Tree in the animation below to see how the balance factors are updated,
and how rotation operations are done when required to restore the balance.
'''

'''
Left and Right Rotations
To restore balance in an AVL Tree, left or right rotations are done, or a combination of left and right rotations.
The previous animation shows one specific left rotation, and one specific right rotation.
But in general, left and right rotations are done like in the animation below.

Notice how the subtree changes its parent. Subtrees change parent in this way during rotation to maintain the correct in-order traversal, 
and to maintain the BST property that the left child is less than the right child, for all nodes in the tree.
Also keep in mind that it is not always the root node that become unbalanced and need rotation.
'''

'''
The Balance Factor
A node's balance factor is the difference in subtree heights.
The subtree heights are stored at each node for all nodes in an AVL Tree, and the balance factor is calculated based on 
its subtree heights to check if the tree has become out of balance.
The height of a subtree is the number of edges between the root node of the subtree and the leaf node farthest down in that subtree.

The Left-Left (LL) Case
The node where the unbalance is discovered is left heavy, and the node's left child node is also left heavy.
When this LL case happens, a single right rotation on the unbalanced node is enough to restore balance.
Step through the animation below to see the LL case, and how the balance is restored by a single right rotation.
'''

'''
The Right-Right (RR) Case
A Right-Right case happens when a node is unbalanced and right heavy, and the right child node is also right heavy.
A single left rotation at the unbalanced node is enough to restore balance in the RR case.
The RR case happens two times in the animation above:
When node D is inserted, A becomes unbalanced, and bot A and B are right heavy. A left rotation at node A restores the tree balance.
After nodes E, C and F are inserted, node B becomes unbalanced. This is an RR case because both node B and its right child node D are 
right heavy. A left rotation restores the tree balance.

The Left-Right (LR) Case
The Left-Right case is when the unbalanced node is left heavy, but its left child node is right heavy.
In this LR case, a left rotation is first done on the left child node, and then a right rotation is done on the original unbalanced node.
Step through the animation below to see how the Left-Right case can happen, and how the rotation operations are done to restore balance.
As you are building the AVL Tree in the animation above, the Left-Right case happens 2 times, and rotation operations are required and done to restore balance:

When K is inserted, node Q gets unbalanced with a balance factor of -2, so it is left heavy, and its left child E is right heavy, 
so this is a Left-Right case.
After nodes C, F, and G are inserted, node K becomes unbalanced and left heavy, with its left child node E right heavy, 
so it is a Left-Right case.

The Right-Left (RL) Case
The Right-Left case is when the unbalanced node is right heavy, and its right child node is left heavy.
In this case we first do a right rotation on the unbalanced node's right child, and then we do a left rotation on the unbalanced node itself.
Step through the animation below to see how the Right-Left case can occur, and how rotations are done to restore the balance.
After inserting node B, we get a Right-Left case because node A becomes unbalanced and right heavy, and its right child is left heavy. 
To restore balance, a right rotation is first done on node F, and then a left rotation is done on node A.
The next Right-Left case occurs after nodes G, E, and D are added. This is a Right-Left case because B is unbalanced and right heavy, 
and its right child F is left heavy. To restore balance, a right rotation is first done on node F, and then a left rotation is done on node B.

Retracing in AVL Trees:
After inserting or deleting a node in an AVL tree, the tree may become unbalanced. To find out if the tree is unbalanced, 
we need to update the heights and recalculate the balance factors of all ancestor nodes.
This process, known as retracing, is handled through recursion. As the recursive calls propagate back to the root after an insertion 
or deletion, each ancestor node's height is updated and the balance factor is recalculated. If any ancestor node is found to have 
a balance factor outside the range of -1 to 1, a rotation is performed at that node to restore the tree's balance.
In the simulation below, after inserting node F, the nodes C, E and H are all unbalanced, but since retracing works through recursion, 
the unbalance at node H is discovered and fixed first, which in this case also fixes the unbalance in nodes E and C.
'''
# Implement AVL Tree in Python:
class TreeNode:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None
    self.height = 1

def getHeight(node):
  if not node:
    return 0
  return node.height

def getBalance(node):
  if not node:
    return 0
  return getHeight(node.left) - getHeight(node.right)

def rightRotate(y):
  print('Rotate right on node',y.data)
  x = y.left
  T2 = x.right
  x.right = y
  y.left = T2
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  return x

def leftRotate(x):
  print('Rotate left on node',x.data)
  y = x.right
  T2 = y.left
  y.left = x
  x.right = T2
  x.height = 1 + max(getHeight(x.left), getHeight(x.right))
  y.height = 1 + max(getHeight(y.left), getHeight(y.right))
  return y

def insert(node, data):
  if not node:
    return TreeNode(data)

  if data < node.data:
    node.left = insert(node.left, data)
  elif data > node.data:
    node.right = insert(node.right, data)

  # Update the balance factor and balance the tree
  node.height = 1 + max(getHeight(node.left), getHeight(node.right))
  balance = getBalance(node)

  # Balancing the tree
  # Left Left
  if balance > 1 and getBalance(node.left) >= 0:
    return rightRotate(node)

  # Left Right
  if balance > 1 and getBalance(node.left) < 0:
    node.left = leftRotate(node.left)
    return rightRotate(node)

  # Right Right
  if balance < -1 and getBalance(node.right) <= 0:
    return leftRotate(node)

  # Right Left
  if balance < -1 and getBalance(node.right) > 0:
    node.right = rightRotate(node.right)
    return leftRotate(node)

  return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

# Inserting nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inOrderTraversal(root)

'''
AVL Delete Node Implementation
When deleting a node that is not a leaf node, the AVL Tree requires the minValueNode() function to find a node's next node 
in the in-order traversal. This is the same as when deleting a node in a Binary Search Tree, as explained on the previous page.
To delete a node in an AVL Tree, the same code to restore balance is needed as for the code to insert a node.
'''
# Delete Node:
def minValueNode(node):
  current = node
  while current.left is not None:
    current = current.left
  return current

def delete(node, data):
  if not node:
    return node

  if data < node.data:
    node.left = delete(node.left, data)
  elif data > node.data:
    node.right = delete(node.right, data)
  else:
    if node.left is None:
      temp = node.right
      node = None
      return temp
    elif node.right is None:
      temp = node.left
      node = None
      return temp

    temp = minValueNode(node.right)
    node.data = temp.data
    node.right = delete(node.right, temp.data)

  return node

def inOrderTraversal(node):
  if node is None:
    return
  inOrderTraversal(node.left)
  print(node.data, end=", ")
  inOrderTraversal(node.right)

# Inserting nodes
root = None
letters = ['C', 'B', 'E', 'A', 'D', 'H', 'G', 'F']
for letter in letters:
  root = insert(root, letter)

inOrderTraversal(root)

'''
Time Complexity for AVL Trees
Take a look at the unbalanced Binary Search Tree below. Searching for "M" means that all nodes except 1 must be compared. 
But searching for "M" in the AVL Tree below only requires us to visit 4 nodes.
So in worst case, algorithms like search, insert, and delete must run through the whole height of the tree. 
This means that keeping the height (h) of the tree low, like we do using AVL Trees, gives us a lower runtime.
'''