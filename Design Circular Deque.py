class MyCircularDeque(object):

    def __init__(self, k):
        """
        :type k: int
        """
        self.items = []
        self.k = k
        
        

    def insertFront(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:  
            self.items.insert(0,value)
            return True
        

    def insertLast(self, value):
        """
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.items.append(value)
            return True



    def deleteFront(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.items.pop(0)
            return True

    def deleteLast(self):
        """
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.items.pop()
            return True
        

    def getFront(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.items[0]
        else:
            return -1

    def getRear(self):
        """
        :rtype: int
        """
        if not self.isEmpty():
            return self.items[-1]
        else:
            return -1
        

    def isEmpty(self):
        """
        :rtype: bool
        """
        if not self.items:
            return True
        else:
            return False
        

    def isFull(self):
        """
        :rtype: bool
        """
        return len(self.items) == self.k
