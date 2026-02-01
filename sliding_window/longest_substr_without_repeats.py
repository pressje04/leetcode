class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        curr_len = 0

        for i, char in enumerate(s):
            #end of the sequence
            if char in seen:
                seen.clear()
                max_length = max(max_length, curr_len)

                curr_len = 0
            curr_len += 1
            seen.add(char)

            if i == len(s) - 1:
                max_length = max(max_length, curr_len)
        return max_length

def test():
    sol = Solution()
    print(sol.lengthOfLongestSubstring("aab"))
    print(sol.lengthOfLongestSubstring("zxyzxyz"))

if __name__ == "__main__":
    test()

