# Top K Most Frequent Elements
# Pattern: 

from typing import List
from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        minheap = []

        for num in freqs:
             count = freqs[num]
             heapq.heappush(minheap, (count, num))
            
             if len(minheap) > k:
                  heapq.heappop(minheap)
        
        res = []
        for num in minheap:
             res.append(num[1])
        return res
    
             
def test():
        sol = Solution()
        print(sol.topKFrequent([1, 2, 2, 3, 3, 3, 4, 4, 4, 4], 4))



if __name__ == "__main__":
    test()
