class Solution:
    def shortestCommonSupersequence(self, text1, text2):
        dp = [[-1 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]
        n = len(text1)
        m = len(text2)
        for i in range(len(text2) + 1):
            dp[0][i] = 0
        for i in range(len(text1) + 1):
            dp[i][0] = 0
            
        for i in range(len(text1)):
            for j in range(len(text2)):
                if text1[i] == text2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j],dp[i][j + 1])
        i, j = n - 1, m - 1
        ans = ""
        while i >= 0 and j >= 0:
            if text1[i] == text2[j]:
                ans += text1[i]
                i -= 1
                j -= 1
            else:
                if dp[i][j + 1] > dp[i + 1][j]:
                    ans += text1[i]
                    i -= 1
                else:
                    ans += text2[j]
                    j -= 1
        
        while i >= 0:
            ans += text1[i]
            i -= 1

        while j >= 0:
            ans  += text2[j]
            j -= 1

        return ans[::-1]

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()