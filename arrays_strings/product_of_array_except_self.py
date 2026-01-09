from typing import List

class Solution:
    def product_except_self(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1] * n

        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]
        
        suffix = 1
        for i in range(n-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        
        return result

def test():
    sol = Solution()
    print(sol.product_except_self([1, 2, 3, 4]))

if __name__ == "__main__":
    test()

