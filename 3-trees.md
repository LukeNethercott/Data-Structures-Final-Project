# Trees

## Description
There are many types of trees, but for the purpose of this tutorial we will be dealing with binary search trees. A binary search tree is similar to a linked list in a lot of ways. It is a data structure made up of nodes. Rather than being ordered by a physical placement in memory, each node has a pointer to a left child and to a right child, as well as space for some type of data. A binary search tree starts with a root and ends with leaves.

![Binary Search Tree](images/bst1.png)

In a binary search tree, everything to the left of any given node has data of a lesser value than the given node. Everything to the right holds data of a greater value.

### A balanced binary search tree
When creating a binary search tree, it is helpful when it is balanced. This means that if you drew it out in a diagram like the one above, the tree would be as symmetrical as possible. This makes search times faster because they can be done in O(logn) time. If a tree is unbalanced, it could take as long as O(n) time, so it's important to keep it balanced when possible.

### The Insert Function - O(logn) Time (if balanced), n=number of nodes
To insert a new piece of data into a binary search tree, we must write a recursive function with two parameters. The first parameter is the data that will go inside of the new node. The second is a node that we will check values with. Our function must take the following steps to insert a new node.

1. The first time we call the function, we should pass in the root for the node parameter so we start from the beginning.
2. Check to see if the node we are checking is `None`. If it is, then we make a new node there and insert our data and we are done.
3. If we aren't done yet, check if the new data is less than or greater than the data in the node we are checking.
4. If it is less than, repeat steps 2-3(and 4 or 5) with the node we are checking's left child.
5. If it is greater than, repeat steps 2-3(and 4 or 5) with the node we are checking's right child.

### The Search Function
In a balanced binary search tree, searching is much faster than in a standard list. Since we cut the data in half with every traversal, a search can always be completed in O(logn) time. It's algorithm is very similar to the insert algorithm.

1. Compare that data you're searching for with a node. (start with the root)
2. Check to see if the node we are checking is `None`. If it is, then we know that data is not in the tree and we are done.
3. If we aren't done yet, check if the new data is less than or greater than the data in the node we are checking.
4. If it is less than, repeat steps 2-3(and 4 or 5) with the node we are checking's left child.
5. If it is greater than, repeat steps 2-3(and 4 or 5) with the node we are checking's right child.

### Common Errors
- It's important to keep your tree balanced if you are expecting O(logn) time results
- Make sure to account for the instances in which your tree has no data in it

## Example - Company Department Employees
Let's say we are writing code for a company, and each employee has a unique employee ID. Every employee ID starts with the four numbers of the year they were hired, followed by a 5 digit auto-incremented number. (e.g. 202212345 for someone that was hired in 2022) The company has each of their departments organized into a binary search tree where each node represents an employee. The company needs a program with which you can enter a department and a year. The program will then print out each ID from the employees in that department hired in that year.

To write a function `employees_in_department()` that searches through the tree and prints the correct employee IDs, we would do the following:

```python
def employees_in_department(department, year):
    employees_found=False
    for employee in department:
        if str(employee)[:4]==str(year):
            print(employee)
            employees_found=True
    
    if employees_found==False:
        print('No employees found for the given year')

department = BST()
department.insert(201912345)
department.insert(202016584)
department.insert(202013497)
department.insert(202195432)
department.insert(202146464)
department.insert(202215987)

employees_in_department(department, 2019) # prints '201912345'
employees_in_department(department, 2018) # prints 'No employees found for the given year'
```

Download the example code at [this link](practice-files/trees-example.py).

## Practice - University Course Sections
Let's say we are writing code for a university, and each student has a unique student ID. They have each of their course sections organized into a binary search tree where each node represents a student. The university needs a program with which you can enter a course section and a student ID. If the given student is in the given section, the program will print true. If the given student is not in the given course section, the program will print false.

Write a function `student_in_section()` that searches through the tree and prints true or false accordingly.

Download the starting code at [this link](practice-files/trees-practice.py). See the solution at [this link](practice-files/trees-solution.py).

#
Images from [geeksforgeeks.org](https://www.geeksforgeeks.org)
