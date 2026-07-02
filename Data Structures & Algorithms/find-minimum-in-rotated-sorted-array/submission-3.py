class Solution:
    def findMin(self, nums: List[int]) -> int:
        st, end = 0, len(nums)-1
        ct = 0
        while(st<end):
            ct+=1
            # if ct>10:
            #     break
            mid = (st+end)//2 
            # print(st, end, mid, nums[st], nums[end], nums[mid])
            if nums[mid]>nums[end]:
                st = mid+1
            elif nums[mid]<nums[end]:
                end = mid
            
        return(min(nums[st], nums[end]))