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

        somewhow store the repeated work in an array
        use array to store 
        """
        output = []
        prefix = []
        suffix = []

        for i in range (len(nums)):
            pre = 1
            suf = 1
            for p in range(i):
                pre *= nums[p]
            prefix.append(pre)
            for s in range(i + 1, len(nums)):
                suf *= nums[s]
            suffix.append(suf)

        for i in range(len(nums)):
            output.append(prefix[i] * suffix[i])

        return output

            

        
        