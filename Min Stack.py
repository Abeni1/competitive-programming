class MinStack(object):

    def __init__(self):
        self.items = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.items.insert(0,val)
        

    def pop(self):
        """
        :rtype: None
        """
        self.items.pop(0)
        

    def top(self):
        """
        :rtype: int
        """
        return self.items[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.items)
