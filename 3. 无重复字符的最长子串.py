class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup = set()
        left, right, count, maxCount = -1, -1, 0, 0
        for ch in s:
            while ch in lookup:
                left += 1
                count -= 1
                lookup.remove(s[left])
            lookup.add(ch)
            count += 1
            if count > maxCount:
                maxCount = count
            right += 1
        return maxCount

result = Solution().lengthOfLongestSubstring('bbbbb')
print(result)