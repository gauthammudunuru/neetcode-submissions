class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pre = [1]*n
        suf = [1]*n
        for i in range(1,n):            
            pre[i] = (pre[i-1]*nums[i-1])
        for i in range(len(nums)-1,0,-1):
            suf[i-1] = (suf[i]*nums[i])

        out = []
        for i in range(n):
            out.append(pre[i]*suf[i])
        return out