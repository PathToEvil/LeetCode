class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        d = [[False] * n for _ in range(n)]
        sub = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n:
                    break
                if i == j:
                    d[i][j] = True
                elif j == i + 1:
                    d[i][j] = s[i] == s[j]
                else:
                    d[i][j] = d[i+1][j-1] and s[i] == s[j]
                if d[i][j] and l + 1 > len(sub):
                    sub = s[i:j+1]
        return sub

result = Solution().longestPalindrome('cbbd')
print(result)