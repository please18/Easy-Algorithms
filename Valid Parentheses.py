# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        while (n != 0 and n%2 == 0):
            s = s.replace("()", "")
            s = s.replace("{}", "")
            s = s.replace("[]",  "")
            if n > len(s):
                n = len(s)
            else:
                n = 0
        return s == ""
