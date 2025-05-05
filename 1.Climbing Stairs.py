import sys
"""
You are climbing a staircase. It takes n steps to reach the top.
Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""
class Solution:

    def helper(self, ind, n, dp):
        if ind == n:
            return 1
        if dp[ind] != -1:
            return dp[ind]
        one = self.helper(ind + 1, n, dp)
        two = 0
        if ind + 2 <= n:
            two = self.helper(ind + 2, n, dp)
        
        dp[ind] = one + two
        
        return dp[ind]
    
    def climbStairs(self, n):
        dp = [-1]*n
        return self.helper(0, n, dp)


def main():
    sln = Solution()
    print(sln.climbStairs(38))
    
if __name__ == "__main__":
    main()