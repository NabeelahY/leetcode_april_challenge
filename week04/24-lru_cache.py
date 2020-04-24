# Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and put.

# get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
# put(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

# The cache is initialized with a positive capacity.

# Follow up:
# Could you do both operations in O(1) time complexity?

# Example:

# LRUCache cache = new LRUCache( 2 /* capacity */ );

# cache.put(1, 1);
# cache.put(2, 2);
# cache.get(1);       // returns 1
# cache.put(3, 3);    // evicts key 2
# cache.get(2);       // returns -1 (not found)
# cache.put(4, 4);    // evicts key 1
# cache.get(1);       // returns -1 (not found)
# cache.get(3);       // returns 3
# cache.get(4);       // returns 4


class Node:
    def __init__(self, key: int, value: int, prev=None, next=None):
        self.key = key
        self.value = value
        self.prev = prev
        self.next = next      

class LRUCache:

    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity > 0")
            
        self.capacity = capacity
        self.size = 0
        self.storage = dict()
        self.head = None
        self.tail = None


    def get(self, key: int) -> int:
        if key in self.storage:
            node = self.storage[key]
            if self.head == node:
                return node.value
            self.delete(node)
            self.add_to_head(node)
            return node.value
        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
            
        if key in self.storage:
            node = self.storage[key]
            node.value = value
            
            if self.head != node:
                self.delete(node)
                self.add_to_head(node)
                
        else:
            new_node = Node(key, value)
    
            if self.size == self.capacity:
                del self.storage[self.tail.key]
                self.delete(self.tail)
            self.add_to_head(new_node)
            self.storage[key] = new_node

        
    def add_to_head(self, node):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.prev = self.head
            self.head.next = node
            self.head = node

        self.size += 1


    def delete(self, node):
        if not self.head:
            return

        if node.prev:
            node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev 

        if not node.next and not node.prev:
            self.head = None
            self.tail = None

        if self.tail == node:
            self.tail = node.next
            self.tail.prev = None
        self.size -= 1
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

class LRUCache2:
    def __init__(self, capacity):
        self.cache = OrderedDict()
        self.capacity = capacity


    def get(self, key):
        if key in self.cache:
            self.cache.move_to_end(key)

        return self.cache.get(key, -1)
        

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if(len(self.cache) >= self.capacity):
                self.cache.popitem(last=False)
        
        self.cache[key] = value