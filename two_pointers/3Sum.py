# Three Sum
# Technique: Two Pointers with sorting (similar to two sum 2)

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort() #Enables Two Pointer Technique

        for i, a in enumerate(nums):
            print(a) # a is the actual value
            print(i) # i is the index of that value

            if a > 0:
                break # if a > 0 in the sorted list, then it's not possible to get lower than zero
            
            if i > 0 and a == nums[i - 1]:
                continue
                # if it's the same number as before we can just skip this
            
            
            #basically gonna do 2 pointers on everything after current i
            l = i + 1
            r = len(nums) - 1

            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1 #Once again skip duplicate elements
        return res

def test():
    sol = Solution()
    print(sol.threeSum([0,1,1]))
    print(sol.threeSum([-1,0,1,2,-1,-4]))

if __name__ == "__main__":
    test()
    

