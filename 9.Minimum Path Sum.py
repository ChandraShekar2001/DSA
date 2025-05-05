import sys
class Solution:
    def helper(self, m, n, r, c, grid, dp):
        if r >= m or c >= n:
            return sys.maxsize
        if r == m - 1 and c == n - 1:
            return grid[r][c]
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        right = self.helper(m, n, r, c + 1, grid, dp) 
        down = self.helper(m, n, r + 1, c, grid, dp)
        dp[r][c] = min(right, down) + grid[r][c]
        return dp[r][c]
                
    
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(m, n, 0, 0, grid, dp)

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()