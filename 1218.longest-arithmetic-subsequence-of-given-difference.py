#https://leetcode-cn.com/problems/longest-arithmetic-subsequence-of-given-difference/

class Solution:

    # dynamics planning
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        res = 1
        dp = {}
        for num in arr:
            dp[num] = 1
            if num - difference in dp:
                dp[num] = dp[num - difference] + 1

        return max(dp.values())
