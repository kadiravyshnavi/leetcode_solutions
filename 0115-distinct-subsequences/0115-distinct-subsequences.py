class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m=len(s)
        n=len(t)
        prev=[0]*(n+1)
        curr=[0]*(n+1)
        prev[0]=1
        curr[0]=1
        for i in range(1,m+1):
            for j in range(1,n+1):
                np=prev[j]
                pick=0
                if s[i-1]==t[j-1]:
                    pick=prev[j-1]
                curr[j]=pick+np
            prev=curr[:]
        return prev[n]            
        pass
        