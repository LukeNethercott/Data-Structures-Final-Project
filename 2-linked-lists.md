# Linked Lists

## Description
There are many types of linked lists, but for the purpose of this tutorial we will be dealing with doubly linked lists. A doubly linked list is a data structure made up of nodes. Rather than being ordered by a physical placement in memory, each node has a previous and a next pointer, as well as space for some type of data. A linked list also starts with a head and ends with a tail.

![Doubly Linked List](images/linked-list.png)

You can implement stacks, queues, and many other data structures using doubly linked lists.

### The Insert Function - O(n) Time, n=length of list
To insert a new piece of data into a linked list, we must write a function with two parameters. The first parameter is the node after which we should place the new node. The second is what data is in the new node. Our function must take the following steps to insert a new node as depicted in the image below.

1. Create a new node and give it our data(in this case node E)
2. Find the specified node after which we should place node E(in this case node B)
3. Set the 'next' attribute of node E to the 'next' attribute of node B(in this case node C)
4. Set the 'next' attribute of node B to node E
5. Set the 'prev' attribute of the node E to node B
6. Set the 'prev' attribute of the node C to node E

![Insert into Doubly Linked List](images/ll-insert.png)

### The Remove Function - O(n) Time, n=length of list
To remove a node from a linked list, we must write a function with just one parameter; the node to be deleted. Our function must take the following steps to remove a node as depicted in the gif below.

1. Find the specified that needs to be deleted(in this case node 3)
2. Set the 'next' attribute of node the node before node 3(in this case node 45) to the node after node 3(in this case node 1
3. Set the 'prev' attribute of node 1 to node 45
4. Use the garbage collector to clean up node 3

![Insert into Doubly Linked List](images/ll-delete.gif)

### Common Errors

- Inserting or removing data from anywhere except for the end of a stack would defeat the purpose of a FILO organized data structure.
- Attempting to pop and item from an empty stack will result in an error. You can check how many items are in a stack with `len(name_of_stack)`.

## Example - 'Undo' in a Word Processor
Let's say that we are writing a program of how we want a word processor to use ctrl+z to undo. Each time an action is taken, it is appended to the stack. Each time it is undone, it is popped from the stack.
```
actions_taken=['Bolded Font of line 17', 'Deleted line 12', 'Pasted lines 20-23']
```

Then the user the decides to delete line 3.
```
actions_taken.append('Deleted line 3')
```

The stack would now look like this:
```
actions_taken=['Bolded Font of line 17', 'Deleted line 12', 'Pasted lines 20-23', 'Deleted line 3']
```

Then the user decides to undo twice. As we undid those actions, we would remove them from the stack.
```
actions_taken.pop()
actions_taken.pop()
```

The stack would now look like this:
```
actions_taken=['Bolded Font of line 17', 'Deleted line 12']
```

## Practice - 'Back' in an Internet Browser
In an internet browser, something needs to keep track of the pages that a user has visited so that when they click the back button, they go to the previously visited page. Write a function `new_page()` that adds every URL that a user visits to the top of the stack. Write a second function `go_back()` that removes a URL from the stack when the back button is pressed. Use [this file](practice-files/stack-practice.py) for your starting/test code. After you have completed the practice, feel free to check [this file](practice-files/stack-solution.py) for one of the many possible solutions. Good luck!

Images from [geeksforgeeks.org](https://www.geeksforgeeks.org)
