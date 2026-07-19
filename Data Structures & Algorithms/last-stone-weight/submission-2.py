import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)
        while(len(stones)>1):
            first = -heapq.heappop(stones)
            sec = -heapq.heappop(stones)
            
            if first == sec:
                continue
            else:
                heapq.heappush(stones, -abs(first-sec))
            # print(first,sec,stones)
        if stones:
            return -stones[0]
        else:
            return 0
