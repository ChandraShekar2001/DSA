class Solution:
    def helper(self, ind, sum, n, arr, target, dp):
        if ind == n:
            return sum == target
        
        if dp[ind][sum] != -1:
            return dp[ind][sum]
        #take this element
        take = self.helper(ind + 1, sum + arr[ind], n, arr, target, dp)
        #dont take 
        donttake = self.helper(ind + 1, sum, n, arr, target, dp)
        
        dp[ind][sum] = take or donttake
        return dp[ind][sum]

    def minimumDifference(self, arr) -> bool:
        n = len(arr)
        total = sum(arr)
        if total % 2 == 1:
            return False
        dp = [[-1 for _ in range(total + 1)] for _ in range(n)]
        lastrow = dp[-1]
        miniDiff = total
        for i in range(1, len(lastrow)):
            if lastrow[i] == 1:
                miniDiff = min(miniDiff, abs(2*i - total))

        return miniDiff
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()