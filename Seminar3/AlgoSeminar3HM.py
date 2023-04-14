class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return self.value
    
class LinkedList:
    def __init__(self):
        self.head = None
        
    def find_node(self, data):
        current_node = self.head
        while current_node:
            if current_node.data == data:
                return current_node
            current_node = current_node.next
        return None
        
    def append(self, data):
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
            
        current_node.next = new_node
    
        
    def insert_node(self, data, previous_node):
        new_node = Node(data)
        previous_node = self.find_node(previous_node)
        if previous_node is None:
            self.append(data)
            return
        last_node = previous_node.next
        previous_node.next = new_node
        new_node.next = last_node
        
    def del_end(self):
        node = self.head
        if not node or not node.next:
            self.head = None
            return
        old_node = None
        while node.next:
            old_node = node
            node = node.next
        old_node.next = None
    
    def reverse(self):
        previous = None
        current = self.head
        while current:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
                
    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(str(current_node.data), end=' ')
            current_node = current_node.next
        print()
      
a = LinkedList()
a.append(50)
a.append(111)
a.append(37)
a.append(5)
a.append(1)
a.print_list()
a.reverse()
a.print_list()