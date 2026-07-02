class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        q = deque([(temperatures[0],0)])
        for i in range(1, n):

            if temperatures[i]<q[-1][0]:
                q.append((temperatures[i],i))
            else:
                while(len(q) and q[-1][0]<temperatures[i]):
                    val, idx = q.pop()
                    res[idx] = i-idx
                q.append((temperatures[i],i))
        return res