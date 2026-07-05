class Solution:
    def minDeletionstoPalindrome(self,s: str) -> int:
        n= len(s)
        # making an n*n 2D dp table
        dp = [[0]*n for i in range(n)]

        #all diagonals are 1
        for i in range(n):
            dp[i][i]= 1
        for length in range(2,n +1):
            for left in range(n-length+1):
                right = left + length+1

if __name__=="__main__":
    solution = Solution()
    print(solution.minDeletionstoPalindrome("abcdba"))
    print(solution.minDeletionstoPalindrome(""))
    print(solution.minDeletionstoPalindrome("ab"))
    print(solution.minDeletionstoPalindrome("a"))
    print(solution.minDeletionstoPalindrome("abcdefg"))
    print(solution.minDeletionstoPalindrome("abacaba"))
    print(solution.minDeletionstoPalindrome("abacada"))
    print(solution.minDeletionstoPalindrome("axbxcxa"))
