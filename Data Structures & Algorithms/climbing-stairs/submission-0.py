class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        if n = 1: ways(1, n) = 1
        in n = 2: ways (2, n) = 2 
        n < 2 : ways(2, n-1) = 0

        n > 2:
        1 + ways(2, n-1) + ways(1, n-1)
        
        '''
        # keep an array of the previously calculated
        # values

        dp = [0] * (n + 1)
        dp[n] = 1
        dp[n-1] = 1

        i = n - 2

        while i >= 0:
            dp[i] = dp[i + 1] + dp[i + 2]
            i -= 1

        print(dp)

        return dp[0]









        
