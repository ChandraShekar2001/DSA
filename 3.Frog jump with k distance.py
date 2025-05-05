import sys

class Solution:
    
    def helper(self, n, height, k, ind, dp):
        if ind == n - 1:
            return 0
        
        if dp[ind] != -1:
            return dp[ind]
        
        minSteps = sys.maxsize
        
        for i in range(k):
            if ind + i + 1 <= n - 1:
                minSteps = min(minSteps, abs(height[ind] - height[ind + i + 1]) +self.helper(n, height, k, ind + i + 1, dp))
                
        dp[ind] = minSteps
        
        return dp[ind]
    
    def frogJumpWithKSteps(self, n, height, k):
        dp = [-1]*n
        return self.helper(n, height, k, 0, dp)
    
    
    
def main():
    height = [30, 10, 60, 10, 60, 50]
    n = len(height)
    k = 2
    print(Solution().frogJumpWithKSteps(n, height, k))
    

if __name__=="__main__":
    main()