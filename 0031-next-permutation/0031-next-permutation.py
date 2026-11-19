class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        ind=-1
        for i in range(len(nums)-1,0,-1):
            if nums[i]>nums[i-1]:
                ind=i-1
                break
        if ind==-1:
            nums.reverse()
            return
        if ind!=-1:
            mini=float('inf')
            index=-1
            for i in range(len(nums)-1,ind,-1):
                if nums[i]>nums[ind]:
                    if nums[i]<mini:
                        mini=nums[i]
                        index=i
            nums[ind],nums[index]=nums[index],nums[ind]
            nums[ind+1:]=reversed(nums[ind+1:])
            return nums

        