# Stacks

## Description
A stack is a FILO data structure. FILO stands for 'first in last out.' I think of it like a stack of pancakes. The first pancake you put on the serving plate is the last pancake to be taken off. The last pancake you put on the serving plate is the first pancake to be taken off.

Stacks are used any time you need FILO organized data. Storing actions taken in a word processor, pages visited in a browser, or most recently used programs in memory are all implementation examples of stacks.

### The `append()` Function - O(1) Time

In the case of our stack in Python, we can use the `append()` function to add something to the top of the stack.

```
list_of_names=['Luke', 'Don', 'Damon', 'Sally']
list_of_names.append('Jenny')
print(list_of_names)
```

This code will print out `['Luke', 'Don', 'Damon', 'Sally', 'Jenny']` because 'Jenny' was appended to the list.

### The `pop()` Function - O(1) Time

In the case of our stack in Python, we can use the `pop()` function to remove something from the top of the stack.

```
list_of_names=['Luke', 'Don', 'Damon', 'Sally']
list_of_names.pop()
print(list_of_names)
```

This code will print out `['Luke', 'Don', 'Damon']` because 'Sally' was popped from the list.

### Common Errors

- Inserting or removing data from anywhere except for the end of a stack would defeat the purpose of a FILO organized data structure.
- Attempting to pop and item from an empty stack will result in an error. You can check how many items are in a stack with `len(name_of_stack)`.

## Example
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



## Practice
- A second problem (again created by you) which is given to the student of your tutorial to solve on their own. You need to provide a link to the solution.
