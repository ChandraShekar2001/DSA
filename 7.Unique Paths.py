class Solution:
    def helper(self, m, n, r, c, dp):
        if r >= m or c >= n:
            return 0
        
        if r == m - 1 and c == n - 1:
            return 1
        
        if dp[r][c] != -1:
            return dp[r][c]
        
        ans = self.helper(m, n, r, c + 1, dp) + self.helper(m, n, r + 1, c, dp)
        dp[r][c] = ans
        return dp[r][c]
    
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.helper(m, n, 0, 0, dp)

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()