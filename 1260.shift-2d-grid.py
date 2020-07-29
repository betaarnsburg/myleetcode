#
# @lc app=leetcode.cn id=1260 lang=python3
#
# https://leetcode-cn.com/problems/shift-2d-grid/description/
#

# @lc code=start


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        n = len(grid)
        m = len(grid[0])
        # 2D to 1D
        arr = [grid[i][j] for i in range(n) for j in range(m)]
        k %= m * n
        res = []

        def reverse(l, r):
            while l < r:
                t = arr[l]
                arr[l] = arr[r]
                arr[r] = t
                l += 1
                r -= 1
        reverse(0, m * n - k - 1)
        reverse(m * n - k, m * n - 1)
        reverse(0, m * n - 1)
        # 1D to 2D
        row = []
        for i in range(m * n):
            if i > 0 and i % m == 0:
                res.append(row)
                row = []
            row.append(arr[i])
        res.append(row)

        return res

# @lc code=end
