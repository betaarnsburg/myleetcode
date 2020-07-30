#https://leetcode-cn.com/problems/largest-rectangle-in-histogram/

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n, heights, st, ans = len(heights),[0] + heights + [0], [], 0
        for i in range(n + 2):
            while st and heights[st[-1]] > heights[i]:
                a = heights[st[-1]]
                st.pop()
                ans = max(ans, a * (i - 1 - st[-1]))
            st.append(i)
        return ans
