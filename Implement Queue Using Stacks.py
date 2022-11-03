class MyQueue(object):

    def __init__(self):
        self.items = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.items.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.items.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.items[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return not self.items
        
