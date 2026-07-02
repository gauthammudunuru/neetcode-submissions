class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        start = row//2
        count=0
        while start>=0 and start<=row:
            count+=1
            if count>row:
                break
            # print(0,row, start, target)
            if target in matrix[start]:
                # print(3,row, start, target)
                return True
            if target> max(matrix[start]):
                # print(1,row, start, target)
                if row==1:
                    return False
                else:
                    start = (start+row)//2
            elif target< min(matrix[start]):
                # print(2,row, start, target)
                if start==0:
                    return False
                else:
                    start = start//2
            else:
                # print(1,row, start, target)
                return False
            # print(1,row, start, target)
        return False