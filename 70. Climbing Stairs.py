class Solution:
    res = {}
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n in Solution.res:
            return Solution.res[n]
        Solution.res[1] = 1
        Solution.res[2] = 2
        if n > 2:
            Solution.res[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return Solution.res[n]
