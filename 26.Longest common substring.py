class Solution:
    def longestCommonSubstr(self, text1, text2):
        dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        n = len(text1)
        m = len(text2)
        for i in range(len(text2) + 1):
            dp[0][i] = 0
        for i in range(len(text1) + 1):
            dp[i][0] = 0
        ans = 0
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                    ans = max(ans, dp[i + 1][j +1])
                else:
                    dp[i + 1][j + 1] = 0
                    
        return ans

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()