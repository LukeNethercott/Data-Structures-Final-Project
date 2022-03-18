# Stacks

## Description
A stack is a FILO data structure. FILO stands for 'first in last out.' I think of it like a stack of pancakes. The first pancake you put on the serving plate is the last pancake to be taken off. The last pancake you put on the serving plate is the first pancake to be taken off.

Stacks are used any time you need FILO organized data. Some examples would be actions taken in a word processor or pages visited in a browser. You can use ctrl+z to revert to the previous action taken in a word processor. You can use a back button to go back to the previously visited page in a browser.

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
- A complete example of a problem solved using the data structure.

## Practice
- A second problem (again created by you) which is given to the student of your tutorial to solve on their own. You need to provide a link to the solution.
