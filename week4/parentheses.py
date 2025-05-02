class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        parens = {"(":")","[":"]", "{":"}"}
        stack = []
        for c in s:
            if c in parens:
                stack.append(c)
            else:
                if not stack or parens[stack.pop()] != c:
                    return False

        return len(stack) == 0
