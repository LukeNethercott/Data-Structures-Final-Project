class BST:
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = BST.Node(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = BST.Node(data)
            else:
                self._insert(data, node.left)
        else:
            if node.right is None:
                node.right = BST.Node(data)
            else:
                self._insert(data, node.right)
         
    def __iter__(self):
        yield from self._traverse_forward(self.root)
        
    def _traverse_forward(self, node):
        if node is not None:
            yield from self._traverse_forward(node.left)
            yield node.data
            yield from self._traverse_forward(node.right)
#----------------------------------------------------------------------------------------

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

employees_in_department(department, 2018)