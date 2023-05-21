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
                return itr.value[1]
            itr = itr.next
        

t = HashMap(100)
ll = LinkedList()
# ll.insert_beginning(1)
# ll.insert_beginning(2)
# ll.insert_beginning(3)
# ll.insert_end(0)
# ll.insert_end(-1)
# ll.print_forward()
# ll.print_backward()
# print(ll.length())
# print(ll.empty())
print(t.hash("fecókadsdd"))
print(t.hash("fecókadsd"))
print(t.hash("Bence"))
print(t.hash("Key"))
t.set_value("fecókadsdd", "Blanca")
t.set_value("fecókadsd", "Szopdkifaggot")
print(t.get_value("fecókadsdd"))
print(t.get_value("fecókadsd"))
print(t.array)

