class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n=len(height)
        prefix=[-1]*(n)
        suffix=[-1]*(n)
        maxi=0
        for i in range(n):
            maxi=max(maxi,height[i])
            prefix[i]=maxi
        maxi=0
        for i in range(n-1,-1,-1):
            maxi=max(maxi,height[i])
            suffix[i]=maxi
        water=0
        for i in range(len(height)):
            water+=min(prefix[i],suffix[i])-height[i]
        return water
