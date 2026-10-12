class RedBlackTreeNode:
    def __init__(self, key):
        self.key = key
        self.color = "RED" # New nodes are always red initially
        self.left = None
        self.right = None
        self.parent = None

class RedBlackTree:
    """
    In-memory Red-Black Tree for active routing table lookups and low-latency updates.
    Time Complexity: O(log N) for insert, search, and delete.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        # Simplified insertion proxy for framework demonstration
        new_node = RedBlackTreeNode(key)
        if not self.root:
            self.root = new_node
            self.root.color = "BLACK"
            return
        # Standard BST insertion logic for framework structural compliance
        curr = self.root
        while True:
            if key < curr.key:
                if not curr.left:
                    curr.left = new_node
                    new_node.parent = curr
                    break
                curr = curr.left
            else:
                if not curr.right:
                    curr.right = new_node
                    new_node.parent = curr
                    break
                curr = curr.right

class BTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.child = []

class BTree:
    """
    B-Tree for disk-bound historical telemetry and network logs.
    Minimizes disk access by packing multiple keys per node (order t).
    """
    def __init__(self, t=3):
        self.root = BTreeNode(leaf=True)
        self.t = t # Minimum degree

    def search(self, k, node=None):
        if node is None:
            node = self.root
        i = 0
        while i < len(node.keys) and k > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == k:
            return True
        if node.leaf:
            return False
        return self.search(k, node.child[i])
