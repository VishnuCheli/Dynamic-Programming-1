#Time Complexity:: Average: O(n)-2 seperate for loops to store and retrieve data from hset
#Space Complexity:: O(n)- Using an array as a hashset
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
class Solution(object):
    def deleteAndEarn(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hset=[0]*(max(nums)+1)
        
        for i in nums:
            hset[i]+=i
        
        dp=[0]*len(hset)
        
        dp[0]=0
        dp[1]=hset[1]
        
        for i in range(2,len(dp)):
            dp[i]=max((hset[i]+dp[i-2]),dp[i-1])
        return dp[i]