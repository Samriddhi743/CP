class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        new_node = Node(data)
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            new_node.next = current.next
            current.next = new_node
        
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            for _ in range(index - 1):
                current = current.next
            current.next = current.next.next
        
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0 or k == 0:
            return
        
        k = k % self.size
        if k == 0:
            return
        
        current = self.head
        length = 1
        while current.next:
            current = current.next
            length += 1
        
        current.next = self.head
        
        steps_to_new_head = length - k
        new_tail = self.head
        for _ in range(steps_to_new_head - 1):
            new_tail = new_tail.next
        
        self.head = new_tail.next
        new_tail.next = None

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.size += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def merge(self, other_list):
        if not self.head:
            self.head = other_list.head
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = other_list.head
        self.size += other_list.size

    def interleave(self, other_list):
        dummy = Node()
        tail = dummy
        current1, current2 = self.head, other_list.head
        
        while current1 or current2:
            if current1:
                tail.next = current1
                tail = tail.next
                current1 = current1.next
            if current2:
                tail.next = current2
                tail = tail.next
                current2 = current2.next
        
        self.head = dummy.next

    def find_middle(self):
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        return slow.data if slow else None

    def index_of(self, data):
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bounds")
        
        if index == 0:
            new_list = SinglyLinkedList()
            new_list.head = self.head
            self.head = None
            new_list.size = self.size
            self.size = 0
            return new_list
        
        current = self.head
        for _ in range(index - 1):
            current = current.next
        
        new_list = SinglyLinkedList()
        new_list.head = current.next
        new_list.size = self.size - index
        self.size = index
        current.next = None
        
        return new_list