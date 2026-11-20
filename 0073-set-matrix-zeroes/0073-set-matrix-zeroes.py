class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        m=len(matrix)
        n=len(matrix[0])
        col=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    if j==0:
                        col=0
                    else:
                        matrix[0][j]=0
        for i in range(m-1,0,-1):
            for j in range(n-1,0,-1):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0
        if matrix[0][0]==0:
            for i in range(n-1,0,-1):
                if matrix[0][0]==0 or matrix[0][i]==0:
                    matrix[0][i]=0
        if col==0:
            for i in range(m):
                matrix[i][0]=0
        return matrix