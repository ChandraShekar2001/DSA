class Solution:
    def helper(self, nums, target, ind, sum, dp):
        if ind == len(nums):
            return sum == target
        
        if dp[ind][sum]  != -1:
            return dp[ind][sum]
        
        #choose the element
        take = self.helper(nums, target, ind + 1, sum + nums[ind], dp)
        #dont choose
        donttake = self.helper(nums, target, ind + 1, sum, dp)
        
        dp[ind][sum] = take + donttake
        return dp[ind][sum]
        

    def findWays(self, nums, k):
        n = len(nums)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        return self.helper(nums, k, 0, 0, dp)
def main():
    ob = Solution()
    arr = [0, 0, 1]
    target = 1
    print(ob.findWays(arr, target))

if __name__ == "__main__":
    main()