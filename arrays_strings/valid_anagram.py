# Valid Anagram
# Pattern: Hashmap
# Time: O(n) Counter operation twice
# Space: O(n) 2 dictionaries 

from typing import List
from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)
    
def test():
        sol = Solution()
        print(sol.isAnagram("bat", "tab"))
        print(sol.isAnagram("car", "cab")) 


        #True\nFalse

if __name__ == "__main__":
    test()