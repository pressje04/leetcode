from typing import List

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights) - 1

        maxArea = float('-inf')

        while l < r:
            area = min(heights[l], heights[r]) * (r - l)

            if heights[l] > heights[r] or heights[l] == heights[r]:
                # move right
                r -= 1
            elif heights[l] < heights[r]:
                l += 1
            else:
                l += 1
                r -= 1
            
            if area > maxArea:
                maxArea = area
        return maxArea

def test():
    sol = Solution()
    print(sol.maxArea([1,7,2,5,4,7,3,6]))

if __name__ == "__main__":
    test()