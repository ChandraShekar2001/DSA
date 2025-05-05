import sys
class Solution:
    def helper(self, i, aj, bj, m, n, grid):
        if i >= n or any(aj, bj) >= m or any(aj, bj) < 0:
            return -sys.maxsize
        
        if ai == m - 1:
            if aj == bj:
                return grid[ai][aj]
            return grid[ai][aj] + grid[bi][bj]
        
        ans = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                temp = self.helper(i + 1, aj + i, bj + j, m, n, grid)
                if aj== bj:
                    temp += grid[i][aj]
                else:
                    temp += (grid[i][aj] + grid[i][bj])
                ans = max(ans, temp)
        
        return ans
    
    def maximumChocolates(n, m, grid):
        pass

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()