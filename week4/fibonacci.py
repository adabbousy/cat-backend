class Solution(object):
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """

        if self.memo.get(n, None):
            return self.memo[n]
        else:
            if n <= 1:
                self.memo[n] = n
            else:
                self.memo[n] = self.fib(n - 1) + self.fib(n - 2)
            return self.memo[n]