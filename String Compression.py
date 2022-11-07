class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s =""
        count = 1
        for i in range(len(chars)-1,-1,-1):
            if i and chars[i]==chars[i-1]:
                count += 1
                chars.pop(i)
            else:
                if count>1:
                    for char in str(count)[::-1]:
                        chars.insert(i+1, char)
                    count = 1
