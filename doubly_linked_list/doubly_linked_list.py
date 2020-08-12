"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

    def get_value(self):
        return self.value
    
    def get_prev(self):
        return self.prev

    def set_prev(self, prev=None):
        self.prev = prev

    def get_next(self):
        return self.next

    def set_next(self, next=None):
        self.next = next
            
"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        node = ListNode(value, None, self.head)
        if self.head is not None:
            self.head.set_prev(node)
        if self.tail is None:
            self.tail = node
        self.head = node
        self.length = self.length + 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        returnval = self.head.get_value()
        if self.head is None and self.tail is None:
            return returnval
        if self.head.get_next() == None:
            self.head = None
            self.tail = None
            self.length = 0
            return returnval
        self.head = self.head.get_next()
        self.head.set_prev()
        self.length = self.length - 1
        return returnval
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        node = ListNode(value)
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        self.tail.set_next(node)
        node.set_prev(self.tail)
        self.tail = node
        self.length = self.length + 1

            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        returnval = self.tail.get_value()
        if self.head is self.tail:
            self.head = None
            self.tail = None
            self.length = 0
            return returnval
        self.tail.get_prev().set_next()
        self.tail = self.tail.get_prev()
        self.length = self.length - 1
        return returnval
            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """
    def move_to_front(self, node):
        node.get_prev().set_next(node.get_next())
        if node.get_next() is not None:
            node.get_next().set_prev(node.get_prev())
        node.set_prev()
        node.set_next(self.head)
        self.head.set_prev(node)
        self.head = node
        
        
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if node.get_prev() is not None:
            node.get_prev().set_next(node.get_next)
        if node.get_next() is not None:    
            node.get_next().set_prev(node.get_prev)
        if self.head is node:
            self.head = node.get_next()
        node.set_next()
        node.set_prev(self.tail)
        self.tail.set_next(node)
        self.tail = node

    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        current = self.head
        while current.get_next:
            if current is node:
                if current.get_prev() is not None:
                    node.get_prev().set_next(node.get_next())
                if self.head is node:
                    self.head = node.get_next()
                if current.get_next() is not None:
                    node.get_next().set_prev(node.get_prev())
                if self.tail is node:
                    self.tail = node.get_prev()
                node.set_next()
                node.set_prev()
                self.length = self.length - 1
                break
        current = current.get_next()
        

    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        current = self.head
        max = self.head.get_value()
        while current.get_next():
            current = current.get_next()
            if current.get_value() > max:
                max = current.get_value()    
        return max
