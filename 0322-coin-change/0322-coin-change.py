class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount==0:
            return amount
        prev=[0]*(amount+1)
        curr=[0]*(amount+1)
        for total in range(amount+1):
            if total%coins[0]==0:
                prev[total]=total//coins[0]
            else:
                prev[total]=float('inf')
        for i in range(1,len(coins)):
            for total in range(amount+1):
                pick=float('inf')
                if coins[i]<=total:
                    if curr[total-coins[i]]!=float('inf'):
                        pick=1+curr[total-coins[i]]
                np=prev[total]
                curr[total]=min(pick,np)
            prev=curr[:]
        if prev[amount]==float('inf'):
            return -1
        return prev[amount]
        