class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        ways to climb n steps = (n-1 steps) + (n-2 steps)

        array of size n
        work from left to right
        each index will be the sum of (i-1) + (i-2)

        base cases:
        n = 0: 0 ways
        n = 1: 1 way
        n = 2: 2 ways

        '''


        if n == 0: return 0
        if n == 1 :return 1
        if n == 2: return 2
        
        arr = [0] * (n + 1)
        if n > 2:
            arr[0], arr[1], arr[2] = 0, 1, 2

            for i in range(3, n+1):
                arr[i] = arr[i-1] + arr[i-2]


            return arr[n]
        