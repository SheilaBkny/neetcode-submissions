class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        plan:
        for each index, go through each element, and product them,
        then add them to product array
        return product array.
        time complexity: o(n^2)
        """

        output = []

        for i in range(len(nums)):
            product = 1
            for j in range(len(nums)):
                if i != j:
                    product = product * nums[j]

            output.append(product)

        return output

        
        