import sys
class Solution:
    def helper(self, nums, target, ind, sum, dp):
        if target == sum:
            return 0
        
        if sum > target:
            return sys.maxsize
        
        if ind == len(nums):
            if sum == target:
                return 0
            return sys.maxsize
        
        if dp[ind][sum]  != -1:
            return dp[ind][sum]
        
        #choose the element
        take = 1 + self.helper(nums, target, ind, sum + nums[ind], dp)
        #dont choose
        donttake = self.helper(nums, target, ind + 1, sum, dp)
        
        dp[ind][sum] = min(take, donttake)
        return dp[ind][sum]

    def coinChange(self, coins, amount):
        pass
        

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()