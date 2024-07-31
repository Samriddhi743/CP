class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1
        self.size = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if not node:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._find(node.left, key)
        else:
            return self._find(node.right, key)

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if not node:
            return AVLNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        else:
            node.right = self._insert(node.right, key)
        return self._rebalance(node)

    def remove(self, key):
        self.root = self._remove(self.root, key)

    def _remove(self, node, key):
        if not node:
            return node
        if key < node.key:
            node.left = self._remove(node.left, key)
        elif key > node.key:
            node.right = self._remove(node.right, key)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._get_min_value_node(node.right)
            node.key = temp.key
            node.right = self._remove(node.right, temp.key)
        return self._rebalance(node)

    def _get_min_value_node(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def order_of_key(self, key):
        return self._order_of_key(self.root, key)

    def _order_of_key(self, node, key):
        if not node:
            return 0
        if key <= node.key:
            return self._order_of_key(node.left, key)
        else:
            left_size = node.left.size if node.left else 0
            return left_size + 1 + self._order_of_key(node.right, key)

    def get_by_order(self, k):
        return self._get_by_order(self.root, k + 1)  
    def _get_by_order(self, node, k):
        if not node:
            return None
        left_size = node.left.size if node.left else 0
        if k == left_size + 1:
            return node.key
        elif k <= left_size:
            return self._get_by_order(node.left, k)
        else:
            return self._get_by_order(node.right, k - left_size - 1)

    def _rebalance(self, node):
        self._update_height_and_size(node)
        balance = self._get_balance(node)
        if balance > 1:
            if self._get_balance(node.left) < 0:
                node.left = self._rotate_left(node.left)
            return self._rotate_right(node)
        if balance < -1:
            if self._get_balance(node.right) > 0:
                node.right = self._rotate_right(node.right)
            return self._rotate_left(node)
        return node

    def _update_height_and_size(self, node):
        node.height = 1 + max(self._get_height(node.left), self._get_height(node.right))
        node.size = 1 + (node.left.size if node.left else 0) + (node.right.size if node.right else 0)

    def _get_height(self, node):
        if not node:
            return 0
        return node.height

    def _get_balance(self, node):
        if not node:
            return 0
        return self._get_height(node.left) - self._get_height(node.right)

    def _rotate_left(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        self._update_height_and_size(z)
        self._update_height_and_size(y)
        return y

    def _rotate_right(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        self._update_height_and_size(z)
        self._update_height_and_size(y)
        return y
 
# Input
avl_tree = AVLTree()

# Insert elements
avl_tree.insert(10)
avl_tree.insert(20)
avl_tree.insert(30)
avl_tree.insert(40)
avl_tree.insert(50)
avl_tree.insert(25)

# Find elements
print(avl_tree.find(20))  # Output: True
print(avl_tree.find(60))  # Output: False

# Remove elements
avl_tree.remove(20)
print(avl_tree.find(20))  # Output: False

# Get elements by order
print(avl_tree.get_by_order(0))  # Output: 10
print(avl_tree.get_by_order(2))  # Output: 30
print(avl_tree.get_by_order(4))  # Output: 50      

# Get order of a key
print(avl_tree.order_of_key(10))  # Output: 0
print(avl_tree.order_of_key(30))  # Output: 2
print(avl_tree.order_of_key(50))  # Output: 4
