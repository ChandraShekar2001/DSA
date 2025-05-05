class Solution:
    
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        i, j = 0, 0
        ans = 0
        while(i < len(g) and j < len(s)):
            if g[i] <= s[j]:
                ans +=1
                i += 1
                j += 1
            else:
                j += 1 
        return ans

def main():
    ob = Solution()
    print("Hello, World!")

if __name__ == "__main__":
    main()