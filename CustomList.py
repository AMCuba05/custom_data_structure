from Node import Node

class CustomList:
    def __init__(self, size):
        self._size = size
        self._head = None
        self._items = 0
    
    def append(self, value):
        if self._items == self._size:
            next_node = self._head.get_next_node()
            next_node.set_previus(None)
            self._head = next_node
            self._items -= 1
        if(self._items == 0):
            self._head = Node(None, None , value)
            self._items += 1
        else:
            next_node = self._head.get_next_node()
            actual_node = self._head
            while next_node is not None:
                actual_node = next_node
                next_node = next_node.get_next_node()

            next_node = Node(actual_node , None, value)
            actual_node.set_next_node(next_node)
            self._items += 1

    def pop(self):
        next_node = self._head.get_next_node()
        actual_node = self._head
        while next_node is not None:
            actual_node = next_node
            next_node = actual_node.get_next_node()
        prev_node = actual_node.get_previus()
        actual_node.set_previus(None)
        prev_node.set_next_node(None)
        return actual_node.get_value()
    
    def get_item(self, index):
        i = 0
        if index >= self._items: raise IndexError("list index out of range")
        actual = self._head
        while i < self._items:
            if i == index: break
            i += 1
            actual = actual.get_next_node()
        return actual.get_value()
    
    def set_item(self, index, value):
        i = 0
        if index >= self._items: raise IndexError("list index out of range")
        actual = self._head
        while i < self._items:
            if i == index:
                actual.set_value(value)                
                break
            i += 1
            actual = actual.get_next_node()
        return actual.get_value()

    def get_size(self):
        return self._size
