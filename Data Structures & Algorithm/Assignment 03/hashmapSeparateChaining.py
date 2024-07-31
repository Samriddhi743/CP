class HashMapSeparateChaining:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.table = [[] for _ in range(capacity)]

    def _hash(self, key):
        return hash(key) % self.capacity

    def find(self, key):
        index = self._hash(key)
        for k, v in self.table[index]:
            if k == key:
                return True
        return False

    def insert(self, key, value):
        index = self._hash(key)
        for i, (k, v) in enumerate(self.table[index]):
            if k == key:
                self.table[index][i] = (key, value)
                return
        self.table[index].append((key, value))

    def remove(self, key):
        index = self._hash(key)
        self.table[index] = [(k, v) for k, v in self.table[index] if k != key]
# Input
hash_map_chaining = HashMapSeparateChaining(capacity=10)
hash_map_chaining.insert("key1", "value1")
hash_map_chaining.insert("key2", "value2")
print(hash_map_chaining.find("key1"))  # Output: True
print(hash_map_chaining.find("key3"))  # Output: False
hash_map_chaining.remove("key1")
print(hash_map_chaining.find("key1"))  # Output: False
