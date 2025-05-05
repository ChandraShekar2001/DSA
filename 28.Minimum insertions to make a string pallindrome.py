class Solution:
    def helper(self, a, b, i, j, dp):
        if i < 0 or j < 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        ans = 0
        if a[i] == b[j]:
            ans = 1 + self.helper(a, b, i - 1, j - 1, dp)
        else:
            ans = max(self.helper(a, b, i - 1, j, dp), self.helper(a, b, i, j - 1, dp))
        dp[i][j] = ans
        return ans                

    def longestCommonSubsequence(self, text1, text2):
        dp = [[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        return self.helper(text1, text2, len(text1) - 1, len(text2) - 1, dp)

    
    def longestPalindromeSubseq(self, s: str) -> int:
        s1 = s 
        s2 = s[::-1]
        return self.longestCommonSubsequence(s1, s2)

    def minInsertions(self, s: str) -> int:
        return len(s) - self.longestPalindromeSubseq(s)
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()