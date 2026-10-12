class Solution(object):
    def shortestCommonSupersequence(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        m=len(str1)
        n=len(str2)
        dp=[[0]*(n+1) for j in range(m+1)]
        for i in range(1,m+1):
            for j in range(1,n+1):
                if str1[i-1]==str2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        res=""
        i=m
        j=n
        k=dp[m][n]
        if k==0:
            return str2+str1
        while i-1>=0 and j-1>=0:
            if k==max(dp[i-1][j],dp[i][j-1]):
                if dp[i-1][j]>=dp[i][j-1]:
                    res+=str1[i-1]
                    i-=1
                    k=dp[i][j]
                else:
                    res+=str2[j-1]
                    j-=1
                    k=dp[i][j]
            else:
                res+=str1[i-1]
                i-=1
                j-=1
                k=dp[i][j]
        while i-1>=0:
            res+=str1[i-1]
            i-=1
        while j-1>=0:
            res+=str2[j-1]
            j-=1
        return res[::-1]
        