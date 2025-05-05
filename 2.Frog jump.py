
class Solution:
    
    def helper(self, h, ind, dp):
        if ind == len(h) - 1:
            return 0
        if dp[ind] != -1:
            return dp[ind]
        one = abs(h[ind] - h[ind + 1]) + self.helper(h, ind + 1, dp)
        two = 2**63-1
        if ind + 2 <= len(h) - 1:
            two =  abs(h[ind] - h[ind + 2]) + self.helper(h, ind + 2, dp)
        
        dp[ind] = min(one, two)
        return dp[ind]
    
    
    def minCost(self, height):
        n = len(height)
        dp = [-1]*n
        return self.helper(height, 0, dp)

def main():
    heights = [20, 30, 40, 20] 
    sln = Solution()
    print(sln.minCost(heights))


if __name__ == "__main__":
    main()