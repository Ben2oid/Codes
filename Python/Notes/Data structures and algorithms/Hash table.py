class HashTable:
    def __init__(self):
        self.MAX = 10
        self.array = [None for i in range(self.MAX)]
        
    def get_hash(self, key, count_collisions = 0):
        h = 0
        for char in key:
            h += ord(char)
        return (h + count_collisions) % self.MAX
    
    def add(self, key, val):
        h = self.get_hash(key)
        current_array_value = self.array[h]
        
        if current_array_value is None:
            self.array[h] = [key, val]
            return
            
        if current_array_value[0] == key:
            self.array[h] = [key, val]
            return
        
        count_collisions = 1
        while current_array_value[0] is not key:
            new_hash = self.get_hash(key, count_collisions)
            current_array_value = self.array[new_hash]
            if current_array_value is None:
                self.array[new_hash] = [key, val]
                return
            if current_array_value[0] is key:
                self.array[new_hash] = [key, val]
                return
            if current_array_value[0] is not key:
                count_collisions += 1
            
            
        
    def get(self, key):
        h = self.get_hash(key)
        possible_return_value = self.array[h]
        if possible_return_value is None:
            return None
        if possible_return_value is not None:
            if possible_return_value[0] is key:
                return possible_return_value[1]
            
        collisions = 1
        while possible_return_value is not key:
            new_hash = self.get_hash(key, collisions)
            possible_return_value = self.array[new_hash]
            if possible_return_value is None:
                return None
            if possible_return_value[0] == key:
                return possible_return_value[1]
            collisions += 1
        return
        
    

    
    
        
t = HashTable()
key = "aaaa"
key2 = "aaaad"
t.add(key, "Seggfaszhülye")
t.add(key2, "mivan")
print(t.get_hash(key2))
print(t.get_hash(key))
print(t.array)
