# Trees

## Description
There are many types of trees, but for the purpose of this tutorial we will be dealing with binary search trees. A binary search tree is similar to a linked list in a lot of ways. It is a data structure made up of nodes. Rather than being ordered by a physical placement in memory, each node has a pointer to a left child and to a right child, as well as space for some type of data. A binary search tree starts with a root and ends with leaves.

![Binary Search Tree](images/bst1.png)

In a binary search tree, everything to the left of any given node has data of a lesser value than the given node. Everything to the right holds data of a greater value.

### The Insert Function - O(logn) Time (if balanced), n=number of nodes
To insert a new piece of data into a binary search tree, we must write a recursive function with two parameters. The first parameter is the data that will go inside of the new node. The second is a node that we will check values with. Our function must take the following steps to insert a new node.

1. The first time we call the function, we should pass in the root for the node parameter so we start from the beginning.
2. Check to see if the node we are checking is `None`. If it is, then we make a new node there and insert our data and we are done.
3. If we aren't done yet, check if the new data is less than or greater than the data in the node we are checking.
4. If it is less than, repeat steps 2-3 with the node we are checking's left child.
5. If it is greater than, repeat steps 2-3 with the node we are checking's right child.

### The Remove Function - O(n) Time, n=length of list
To remove a node from a linked list, we must write a function with just one parameter; the node to be deleted. Our function must take the following steps to remove a node as depicted in the gif below.

1. Find the specified that needs to be deleted(in this case node 3)
2. Set the 'next' attribute of node the node before node 3(in this case node 45) to the node after node 3(in this case node 1
3. Set the 'prev' attribute of node 1 to node 45
4. Use the garbage collector to clean up node 3

![Insert into Doubly Linked List](images/ll-delete.gif)

### Common Errors

## Example - Insert After Function

## Practice - Customer Priority Queue
#
Images from [geeksforgeeks.org](https://www.geeksforgeeks.org)
