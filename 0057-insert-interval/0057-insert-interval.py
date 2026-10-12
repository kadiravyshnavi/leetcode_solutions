class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        l=0
        if len(intervals)==0:
            return [newInterval]
        list=[]
        while l<len(intervals) and intervals[l][1]<newInterval[0]:
            list.append(intervals[l])
            l+=1
        mini=float('inf')
        maxi=-1
        while l<len(intervals) and intervals[l][0]<=newInterval[1]:
            mini=min(mini,intervals[l][0])
            maxi=max(maxi,intervals[l][1])
            l+=1
        mini=min(mini,newInterval[0])
        maxi=max(maxi,newInterval[1])
        list.append([mini,maxi])
        while l<len(intervals):
            list.append(intervals[l])
            l+=1
        return list
        