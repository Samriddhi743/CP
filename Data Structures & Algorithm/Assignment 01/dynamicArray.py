class DynamicArray:
    def __init__(self, resize_factor=2):
        self.array = []
        self.size = 0
        self.resize_factor = resize_factor

    def insert(self, index, element):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        self.array.insert(index, element)
        self.size += 1

    def delete(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bound")
        del self.array[index]
        self.size -= 1

    def get_size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def rotate(self, k):
        if self.size == 0 or k == 0:
            return
        k = k % self.size
        self.array = self.array[-k:] + self.array[:-k]

    def reverse(self):
        self.array.reverse()

    def append(self, ele):
        self.array.append(ele)
        self.size += 1

    def prepend(self, ele):
        self.array.insert(0, ele)
        self.size += 1

    def merge(self, other_array):
        self.array.extend(other_array.array)
        self.size += other_array.size

    def interleave(self, other_array):
        res = []
        i, j = 0, 0
        while i < self.size or j < other_array.size:
            if i < self.size:
                res.append(self.array[i])
                i += 1
            if j < other_array.size:
                res.append(other_array.array[j])
                j += 1
        self.array = res
        self.size = len(res)

    def find_middle(self):
        if self.size == 0:
            return None
        return self.array[self.size // 2]

    def index_of(self, ele):
        for i in range(self.size):
            if self.array[i] == ele:
                return i
        return -1

    def split(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index out of bound")
        new_array = DynamicArray(self.resize_factor)
        new_array.array = self.array[index:]
        new_array.size = len(new_array.array)
        self.array = self.array[:index]
        self.size = len(self.array)
        return new_array

    def resize(self, new_resize_factor):
        self.resize_factor = new_resize_factor

    def __resize_up(self):
        new_capacity = int(len(self.array) * self.resize_factor)
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array

    def __resize_down(self):
        new_capacity = max(1, int(len(self.array) / self.resize_factor))
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
