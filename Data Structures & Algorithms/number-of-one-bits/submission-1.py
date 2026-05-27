class Solution:
    def hammingWeight(self, n: int) -> int:
        # shifting and &ing with 1

        s = 0
        num = n

        for i in range(32):
            if (num & 1) > 0:
                s += 1
            num = num >> 1

        return s