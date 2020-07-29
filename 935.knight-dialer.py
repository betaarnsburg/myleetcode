#https://leetcode-cn.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, N: int) -> int:
        cnt = 0
        jump = [[4, 6], [6, 8], [7, 9], [4, 8], [
            0, 3, 9], [], [0, 1, 7], [2, 6], [1, 3], [2, 4]]
        visited = dict()

        def helper(i, n):
            if (i, n) in visited: return visited[(i, n)]
            if n == 1:
                return 1
            cnt = 0
            for j in jump[i]:
                cnt += helper(j, n - 1)
            visited[(i, n)] = cnt
            return cnt
        for i in range(10):
            cnt += helper(i, N)
        return cnt % (10**9 + 7)
