class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        rows=[]
        cols=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    if i not in rows:
                        rows.append(i)
                    if j not in cols:
                        cols.append(j)
        for row in rows:
            for col in range(len(matrix[0])):
                matrix[row][col]=0
        for col in cols:
            for row in range(len(matrix)):
                matrix[row][col]=0
        return matrix