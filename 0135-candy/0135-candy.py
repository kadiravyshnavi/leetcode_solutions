class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        n=len(ratings)
        left=[1]*n
        for i in range(1,n):
            if ratings[i]>ratings[i-1]:
                left[i]=left[i-1]+1
        prev=1
        curr=1
        ans=max(left[-1],prev)
        for i in range(n-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                curr=prev+1
                ans+=max(curr,left[i])
                prev=curr
            else:
                prev=1
                ans+=max(prev,left[i])
        return ans
        