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
Let's say that we are writing a program of how we want our computer to best utilize it's RAM. We would want to keep the mostly recently used tasks at the top of the stack so when the user returns to them, they will not have to load again. Let's say that a user is running all of the following programs.

```
open_programs=['Steam', 'Word', 'Microsoft Edge', 'Spotify', 'One Note']
```

Then the user opens up Visual Studio Code. We would want to make sure that our computer adds that to the top of the memory stack.

```
open_programs.append('Visual Studio Code')
```

The stack would now look like this:

```
open_programs=['Steam', 'Word', 'Microsoft Edge', 'Spotify', 'One Note', 'Visual Studio Code']
```

Depending on our program and how much memory the computer has, it may decide to remove Steam from the RAM so it could devote all of it's memory towards the 5 most recently opened programs.

## Practice
- A second problem (again created by you) which is given to the student of your tutorial to solve on their own. You need to provide a link to the solution.
