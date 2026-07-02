class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        Map = {"(":")", "{":"}", "[":"]" }
        for i in s:
            if i in ["(","{","["]:
                q.append(i)
            elif i in [")","}","]"]:
                if not len(q):
                    return False
                else:
                    if i != Map[q.pop()]:
                        return False
        if len(q):
            return False
        else:
            return True