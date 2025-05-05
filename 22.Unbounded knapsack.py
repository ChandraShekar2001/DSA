import sys


class Solution:
    def helper(self, n, cap, val, wt, ind, weight, dp):
        if ind == n:
            if weight <= cap:
                return 0
            return -sys.maxsize
        
        if weight > cap:
            return -sys.maxsize
        
        if dp[ind][weight] != -1:
            return dp[ind][weight]
        
        #take
        take = self.helper(n, cap, val, wt, ind, weight + wt[ind], dp) + val[ind]
        #donttake 
        donttake = self.helper(n, cap, val, wt, ind + 1, weight, dp)
        
        dp[ind][weight] = max(take, donttake)
        return dp[ind][weight]
    
    def knapSack(self, val, wt, W):
        n = len(val)
        dp = [[-1 for _ in range(W + 1)] for _ in range(len(val))]
        ans = self.helper(n, W, val, wt, 0, 0, dp)
        return ans if ans != -sys.maxsize else 0

def main():
    ob = Solution()
    wt = [2, 4, 6]
    val = [5, 11, 13]
    W = 10
    n = len(wt)
    print(ob.unboundedKnapsack(n, W, val, wt))

if __name__ == "__main__":
    main()