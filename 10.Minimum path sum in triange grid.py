
class Solution:
    def helper(self, rows, r, c, triangle, dp):        
        if rows == r:
            return 0
        if dp[r][c] != -1:
            return dp[r][c]
        
        down = self.helper(rows, r + 1, c, triangle, dp)
        diag = self.helper(rows, r + 1, c + 1, triangle, dp)
        
        dp[r][c] = min(down, diag) + triangle[r][c]
        return dp[r][c]
    
    def minimumTotal(self, triangle):
        rows = len(triangle)
        cols = len(triangle[rows - 1])
        dp = [[-1 for _ in range(cols)] for _ in range(rows)]
        return self.helper(rows, 0, 0, triangle, dp)
    
    
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()