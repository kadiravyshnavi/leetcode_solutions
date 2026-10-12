class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        dict={5:0,10:0,20:0}
        for i in range(len(bills)):
            if bills[i]==5:
                dict[5]+=1
            elif bills[i]==10:
                if dict[5]>=1:
                    dict[5]-=1
                    dict[10]+=1
                else:
                    return False
            else:
                if dict[10]>=1 and dict[5]>=1:
                    dict[10]-=1
                    dict[5]-=1
                    dict[20]+=1
                elif dict[5]>=3:
                    dict[5]-=3
                    dict[20]+=1
                else:
                    return False
        return True