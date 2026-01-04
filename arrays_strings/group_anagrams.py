# Group Anagrams
# Pattern: Hashmap + Sorting

#My approach: have a dictionary where each key is a sorted arrangement of a group of letters and 
#have the key be a list containing all of the different words which are anagrams of each other 
        # {"eta": [eat, tea, ate]}

from typing import List
from collections import defaultdict

class Solution: 
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            key = ''.join(sorted(s))
            res[key].append(s)
        return list(res.values())

def test():
    sol = Solution() 
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

if __name__ == "__main__":
    test()