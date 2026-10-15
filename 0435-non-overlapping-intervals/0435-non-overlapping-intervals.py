import heapq
class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        heap=[]
        intervals.sort(key=lambda x:x[1])
        heapq.heappush(heap,intervals[0][1])
        count=0
        for i in range(1,len(intervals)):
            if heap[0]<=intervals[i][0]:
                heapq.heappop(heap)
                heapq.heappush(heap,intervals[i][1])
            else:
                count+=1
        return count


        