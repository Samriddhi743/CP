class HashMapLinearProbing:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.size = 0
        self.keys = [None] * capacity
        self.values = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        index = self._hash(key)
        for i in range(self.capacity):
            if self.keys[index] is None:
                return False
            if self.keys[index] == key:
                return True
            index = (index + 1) % self.capacity
        return False

    def insert(self, key, value):
        index = self._hash(key)
        for i in range(self.capacity):
            if self.keys[index] is None or self.keys[index] == key:
                self.keys[index] = key
                self.values[index] = value
                self.size += 1
                return
            index = (index + 1) % self.capacity
        raise Exception("HashMap is full")

    def remove(self, key):
        index = self._hash(key)
        for i in range(self.capacity):
            if self.keys[index] is None:
                return
            if self.keys[index] == key:
                self.keys[index] = None
                self.values[index] = None
                self.size -= 1
                
                index = (index + 1) % self.capacity
                while self.keys[index] is not None:
                    rehash_key = self.keys[index]
                    rehash_value = self.values[index]
                    self.keys[index] = None
                    self.values[index] = None
                    self.size -= 1
                    self.insert(rehash_key, rehash_value)
                    index = (index + 1) % self.capacity
                return
            index = (index + 1) % self.capacity
# Input
hash_map_linear = HashMapLinearProbing(capacity=10)
hash_map_linear.insert("key1", "value1")
hash_map_linear.insert("key2", "value2")
print(hash_map_linear.find("key1"))  # Output: True
print(hash_map_linear.find("key3"))  # Output: False
hash_map_linear.remove("key1")
print(hash_map_linear.find("key1"))  # Output: False

