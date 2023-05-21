class Node:
    def __init__(self, value, prev = None, next = None):
        self.value = value
        self.prev = prev
        self.next = next
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def empty(self):
        return self.head is None and self.tail is None
    
    def get_head(self):
        return self.head
    
    def insert_beginning(self, value):
        if self.empty():
            self.head = Node(value)
            self.tail = self.head
            return
        self.head.prev = Node(value, None, self.head)
        self.head = self.head.prev
    
    def insert_end(self, value):
        if self.empty():
            self.head = Node(value)
            self.tail = self.head
            return
        self.tail.next = Node(value, self.tail)
        self.tail = self.tail.next
        
    def print_forward(self):
        itr = self.head
        llstr = ""
        while itr:
            llstr += str(itr.value) + " --> "
            itr = itr.next
        print(llstr)
        
    def print_backward(self):
        itr = self.tail
        llstr = ""
        while itr:
            llstr +=  " <-- " + str(itr.value)
            itr = itr.prev
        print(llstr)
        
    def length(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count
            
class HashMap:
    def __init__(self, size):
        self.size = size
        self.array = [LinkedList() for i in range(self.size)]
        
    def hash(self, key):
        h = 0
        for i in key:
            h += ord(i)
        return h % self.size
    
    def set_value(self, key, value):
        h = self.hash(key)
        self.array[h].insert_beginning([key, value])
        
    def get_value(self, key):
        h = self.hash(key)
        index = self.array[h]
        itr = index.get_head()
        for i in range(index.length()):
            if itr.value[0] == key:
                return print(itr.value[1])
            itr = itr.next
        

t = HashMap(100)
print(t.hash("Bence"))
print(t.hash("Gellért"))
print(t.hash("Fecó"))
print(t.hash("Moni"))
t.set_value("Bence", "Blanca")
t.set_value("Gellért", "Regina")
t.set_value("Fecó", "Reni")
t.set_value("Moni", "Attila")
t.get_value("Bence")
t.get_value("Gellért")
t.get_value("Fecó")
t.get_value("Moni")
