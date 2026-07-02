class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if not tokens:
            return []
        q = deque()
        new_val = int(tokens[0])
        for i in tokens:
            if i in ['+','-','*','/']:
                val2 = int(q.pop())
                val1 = int(q.pop())
                if i=='+':
                    new_val = val1 + val2
                elif i=='-':
                    new_val = val1 - val2
                elif i=='*':
                    new_val = val1 * val2
                elif i=='/':
                    new_val = val1 / val2
                q.append(new_val)
            else:
                q.append(i)
        return int(new_val)
