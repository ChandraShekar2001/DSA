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
    
    def rob(self, nums) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        dp = [-1]*n
        one = self.helper(nums[1:], n - 1, 0, dp)
        dp = [-1]*n
        two = self.helper(nums[:n-1], n - 1, 0, dp)
        return max(one, two)

def main():
    ob = Solution()
    nums = [2,3,2]
    n = len(nums)
    print(ob.rob(nums))

if __name__ == "__main__":
    main()