#Time Complexity:: Average: O(n)
#Space Complexity:: O(1) - Using no extra space for data structure
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp1=0;dp2=0;dp3=0
        
        if len(nums)==1:
            return nums[0]

        dp1=nums[0]

        dp2=max(nums[0],nums[1])
        
        for i in range(2,len(nums)): #698115 #69
            dp3=max((nums[i]+dp1),dp2)
            dp1,dp2=dp2,dp3
    
        return dp3 if len(nums)>2 else dp2