import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)   
        while(len(self.nums)>self.k):
            heapq.heappop(self.nums)        
        
    def add(self, val: int) -> int:  
        if not self.nums:
            heapq.heappush(self.nums, val)  
            return val  
        top = self.nums[0]
        if len(self.nums)<self.k:
            heapq.heappush(self.nums, val) 
            return top
        if val>top:            
            heapq.heappush(self.nums, val)  
            heapq.heappop(self.nums)
            return self.nums[0]
        else:
            return top
        
