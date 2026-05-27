class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # note: the array is not sorted.

        '''
        plan:
        enter each element into a hashman with frequencies.
        if there is any element with frequency 2, return true
        '''

        d = {}
        for n in nums:
            if n in d:
                d[n] += 1
            else:
                d[n] = 1

        for e in d:
            if d[e] > 1:
                return True
        
        return False
