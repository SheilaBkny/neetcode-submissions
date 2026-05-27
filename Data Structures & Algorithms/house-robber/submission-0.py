class Solution:
    def rob(self, nums: List[int]) -> int:
        
        i = len(nums) - 3

        while i >= 0:
            curr_cost = nums[i]
            for j in range(2, len(nums) - i):
                
            
                nums[i] = max(nums[i], curr_cost + nums[i + j])
            
            i -= 1

            print(nums)

        return max(nums)