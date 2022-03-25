class LinkedList:
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
            self.prev = None

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_head(self, value):
        new_node = LinkedList.Node(value)  

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def remove_head(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        elif self.head is not None:
            self.head.next.prev = None
            self.head = self.head.next

    def insert_after(self, value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.tail:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = self.tail
                    self.tail.next = new_node
                    self.tail = new_node
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.prev = curr
                    new_node.next = curr.next
                    curr.next.prev = new_node
                    curr.next = new_node
                return
            curr = curr.next

    def insert_before(self, value, new_value):
        curr = self.head
        while curr is not None:
            if curr.data == value:
                if curr == self.head:
                    new_node = LinkedList.Node(new_value)
                    new_node.next = self.head
                    self.head.prev = new_node
                    self.head = new_node
                else:
                    new_node = LinkedList.Node(new_value)
                    new_node.next = curr
                    new_node.prev = curr.prev
                    curr.prev.next = new_node
                    curr.prev = new_node
                return
            curr = curr.next

    def __iter__(self):
        curr = self.head
        while curr is not None:
            yield curr.data
            curr = curr.next

    def __str__(self):
        output = "linkedlist["
        first = True
        curr = self.head
        while curr is not None:
            if first:
                first = False
            else:
                output += ", "
            output += str(curr.data)
            curr = curr.next
        output += "]"
        return output

def customer_priority(customer):
    if '***' in customer:
        return 3
    elif '**' in customer:
        return 2
    elif '*' in customer:
        return 1
    else:
        return 0

def order_in_queue(new_customer, queue):
    priority=customer_priority(new_customer)
    for customer in queue:
        if priority>customer_priority(customer):
            queue.insert_before(customer, new_customer)
            break

# Test -------------------------------------------------------
customer_queue=LinkedList()
customer_queue.insert_head('end of customer queue')
order_in_queue('Amy - **', customer_queue)
order_in_queue('Mike - *', customer_queue)
order_in_queue('John - ***', customer_queue)
order_in_queue('Sally - *', customer_queue)
order_in_queue('Jim - **', customer_queue)
order_in_queue('Levi - *', customer_queue)
order_in_queue('Nate - ***', customer_queue)
order_in_queue('Jane - *', customer_queue)

print(customer_queue)
# Should print: [John - ***, Nate - ***, Amy - **, Jim - **, Mike - *, Sally - *, Levi - *, Jane - *, end of customer queue]