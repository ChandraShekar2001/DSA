import sys

class Solution:
    def helper(self, arr, row, prev, n, dp):
        if row == n:
            return 0
        if dp[row][prev + 1] != -1:
            return dp[row][prev + 1]
        
        maxPoints = -sys.maxsize
        for i in range(3):
            if i != prev or i == -1:
                maxPoints = max(maxPoints, arr[row][i] + self.helper(arr, row + 1, i, n, dp))
        dp[row][prev + 1] = maxPoints      
        return dp[row][prev + 1]
        
    def maximumPoints(self, arr):
        n = len(arr)
        dp = [[-1 for _ in range(4)] for _ in range(n)]
        return self.helper(arr, 0, -1, n, dp)
def main():
    ob = Solution()
    print(ob.maximumPoints())

if __name__ == "__main__":
    main()