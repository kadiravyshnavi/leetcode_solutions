class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        m=len(matrix)
        n=len(matrix[0])
        top=0
        left=0
        right=n-1
        bottom=m-1
        res=[]
        while left<=right and top<=bottom:
            #from top left to right
            for i in range(left,right+1):
                res.append(matrix[top][i])
            top+=1
            #from top right to bottom
            for i in range(top,bottom+1):
                res.append(matrix[i][right])
            right-=1
            #from bottom right to left
            if top<=bottom:
                for i in range(right,left-1,-1):
                    res.append(matrix[bottom][i])
                bottom-=1
            #from bottom left to top
            if left<=right:
                for i in range(bottom,top-1,-1):
                    res.append(matrix[i][left])
                left+=1
        return res