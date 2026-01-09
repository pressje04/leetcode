#My solution involves using a hash set and skipping the sorting overhead by taking advantage of O(1) lookup time to see if the next 
#element that SHOULD be in the list is actually there. 

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for num in numSet:
            if (num - 1) not in numSet: #if n - 1 is not in the list, this starts a new potential consecutive sequence
                length = 1
                while (num + length) in numSet:
                    length += 1
                longest = max(length, longest) #You might have more than 1 different consecutive subsequence 
        return longest

def test():
    sol = Solution()
    print(sol.longestConsecutive([1, 2, 3, 4, 5])) #5
    print(sol.longestConsecutive([1, 2, 7, 6, 5, 3, 4])) #7
    print(sol.longestConsecutive([1, 4, 7, 4])) #1
    print(sol.longestConsecutive([0,3,2,5,4,6,1,1])) #7
    print(sol.longestConsecutive([1, 2, 3, 4, 6, 7, 8, 9, 10, 11])) #6

if __name__ == "__main__":
    test()