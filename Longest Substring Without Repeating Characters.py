class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
            """
        max_st= ""
        tmp = ""
        for char in s:
            if char in tmp:
                if len(tmp) > len(max_st):
                    max_st = tmp
                tmp = tmp[tmp.index(char) + 1:] + char
            else:
                tmp += char
        return max(len(max_st), len(tmp))
