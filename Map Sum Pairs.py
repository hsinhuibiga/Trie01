#Map Sum Pairs

class Node(object):
    def __init__(self, count=0):
        self.children = collections.defaultdict(Node)
        self.count = count


class MapSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()
        self.keys = {}

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: void
        """
        curr = self.root
        delta = val - self.keys.get(key, 0)

        self.keys[key] = val

        curr = self.root
        
        curr.count += delta
        for char in key:
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count