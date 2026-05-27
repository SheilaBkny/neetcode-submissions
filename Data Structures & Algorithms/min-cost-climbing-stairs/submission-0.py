class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        '''
        brute forcd


        '''
        cost.append(0)
        #start at len(cost) - 1

        i = len(cost) - 3
        

        while i >= 0:
            cost[i] = min(cost[i] + cost[i+1], cost[i] + cost[i+2])
            i -= 1

        return min(cost[0], cost[1])

        
        