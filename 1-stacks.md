# Stacks

## Description
- Detailed and organized coverage of the topic with documentation including (but not limited to) example Python code, diagrams, and tables.
- What is the purpose of the data structure?
- What is the performance of the data structure (you will need to talk about big O notation)?
- What kind of problems can be solved using the data structure?
- How would the data structure be used in Python (in some cases you will need to discuss recursion)?
- What kind of errors are common when using the data structure?

A stack is a FILO data structure. FILO stands for 'first in last out.' I think of it like a stack of pancakes. The first pancake you put on the serving plate is the last pancake to be taken off. The last pancake you put on the serving plate is the first pancake to be taken off.

### Stack Functions

#### The `append()` Function

In the case of our stack in Python, we can use the `append()` function to add something from to top of the stack.

```
list_of_names=['Luke', 'Don', 'Damon', 'Sally']
list_of_names.append('Jenny')
print(list_of_names)
```

This code will print out `['Luke', 'Don', 'Damon', 'Sally', 'Jenny']` because 'Jenny' was appended to the list.

#### The `pop()` Function

In the case of our stack in Python, we can use the `pop()` function to remove something from the top of the stack.

```
list_of_names=['Luke', 'Don', 'Damon', 'Sally']
list_of_names.pop()
print(list_of_names)
```

This code will print out `['Luke', 'Don', 'Damon']` because 'Sally' was popped from the list.

## Example
- A complete example of a problem solved using the data structure.

## Practice
- A second problem (again created by you) which is given to the student of your tutorial to solve on their own. You need to provide a link to the solution.
