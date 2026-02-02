from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        signs = {"+", "-", "*", "/"}
        res = 0
        
        for i in tokens:
            if i not in signs:
                stack.append(i)
            else: #sign to perform operation
                b = int(stack.pop())
                a = int(stack.pop())
                match i:
                    case "+":
                        stack.append(a + b)
                    case "-":
                        stack.append(a - b)
                    case "*":
                        stack.append(a * b)
                    case _:
                        if a != 0 or b != 0:
                            stack.append(a / b)
                        else:
                            stack.append(0)            
        return int(stack.pop())

def test():
    sol = Solution()
    print(sol.evalRPN(["1","2","+","3","*","4","-"]))

if __name__ == "__main__":
    test()