from collections import Counter 

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        need = Counter(t)
        window = {}

        have = 0
        need_unique_chars = len(need)

        best_l, best_r = -1, -1
        best_len = float("inf")

        l = 0
        for r, ch in enumerate(s):
            window[ch] = window.get(ch, 0) + 1

            if ch in need and window[ch] == need[ch]:
                have += 1

                while have == need_unique_chars:
                #check window size and see if it's smaller than curr tracked min_len
                    if (r - l + 1) < best_len:
                        best_len = r - l + 1
                        best_l = l
                        best_r = r
                
                    window[s[l]] -= 1

                    if s[l] in need and window[s[l]] < need[s[l]]:
                        have -= 1
                    l += 1
        if best_len < float("infinity"):
            return s[best_l : best_r + 1]
        else:
            return ""
    
def test():
    sol = Solution()
    print(sol.minWindow("OUZODYXAZV", "XYZ"))

if __name__ == "__main__":
    test()
