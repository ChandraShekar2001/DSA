class Solution:
    def helper(self, nums, target, sum, ind, dp):
        if ind == len(nums):
            return 1 if target == sum else 0
        
        if (ind, sum) in dp:
            return dp[(ind, sum)]
        
        #take positive
        takep = self.helper(nums, target, sum + nums[ind], ind + 1, dp)
        taken = self.helper(nums, target, sum - nums[ind], ind + 1, dp)
        
        dp[(ind, sum)] = takep + taken 
        
        return dp[(ind, sum)]
    
    def findTargetSumWays(self, nums, target: int) -> int:
        n = len(nums)
        dp = {}
        return self.helper(nums, target, 0, 0, dp)
def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()