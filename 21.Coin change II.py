class Solution:
    def helper(self, nums, target, ind, sum, dp):
        if target == sum:
            return 1
        
        if sum > target:
            return 0
        
        if ind == len(nums):
            if sum == target:
                return 1
            return 0
        
        if dp[ind][sum] != -1:
            return dp[ind][sum]
        
        #choose the element
        take = self.helper(nums, target, ind, sum + nums[ind], dp)
        #dont choose
        donttake = self.helper(nums, target, ind + 1, sum, dp)
        
        dp[ind][sum] = take + donttake
        return dp[ind][sum]
    
    def change(self, amount: int, coins):
        dp = [[-1 for _ in range(sum(coins))] for _ in range(len(coins))]
        return self.helper(coins, amount, 0, 0, dp)
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()