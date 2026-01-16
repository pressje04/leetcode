from typing import List
class Solution():
    def maxProfit(self, prices: List[int]) -> int:
        profit_max = 0
        min_value = float("inf")

        for day in prices:
            if day < min_value: 
                min_value = day
            if day - min_value > profit_max:
                profit_max = day - min_value
        return profit_max
    
def test():
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4]))
    print(sol.maxProfit([7,6,4,3,1]))

if __name__ == "__main__":
    test()