# Contains Duplicate
# Pattern: Using a Set 
# Time: O(n) + O(n) = O(n)   make a set and loop thru nums
# Space: O(n)  one set that stores n elements

from typing import List
from collections import defaultdict

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        single = set(nums)

        for num in nums:
            if num in single:
                single.remove(num)
            else:
                return True
        return False
    
def test():
        sol = Solution()
        print(sol.containsDuplicate([1,2,3,4]))      # False
        print(sol.containsDuplicate([1,2,3,1]))      # True
        print(sol.containsDuplicate([]))              # False
        print(sol.containsDuplicate([1]))             # False

if __name__ == "__main__":
    test()
        

