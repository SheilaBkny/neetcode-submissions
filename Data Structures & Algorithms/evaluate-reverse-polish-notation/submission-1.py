class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # create stack to format this.
        stack = []
        operators = {"+", "-", "*", "/"}

        for s in tokens:
            if s not in operators:
                stack.append(s)
            else:
                num2 = int(stack.pop())
                num1 = int(stack.pop())
                res = 0

                if s == "+":
                    res = num1 + num2
                elif s == "-":
                    res = num1 - num2
                elif s == "*":
                    res = num1 * num2
                else:
                    res = int(num1 / num2)

                stack.append(str(res))
                   
        return int(stack.pop())

            
                