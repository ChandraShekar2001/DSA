import sys
class Solution:
    def helper(self, m, n, r, c, grid, dp):
        if r >= m or c >= n or r < 0 or c < 0:
            return sys.maxsize
        if r == m - 1:
            return grid[r][c]
        
        if dp[r][c] !=sys.maxsize:
            return dp[r][c]
        
        leftdiag = self.helper(m, n, r + 1, c - 1, grid, dp)
        down = self.helper(m, n, r + 1, c, grid, dp)
        rightdiag = self.helper(m, n , r + 1, c + 1, grid, dp)
        
        dp[r][c] = min(leftdiag, down, rightdiag) + grid[r][c]
    
        return dp[r][c]        

    def minFallingPathSum(self, matrix) -> int:
        rows = len(matrix)
        ans = sys.maxsize
        for i in range(rows):
            dp = [[sys.maxsize for _ in range(rows)] for _ in range(rows)]
            ans = min(ans, self.helper(rows, rows, 0, i, matrix, dp))
            
        return ans
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()