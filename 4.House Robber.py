class Solution:
    def helper(self, nums, n, ind, dp):
        if ind >= n:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        #pick this element
        pick = nums[ind] + self.helper(nums, n, ind + 2, dp)
        
        #dont pick this element
        notPick = self.helper(nums, n, ind + 1, dp)
        
        dp[ind] = max(pick, notPick)
        
        return dp[ind]
    
    def rob(self, nums):
        n = len(nums)
        dp = [-1]*n
        return self.helper(nums,n, 0, dp)

def main():
    ob = Solution()
    nums = [1,2,3,1]
    print(ob.rob(nums))

if __name__ == "__main__":
    main()