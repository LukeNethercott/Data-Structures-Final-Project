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

def student_in_section(classroom, student_id):
    pass


# Everything below this line is for testing purposes only -------------------------------
# Create classroom and insert students into classroom
section = BST()
section.insert(1012)
section.insert(765)
section.insert(1234)
section.insert(502)
section.insert(663)
section.insert(1013)

student_in_section(section, 1234)
student_in_section(section, 1235)
student_in_section(section, 1)
student_in_section(section, 765)
student_in_section(section, 663)
student_in_section(section, 1235)
student_in_section(section, 1013)

# Should print:
# True
# False
# False
# True
# True
# False
# True