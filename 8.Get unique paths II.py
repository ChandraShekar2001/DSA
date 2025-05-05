class Solution:
    def helper(self, m, n, r, c, obs, dp):
        if r >= m or c >= n or obs[r][c] == 1:
            return 0
        
        if r == m - 1 and c == n - 1:
            return 1
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        ans = self.helper(m, n, r, c + 1,obs,  dp) + self.helper(m, n, r + 1, c, obs, dp)
        dp[r][c] = ans
        return dp[r][c]
    
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(m, n, 0, 0, obstacleGrid, dp)
        

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()