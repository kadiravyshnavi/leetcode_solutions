class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        target=abs(target)
        total=sum(nums)
        if total-target<0 or (total-target)%2!=0:
            return 0
        k=(total-target)//2
        prev=[0]*(k+1)
        curr=[0]*(k+1)
        prev[0]=1
        for i in range(len(nums)):
            for target in range(k+1):
                pick=0
                if nums[i]<=target:
                    pick=prev[target-nums[i]]
                np=prev[target]
                curr[target]=pick+np
            prev=curr[:]
        return prev[k]
        