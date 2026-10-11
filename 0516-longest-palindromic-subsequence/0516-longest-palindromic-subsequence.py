class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """
        def f(i,j,dp):
            if j<i:
                return 0
            if dp[i][j]!=-1:
                return dp[i][j]
            if i==j:
                dp[i][j]=1
            elif s[i]==s[j]:
                dp[i][j]=2+f(i+1,j-1,dp)
            else:
                dp[i][j]=max(f(i+1,j,dp),f(i,j-1,dp))
            return dp[i][j]
        m=len(s)
        dp=[[-1]*(m) for i in range(m)]
        return f(0,m-1,dp)