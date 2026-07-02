class Solution:
    def search(self, nums: List[int], target: int) -> int:        
        st = 0
        end = len(nums)-1
        # count = 0
        while st<=end:
            if st == end:
                if nums[st] == target:
                    return st
                else:
                    return -1
            # count+=1
            # if count>10:
            #     break
            mid = (st+end)//2
            # print(nums[mid], st, end, mid)
            if nums[mid]==target:
                return mid
            elif nums[mid]>target:
                end = mid
            else:
                st = mid+1
        return -1