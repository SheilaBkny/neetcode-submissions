class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        plan:
        for each index, go through each element, and product them,
        then add them to product array
        return product array.
        time complexity: o(n^2)
        """
        # output = []
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if i != j:
        #             product = product * nums[j]

        #     output.append(product)

        # return output

        """
        plan 2:
        goal: time complexity O(n) using the division operation
        """
        # output = []

        # product = 1
        # zero = 1
        # for n in nums:
        #     if n == 0:

        #     product *= n
        
        # for i in range(len(nums)):
        #     if nums[i] == 0:
                 
        #     else:
        #         output.append(product // nums[i])
                
        # return output

        """
        plan 3:
        goal: time complexity O(n) without using the division operation
        prefix - suffix method
        have an array that stores consecutive products from left to right
        another array fpr consecutive products right to left
        at an index, the product will be pref[i - 1] * suf[i + 1]

        """
        output = [0] * len(nums)
        prefix = [0] * len(nums)
        suffix = [0] * len(nums)

        p = 1
        s = 1

        for i in range(len(nums)):
            p *= nums[i]
            prefix[i] = p

        j = len(nums) - 1
        
        while j >= 0:
            s *= nums[j]
            suffix[j] = s
            j -= 1
            

        print(suffix)
        print(prefix)

        for i in range(len(nums)):
            if i == 0:
                output[i] = suffix[i + 1]
            elif i == len(nums) - 1:
                output[i] = prefix[i - 1]
            else:
                output[i] = prefix[i - 1] * suffix[i + 1]

        return output

 

            

        
        