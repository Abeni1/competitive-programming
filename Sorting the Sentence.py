class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        arr = s[::-1].split()
        arr.sort()
        sent = []
        for word in arr:
            sent.append(word[1:][::-1])
        
        return " ".join(sent)
