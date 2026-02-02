from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Not possible
        if len(s1) > len(s2):
            return False
        
        s1_counts = Counter(s1)
        window_counts = Counter(s2[:len(s1)])

        if s1_counts == window_counts:
            return True
        
        #slide window across s2, comparing the window to s1 every time
        for i in range(len(s1), len(s2)):
            window_counts[s2[i]] += 1 #add new character to window
            left_char = s2[i - len(s1)]
            window_counts[left_char] -= 1 #remove left char from the window

            if window_counts[left_char] == 0:
                del window_counts[left_char]

            if s1_counts == window_counts:
                return True
        return False