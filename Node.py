class Node:
    def __init__(self, previus, next_node, value):
        self._previus = previus
        self._next_node = next_node
        self._value = value
    
    def get_value(self):
        return self._value
    
    def get_previus(self):
        return self._previus
    
    def get_next_node(self):
        return self._next_node
    
    def set_value(self, new_value):
        self._value = new_value

    def set_previus(self, new_previus):
        self._previus = new_previus
    
    def set_next_node(self, new_next):
        self._next_node = new_next