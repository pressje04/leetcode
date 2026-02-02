from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 0 or not nums or not k:
            return []
        
        res = [] #result array, append max at each step
        n = len(nums)
        window = []
        curr_max = float("-infinity")

        #Fill initial window, the window here is just the first k elements
        index = 0
        while index < k:
            window.append(nums[index])
            if nums[index] > curr_max:
                curr_max = nums[index]
            index += 1
        res.append(curr_max)

        if n == 1:
            return res

        #slide window 1 to the right until the end
        l = 0
        r = k - 1

        while r < n - 1:
            l += 1
            r += 1
            window = nums[l : r + 1]
            if max(window) > curr_max or curr_max not in window:
                res.append(max(window))
            else:
                res.append(curr_max)
            
        return res

def test():
    sol = Solution()
    print(sol.maxSlidingWindow([1, 2, 1, 0, 4, 2, 6], k = 3))
    print(sol.maxSlidingWindow([1, -1], k = 1))

if __name__ == "__main__":
    test()