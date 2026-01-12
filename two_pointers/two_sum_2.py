from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        l = 0
        r = n - 1

        while l < r:
            if numbers[r] + numbers[l] < target:
                l += 1
            if numbers[r] + numbers[l] > target:
                r -= 1
            if numbers[r] + numbers[l] == target:
                return [l + 1, r + 1]

def test():
    sol = Solution()
    print(sol.twoSum([1, 2, 3, 4, 5], 3))

if __name__ == "__main__":
    test()