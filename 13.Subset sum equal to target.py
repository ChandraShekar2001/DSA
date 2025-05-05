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

    def subsetSumToK(self, n, k, arr):
        n = len(arr)
        total = sum(arr) + 1
        dp = [[-1 for _ in range(sum)] for _ in range(n)]
        return self.helper(0, 0, n, arr, k, dp)
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main() 