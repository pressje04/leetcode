from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        #We will append length of the string + delimeter #  --> 4#boat3#toy
        encoded = ""
        for s in strs:
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = []
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] != "#":
                j += 1

            length_str = s[i:j]
            length = int(length_str)

            i = j + 1

            word = s[i:i+length]
            decoded.append(word)

            i += length
        
        return decoded
    
def test():
    sol = Solution()
    print(sol.encode(["card", "cow", "to", "darth"]))
    print(sol.decode("4#card3#cow2#to5#darth"))

if __name__ == "__main__":
    test()
